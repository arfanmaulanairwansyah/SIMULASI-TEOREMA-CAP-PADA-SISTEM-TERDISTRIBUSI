import time

class ServerNode:
    def __init__(self, nama):
        self.nama = nama
        self.data = {"status": "Sinkron", "saldo": 1000000}
        self.terhubung = True  # Status koneksi jaringan (Partition)

    def putus_koneksi(self):
        self.terhubung = False
        print(f"\n[!] GANGGUAN JARINGAN: {self.nama} terisolasi (Partition terjadi)!")

    def sambung_koneksi(self):
        self.terhubung = True
        print(f"\n[+] JARINGAN PULIH: {self.nama} kembali terhubung ke klaster.")

class KlasterDatabase:
    def __init__(self, mode):
        self.mode = mode  # 'CP' (MongoDB) atau 'AP' (Cassandra)
        self.node_utama = ServerNode("Node-1 (Utama/Lokal)")
        self.node_replika = ServerNode("Node-2 (Replika)")

    def tulis_data(self, saldo_baru):
        print(f"\n--- Mencoba Update Saldo menjadi Rp{saldo_baru:,} ---")
        time.sleep(1)

        # Jika jaringan normal (Tidak ada partisi)
        if self.node_utama.terhubung and self.node_replika.terhubung:
            self.node_utama.data["saldo"] = saldo_baru
            self.node_replika.data["saldo"] = saldo_baru
            print("[SUKSES] Data berhasil disimpan dan disinkronkan ke semua server.")
            return

        # JIKA TERJADI PARTISI JARINGAN (Node utama terputus dari replika)
        print("[INFO] Mendeteksi kegagalan komunikasi antar server...")
        time.sleep(1)

        if self.mode == "CP":
            # Model CP: Prioritas Konsistensi (Contoh: MongoDB)
            print("[ERROR] MongoServerError: not primary / no quorum.")
            print(">> SIMULASI CP: Request DITOLAK sementara untuk mencegah data tidak sinkron.")
        
        elif self.mode == "AP":
            # Model AP: Prioritas Ketersediaan (Contoh: Apache Cassandra)
            self.node_utama.data["saldo"] = saldo_baru
            self.node_utama.data["status"] = "Belum Sinkron (Stale Data)"
            print("[SUKSES] Data disimpan sementara di penyimpanan lokal Node-1.")
            print(">> SIMULASI AP: Layanan TETAP AKTIF melayani pengguna (Eventual Consistency).")

    def baca_data(self):
        print("\n--- Membaca Data dari Server ---")
        print(f"Data di {self.node_utama.nama} : Saldo = Rp{self.node_utama.data['saldo']:,} | Status = {self.node_utama.data['status']}")
        print(f"Data di {self.node_replika.nama}   : Saldo = Rp{self.node_replika.data['saldo']:,} | Status = {self.node_replika.data['status']}")


def jalankan_simulasi():
    while True:
        print("\n==================================================")
        print("   SIMULASI TEOREMA CAP - KELOMPOK 4 (SCALABLE)")
        print("==================================================")
        print("Pilih Model Database yang ingin disimulasikan:")
        print("1. Model CP (MongoDB / Sistem Perbankan)")
        print("2. Model AP (Apache Cassandra / Media Sosial)")
        print("3. Keluar Program")
        
        pilihan = input("\nMasukkan pilihan (1/2/3): ")

        if pilihan == "3":
            print("Terima kasih! Program selesai.")
            break
        elif pilihan not in ["1", "2"]:
            print("Pilihan tidak valid.")
            continue

        mode = "CP" if pilihan == "1" else "AP"
        nama_db = "MongoDB (CP)" if mode == "CP" else "Apache Cassandra (AP)"
        
        db = KlasterDatabase(mode)
        print(f"\n>>> Memulai Klaster Database: {nama_db} <<<")
        
        # 1. Kondisi Normal
        print("\n[KONDISI 1: JARINGAN NORMAL]")
        db.baca_data()
        db.tulis_data(1500000)
        db.baca_data()

        # 2. Kondisi Terjadi Partisi Jaringan (Partition Tolerance diuji)
        print("\n--------------------------------------------------")
        print("[KONDISI 2: TERJADI GANGGUAN JARINGAN / PARTITION]")
        db.node_utama.putus_koneksi()
        
        # Mencoba melakukan transaksi saat jaringan putus
        db.tulis_data(2000000)
        db.baca_data()
        
        input("\nTekan [ENTER] untuk kembali ke menu utama...")

if __name__ == "__main__":
    jalankan_simulasi()