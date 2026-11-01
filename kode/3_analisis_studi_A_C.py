"""
Analisis Studi A dan Studi C untuk buku *Membaca Angka, Menilai Riset* (Negara, 2026).

Mereproduksi angka di Subbab 4.5 (Tabel 4.x, studiA dan studiA-umur) dan
Subbab 10.3 (Tabel 10.x, studiC dan Gambar sebaran skor) dari data turunan
di folder ../data.

Pemakaian:
    pip install pandas numpy scipy
    python 3_analisis_studi_A_C.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats


def wilson(k, n, z=1.959964):
    p = k / n
    den = 1 + z**2 / n
    mid = (p + z**2 / (2 * n)) / den
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / den
    return mid - half, mid + half

DATA = Path(__file__).resolve().parent.parent / "data"
A = pd.read_csv(DATA / "studiA_artikel.csv")
C = pd.read_csv(DATA / "studiC_skor.csv")
J = pd.read_csv(DATA / "studiA_penyaringan_jurnal_agregat.csv")


def judul(t):
    print("\n" + "=" * 70 + f"\n{t}\n" + "=" * 70)


# ---------------------------------------------------------------- Studi A
judul("STUDI A: penyaringan jurnal")
print(J.set_index("bidang").T.to_string())

judul("STUDI A: Tabel cakupan (persen)")
A["kelompok"] = A.bidang + " " + A.kelompok_peringkat
kol = {"doi_di_metadata": "DOI tercantum di metadata",
       "doi_terdaftar_crossref": "DOI terdaftar (Crossref)",
       "doi_aktif": "Punya DOI yang aktif",
       "doi_tidak_terdaftar": "DOI tercantum tetapi tidak terdaftar",
       "terindeks_openalex": "Terindeks OpenAlex"}
tab = A.groupby("kelompok")[list(kol)].mean().mul(100).T
tab["Total"] = A[list(kol)].mean().mul(100)
tab.index = [kol[i] for i in tab.index]
print(tab.round(1).to_string())
print("\nJurnal per kelompok:", A.groupby("kelompok").kode_jurnal.nunique().to_dict())
for k in ["doi_aktif", "doi_tidak_terdaftar", "terindeks_openalex"]:
    lo, hi = wilson(A[k].sum(), len(A))
    print(f"Wilson 95% {k}: {lo*100:.1f}-{hi*100:.1f}")
print("Ditemukan lewat:", A.dicocokkan_lewat.fillna("").value_counts().to_dict())
print("DOI tidak terdaftar dan tidak di OpenAlex:",
      int((A.doi_tidak_terdaftar & ~A.terindeks_openalex).sum()))
print("Label bahasa metadata keliru:", int(A.label_bahasa_keliru.sum()))

judul("STUDI A: sitasi OpenAlex")
O = A[A.terindeks_openalex]
s = O.sitasi_openalex
print(f"n={len(O)} median={s.median():.0f} rata-rata={s.mean():.2f} "
      f"belum dikutip={100*(s == 0).mean():.1f}%")
top = s.sort_values(ascending=False).head(round(len(s) * 0.1)).sum() / s.sum()
print(f"10% teratas menyumbang {100*top:.0f}% sitasi")
umur = O.groupby("tahun_terbit").sitasi_openalex.agg(
    artikel="size", median="median", rata_rata="mean",
    belum_dikutip=lambda x: 100 * (x == 0).mean())
print(umur.round(1).to_string())
print("Median per bidang dan peringkat:")
print(O.groupby(["bidang", "kelompok_peringkat"]).sitasi_openalex.median().to_string())

# ---------------------------------------------------------------- Studi C
judul("STUDI C: skor LLM versi Indonesia dan Inggris")
print("Jumlah penilaian:", len(C), C.model.value_counts().to_dict())
cit = A.set_index("id_artikel").sitasi_openalex
mm = C.groupby(["model", "id_artikel", "bahasa_versi"]).skor.mean().unstack()
for model in ["Gemini", "ChatGPT"]:
    x = mm.loc[model]
    d = x.en - x.id
    rng = np.random.default_rng(2026)
    boot = [rng.choice(d.values, len(d)).mean() for _ in range(5000)]
    lo, hi = np.percentile(boot, [2.5, 97.5])
    ulang = C[C.model == model].groupby(["id_artikel", "bahasa_versi"]).skor.nunique()
    avg = (x.en + x.id) / 2
    ok = cit.reindex(avg.index).notna()
    rho = stats.spearmanr(avg[ok], cit.reindex(avg.index)[ok]).correlation
    print(f"\n{model}")
    print(f"  rata-rata ID={x.id.mean():.2f}  EN={x.en.mean():.2f}  selisih EN-ID={d.mean():+.3f}"
          f"  (bootstrap 95%: {lo:+.3f} s.d. {hi:+.3f})")
    print(f"  skor sama={100*(d == 0).mean():.0f}%  EN lebih tinggi:lebih rendah={int((d > 0).sum())}:{int((d < 0).sum())}"
          f"  Wilcoxon p={stats.wilcoxon(x.en, x.id).pvalue:.3f}")
    print(f"  kelima ulangan identik={100*(ulang == 1).mean():.0f}%  rho(sitasi)={rho:.2f} (n={ok.sum()})")
    print("  sebaran skor (%):", C[C.model == model].skor.value_counts(normalize=True)
          .sort_index().mul(100).round(1).to_dict())

g = mm.loc["Gemini"].mean(axis=1)
o = mm.loc["ChatGPT"].mean(axis=1)
print(f"\nKorelasi peringkat antarmodel: {stats.spearmanr(g, o.reindex(g.index)).correlation:.2f}")
print(f"Artikel dengan tingkat sama di kedua model: {100*(g.round() == o.reindex(g.index).round()).mean():.0f}%")
