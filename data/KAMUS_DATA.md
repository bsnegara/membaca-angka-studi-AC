# Kamus data

## studiA_artikel.csv (300 baris)

| Kolom | Isi |
|---|---|
| `id_artikel` | Kode acak artikel, A001–A300 |
| `kode_jurnal` | Kode acak jurnal, J01–J17 |
| `bidang` | `informatika` atau `manajemen` (manajemen dan bisnis) |
| `kelompok_peringkat` | Peringkat akreditasi jurnal: `1-2` atau `3-4` |
| `tahun_terbit` | 2021–2023 |
| `jumlah_penulis` | Jumlah penulis menurut metadata OAI |
| `label_bahasa_metadata` | Bahasa abstrak menurut label metadata: `en`, `id`, atau `dua` |
| `bahasa_abstrak_penulis` | Bahasa abstrak tulisan penulis menurut deteksi otomatis (`langdetect`): `en`, `id`, atau `dua` |
| `label_bahasa_keliru` | `True` bila kedua kolom di atas berbeda |
| `doi_di_metadata` | Metadata OAI jurnal mencantumkan DOI |
| `doi_terdaftar_crossref` | DOI dikenali API Crossref |
| `doi_tidak_terdaftar` | DOI tercantum tetapi tidak dikenali Crossref maupun doi.org (dicek ulang) |
| `doi_org_mengenali_doi` | Hanya untuk baris `doi_tidak_terdaftar`: hasil pemeriksaan API handle doi.org |
| `doi_hanya_dari_openalex` | DOI tidak tercantum di metadata, tetapi ditemukan di OpenAlex |
| `doi_aktif` | `doi_terdaftar_crossref` atau `doi_hanya_dari_openalex` |
| `terindeks_openalex` | Artikel ditemukan di OpenAlex |
| `dicocokkan_lewat` | `doi`, `judul` (kecocokan judul ≥90 dan tahun ±1), atau kosong |
| `sitasi_openalex` | Jumlah sitasi OpenAlex per 27 Oktober 2026 (kosong bila tidak terindeks) |

## studiA_penyaringan_jurnal_agregat.csv

Hasil memanen metadata OAI-PMH dari 47 jurnal kandidat, per bidang. Kolom `abstrak_*` dihitung untuk jurnal yang punya artikel 2021–2023: `dua_bahasa` bila minimal 50% rekaman memuat abstrak Indonesia dan Inggris; `hanya_inggris` bila rekaman berabstrak Indonesia ≤5%; `hanya_indonesia` bila rekaman berabstrak Inggris ≤5%; selebihnya `campuran`.

## studiC_skor.csv (6.000 baris)

| Kolom | Isi |
|---|---|
| `id_artikel` | Kode acak artikel, sama dengan Studi A |
| `model` | `Gemini` atau `ChatGPT` |
| `versi_model` | `gemini-3.8-flash` atau `gpt-4.1-mini-2025-04-14` |
| `bahasa_versi` | Versi yang dinilai: `id` atau `en` |
| `sumber_teks` | `penulis` (teks asli penulis) atau `mesin` (terjemahan NLLB-200, `facebook/nllb-200-distilled-600M`) |
| `ulangan` | 0–4 |
| `skor` | Skor mutu 1–4 ala REF (4 = world-leading, 1 = recognised nationally) |
| `waktu` | Waktu penilaian tercatat |
