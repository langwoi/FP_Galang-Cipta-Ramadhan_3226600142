# Final Project Oprec PENSHIP - Galang Cipta Ramadhan (3226600142)

## Identitas
- Nama: Galang Cipta Ramadhan
- NRP: 3226600142
- Program studi: 1 CE D

## Project Roboflow
- Project ID Roboflow: 13-galang-cipta-ramadhan, version 6
- Link Roboflow Universe: https://universe.roboflow.com/13-galang-cipta-ramadhan/belajar-train-data

## Dataset
- Jumlah foto asli: bottle 110+, laptop 80, pencil 50
- Metode pengambilan foto: variasi jarak 1-3Meter, sudut , cahaya 50% dan 100%, dan latar : Kamar>
- Fitur AI labeling Roboflow yang digunakan (apabila ada) dan cara perapiannya: Tidak Pakai AI

## Training
- Lingkungan training: laptop Nvidia RTX 4050
- Model: yolov8n
- Grafik: lihat folder grafik/

## Pengembangan Kode
Daftar perubahan terhadap kode dasar, beserta alasan dan pengaruhnya terhadap hasil:
1. Penyesuaian Jumlah Epoch dari 50 Menjadi 20, Alasannya : Menyesuaikan durasi pelatihan agar lebih efisien dan cepat dalam tahap pengujian serta validasi model.
2. Merubah Batch Yang nilai awalnya 16 kuturunkan menjadi 8, Alasannya : Penggunaan memori GPU menjadi jauh lebih aman dan stabil, memastikan keseluruhan proses pelatihan berjalan lancar tanpa risiko crash.
3. Penambahan Parameter workers (Diset ke 0) pada Fungsi Train,Alasannya : Mencegah konflik multiprocessing di sistem operasi Windows yang sering kali memicu error memori virtual (WinError 1455 / Paging file too small) saat memuat pustaka CUDA.

## Hasil Eksperimen
| No | Skenario | Epochs | Batch | Optimizer | mAP50 | mAP50-95 | Keterangan |
|:--:|:---|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | Baseline (kode dasar) | 50 | 16 | auto | ... | ... | Titik acuan,Error karena belum menambahkan parameter workers |
| 1 | Menambahkan Workers | 20 | 16 | auto | 1.0 | 0.72 | Berhasil Tapi data yang ketrack lambat |
| 2 | Menambahkan Workers | 15 | 16 | auto | 0.7 | 0.9 | Berhasil Tapi Data Yang ketrack kurang optimal |
| 3 | Menambahkan Workers | 50 | 16 | auto | 1.0 | 0.75 | Berhasil Tapi Ada Sedikit False Positive |
| 4 | Menambahkan Workers | 60 | 16 | auto | 1.0 | 0.78 | Berhasil dengan optimal |

## Analisis dan Kendala
- Analisis penyebab skenario terbaik menghasilkan nilai lebih tinggi: Skenario ke 4 menghasilkan nilai metrik evaluasi yang paling optimal dibandingkan epoch yang lebih rendah.hal ini disebabkan karena jumlah epoch yang lebih banyak memberikan ruang iterasi yang cukup bagi model untuk mencapai konvergensi penuh,memahami pola gambar secara mendalam,serta meminimalisasi underfiting 
- Kendala yang ditemui dan cara penyelesaiannya: False Positive Cara Penyelesaiannya Adalah menambahkan background no object ke dalam dataset,hal ini dilakukan agar model tahu kapan object tidak ada
