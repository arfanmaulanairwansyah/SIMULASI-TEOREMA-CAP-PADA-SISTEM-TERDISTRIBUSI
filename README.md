# Simulasi Teorema CAP (Consistency, Availability, Partition Tolerance)

Proyek ini merupakan program simulasi berbasis Python yang dibuat untuk mendemonstrasikan implementasi **Teorema CAP** dalam sistem terdistribusi. Simulasi ini membandingkan dua pendekatan arsitektur database saat menghadapi partisi jaringan (gangguan komunikasi), yaitu model **CP (Consistency & Partition Tolerance)** dan model **AP (Availability & Partition Tolerance)**.

Tugas ini disusun untuk memenuhi tugas kuliah **Sistem Terdistribusi / Arsitektur Skalabel (Kelompok 4)**.

---

## 📌 Anggota Kelompok 4 (Scalable)
* **Syahlan** (Lann)
* *[Silakan isi nama anggota lain di sini jika ada]*
* *[Silakan isi nama anggota lain di sini jika ada]*

---

## 🛠️ Penjelasan Teorema CAP dalam Simulasi

Teorema CAP menyatakan bahwa sebuah sistem data terdistribusi hanya dapat menjamin maksimal dua dari tiga karakteristik berikut secara bersamaan:
1. **Consistency (Konsistensi):** Setiap proses membaca akan menerima data terbaru atau error.
2. **Availability (Ketersediaan):** Setiap request non-gagal akan menerima respons (bukan error), tanpa jaminan bahwa itu berisi data terbaru.
3. **Partition Tolerance (Toleransi Partisi):** Sistem terus beroperasi meskipun ada gangguan komunikasi antar node.

### Skenario yang Disimulasikan dalam Kode:
* **Kondisi 1 (Jaringan Normal):** Baik model CP maupun AP dapat melakukan sinkronisasi data dengan lancar antara `Node-1 (Utama)` dan `Node-2 (Replika)`.
* **Kondisi 2 (Terjadi Partisi Jaringan):** Ketika koneksi antar node terputus:
  * **Model CP (Contoh: MongoDB / Sistem Perbankan):** Memprioritaskan konsistensi data. Sistem akan menolak operasi tulis (`tulis_data`) dan mengembalikan *error* demi mencegah terjadinya data yang tidak sinkron (*stale/split-brain*).
  * **Model AP (Contoh: Apache Cassandra / Media Sosial):** Memprioritaskan ketersediaan layanan. Sistem tetap menerima operasi tulis di node lokal (`Node-1`), meskipun mengakibatkan data di node replika menjadi tidak sinkron sementara waktu (*Eventual Consistency*).

---

## 🚀 Fitur Program

* **Simulasi Arsitektur CP:** Simulasi penolakan transaksi saat jaringan eror (*No Quorum / Not Primary Error*).
* **Simulasi Arsitektur AP:** Simulasi penerimaan data lokal dengan status *Stale Data* demi menjaga sistem tetap aktif.
* **Interaktif:** Berbasis CLI (*Command Line Interface*) yang mudah dipahami dengan visualisasi perubahan saldo dan status node secara real-time.

---

## 💻 Struktur Kode Utama (`simulasi_cap.py`)

Program ini menggunakan dua class utama untuk mensimulasikan lingkungan klaster database:
* **`ServerNode`**: Merepresentasikan sebuah server node dengan data saldo dan status koneksinya.
* **`KlasterDatabase`**: Mengelola logika pembagian sistem berdasarkan pilihan mode (`CP` atau `AP`) saat terjadi *network partition*.

---

## 🏃‍♂️ Cara Menjalankan Program

### Prasyarat
* Pastikan kamu sudah menginstal **Python 3.x** di perangkatmu.

### Langkah-langkah
1. **Clone repositori ini** atau unduh file `simulasi_cap.py`.
   ```bash
   git clone [https://github.com/username/repository-name.git](https://github.com/username/repository-name.git)
   cd repository-name

1. Jalankan script python melalui terminal atau command promt:
   python simulasi_cap.py

2. Pilih menu simulasi yang ingin dijalankan (1 untuk CP, 2 untuk AP, atau 3 untuk keluar).

📊 Contoh Output Program
1. Pilihan Model CP (Consistency)
Plaintext
[KONDISI 2: TERJADI GANGGUAN JARINGAN / PARTITION]

[!] GANGGUAN JARINGAN: Node-1 (Utama/Lokal) terisolasi (Partition terjadi)!

--- Mencoba Update Saldo menjadi Rp2,000,000 ---
[INFO] Mendeteksi kegagalan komunikasi antar server...
[ERROR] MongoServerError: not primary / no quorum.
>> SIMULASI CP: Request DITOLAK sementara untuk mencegah data tidak sinkron.
2. Pilihan Model AP (Availability)
Plaintext
[KONDISI 2: TERJADI GANGGUAN JARINGAN / PARTITION]

[!] GANGGUAN JARINGAN: Node-1 (Utama/Lokal) terisolasi (Partition terjadi)!

--- Mencoba Update Saldo menjadi Rp2,000,000 ---
[INFO] Mendeteksi kegagalan komunikasi antar server...
[SUKSES] Data disimpan sementara di penyimpanan lokal Node-1.
>> SIMULASI AP: Layanan TETAP AKTIF melayani pengguna (Eventual Consistency).

Kamu tinggal *copy-paste* seluruh teks di dalam blok kode di atas dan simpan dengan na

