# CODE SECARA STATIS 

# class siswa :
#     def __init__(self, nama, nis):
#         self.nama = nama
#         self.nis = nis
#         self.nilai_ujian = []

#     def tambah_nilai(self, nilai):
#         if isinstance(nilai, (int, float)) and 0 <= nilai <= 100:
#             self.nilai_ujian.append(nilai)
#         else:
#             print("Nilai yang dimasukan harus berupa angka")

#     def hitung_rata_rata(self):
#         if not self.nilai_ujian:
#             return 0 
#         return sum(self.nilai_ujian) / len(self.nilai_ujian)
    
#     def tampilkan_info(self):
#         print(f"Nama: {self.nama}")
#         print(f"NIS: {self.nis}")
#         print(f"Nilai Ujian: {self.nilai_ujian}")
#         print(f"Rata-rata Nilai Ujian: {self.hitung_rata_rata():2f}")

# # Penggunaan 
# siswa1 = siswa("Gibransyah Agung Kusuma", "23.01.5002")
# siswa1.tambah_nilai(80)
# siswa1.tambah_nilai(90)
# siswa1.tambah_nilai(85)
# siswa1.tampilkan_info()



# CODE SECARA DINAMIS MAKA DATA YANG SUDAH DIINPUTKAN AKAN OTOMATIS MASUK KE DALAM FILE .JSON

import json
import os

class Siswa:
    def __init__(self, nama, nis, nilai_ujian=None):
        self.nama = nama
        self.nis = nis
        self.nilai_ujian = nilai_ujian or []
    
    def tambah_nilai(self, nilai):
        if isinstance(nilai, (int, float)) and 0 <= nilai <= 100:
            self.nilai_ujian.append(nilai)
        else:
            print("Nilai yang dimasukkan harus berupa angka antara 0 dan 100.")
    
    def hitung_rata_rata(self):
        return sum(self.nilai_ujian) / len(self.nilai_ujian) if self.nilai_ujian else 0
    
    def tampilkan_info(self):
        return {
            "Nama": self.nama,
            "NIS": self.nis,
            "Nilai Ujian": self.nilai_ujian,
            "Rata-rata Nilai Ujian": round(self.hitung_rata_rata(), 2)
        }
    
    def to_dict(self):
        return self.__dict__

def simpan_data(siswa_list, filename="siswa.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([s.to_dict() for s in siswa_list], file, indent=4)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")

def baca_data(filename="siswa.json"):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [Siswa(**d) for d in json.load(file)]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Gagal membaca data: {e}")
        return []

def main():
    siswa_list = baca_data()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tambah Nilai")
        print("3. Tampilkan Info Siswa")
        print("4. Tampilkan Semua Data")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            nis = input("Masukkan NIS siswa: ")
            siswa_list.append(Siswa(nama, nis))
            simpan_data(siswa_list)
        elif pilihan == "2":
            nis = input("Masukkan NIS siswa: ")
            siswa = next((s for s in siswa_list if s.nis == nis), None)
            if siswa:
                try:
                    nilai = float(input("Masukkan nilai ujian: "))
                    siswa.tambah_nilai(nilai)
                    simpan_data(siswa_list)
                except ValueError:
                    print("Nilai harus berupa angka.")
            else:
                print("Siswa tidak ditemukan.")
        elif pilihan == "3":
            nis = input("Masukkan NIS siswa: ")
            siswa = next((s for s in siswa_list if s.nis == nis), None)
            if siswa:
                print(json.dumps(siswa.tampilkan_info(), indent=4))
            else:
                print("Siswa tidak ditemukan.")
        elif pilihan == "4":
            print("Data Semua Siswa:")
            print(json.dumps([s.tampilkan_info() for s in siswa_list], indent=4))
        elif pilihan == "5":
            simpan_data(siswa_list)
            print("Data disimpan ke siswa.json. Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
