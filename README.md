# Data, kode, dan protokol Studi A dan Studi C
## Buku *Membaca Angka, Menilai Riset: Memahami dan Mengkritisi Indikator Riset bagi Dosen dan Peneliti Indonesia*

Penulis: Benny Sukma Negara (UIN Sultan Syarif Kasim Riau, ORCID 0000-0001-8455-0912)

Repositori: https://github.com/bsnegara/membaca-angka-studi-ac · Arsip permanen: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23854536.svg)](https://doi.org/10.5281/zenodo.23854536)

Pertanyaan atau laporan kesalahan: silakan buka *Issue* di repositori ini.

Arsip ini memuat bahan untuk memeriksa dan mengulang dua studi empiris dalam buku:

* **Studi A (Subbab 4.5):** cakupan DOI, Crossref, dan OpenAlex untuk 300 artikel terbitan 2021–2023 dari 17 jurnal terakreditasi Indonesia (informatika serta manajemen dan bisnis). Data dikumpulkan 27 Oktober 2026.
* **Studi C (Subbab 10.3):** 6.000 skor mutu dari dua model bahasa besar (`gemini-3.8-flash` dan `gpt-4.1-mini-2025-04-14`) untuk versi berbahasa Indonesia dan Inggris dari 300 artikel yang sama. Data dikumpulkan 27–31 Oktober 2026.

## Isi

| Berkas | Isi |
|---|---|
| `protokol/Protokol_Studi_A_C_v1.2.pdf` | Protokol penelitian versi 1.2, termasuk catatan semua perubahan rancangan |
| `kode/1_Studi_A_C_persiapan_data.ipynb` | Notebook Colab: penyaringan jurnal, sampel artikel, pemeriksaan DOI/Crossref/OpenAlex, terjemahan NLLB-200 |
| `kode/2_Studi_C_penilaian_LLM.ipynb` | Notebook Colab: penilaian Gemini dan ChatGPT (instruksi penilaian lengkap ada di notebook) |
| `kode/3_analisis_studi_A_C.py` | Skrip yang mereproduksi semua angka Studi A dan C di buku dari data di folder `data/` |
| `data/studiA_artikel.csv` | 300 baris, satu per artikel: kelompok, tahun, status DOI, Crossref, OpenAlex, sitasi |
| `data/studiA_penyaringan_jurnal_agregat.csv` | Hasil penyaringan 47 jurnal kandidat, diagregasi per bidang |
| `data/studiC_skor.csv` | 6.000 baris, satu per penilaian: model, versi bahasa, sumber teks, ulangan, skor |
| `data/KAMUS_DATA.md` | Penjelasan setiap kolom |

Mereproduksi angka buku:

```
pip install pandas numpy scipy
python kode/3_analisis_studi_A_C.py
```

## Batasan akses

Sesuai protokol, buku hanya melaporkan hasil agregat dan tidak menyebut jurnal atau artikel satu per satu. Karena itu:

1. **Identitas jurnal dan artikel diganti kode acak.** Artikel diberi kode `A001`–`A300` dan jurnal `J01`–`J17`. Kode ini tidak dapat dicocokkan dengan kode internal notebook.
2. **Tidak didistribusikan ulang:** judul, abstrak, terjemahan abstrak, DOI, pengenal OAI, alamat jurnal, daftar 47 jurnal kandidat, dan teks alasan yang ditulis model. Abstrak dan judul adalah karya penulis artikel dengan lisensi yang berbeda-beda antarjurnal; DOI dan alamat jurnal akan membuka identitas jurnal.
3. **Notebook versi publik** sama dengan yang dijalankan, kecuali daftar jurnal kandidat dan peringkat manual dikosongkan, dan email kontak API diganti contoh. Kunci API tidak pernah disimpan di notebook (dibaca dari Colab Secrets).
4. **Protokol versi publik** sama dengan versi 1.2, kecuali nama enam jurnal yang peringkatnya dicek ulang dihapus.

Untuk keperluan verifikasi ilmiah (misalnya oleh penelaah atau peneliti yang ingin mengulang studi), data lengkap dapat diminta kepada penulis dengan alasan yang jelas dan kesediaan untuk tidak menerbitkan hasil per jurnal.

## Catatan waktu

Protokol ditulis sebelum data dikumpulkan, tetapi diarsipkan di repositori ini setelah data terkumpul. Arsip ini karena itu bukan praregistrasi; semua perubahan rancangan dicatat di dalam protokol beserta alasannya.

## Lisensi

* Data dan protokol: Creative Commons Attribution 4.0 International (CC BY 4.0), lihat `LICENSE-data.txt`.
* Kode: MIT, lihat `LICENSE-code.txt`.

## Cara mengutip

Negara, B. S. (2026). *Data, kode, dan protokol Studi A dan Studi C untuk buku Membaca Angka, Menilai Riset* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23854536
