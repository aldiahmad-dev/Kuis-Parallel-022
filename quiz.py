import multiprocessing
import os
import time

# --- BAGIAN DATA PARALLELISM (FOKUS UTAMA NRP GENAP) ---
def proses_sensor_data(nilai_input):
    """
    Data Parallelism: Fungsi yang sama mengeksekusi data yang berbeda.
    Simulasi pengolahan data sensor mentah menjadi nilai terkalibrasi.
    """
    hasil_kalibrasi = nilai_input * 1.5 + 10  # Contoh rumus sederhana
    print(f"[Data Parallel] Input: {nilai_input} -> Hasil: {hasil_kalibrasi:.2f} | Worker PID: {os.getpid()}")
    return hasil_kalibrasi

# --- BAGIAN TASK PARALLELISM (PELENGKAP) ---
def log_aktivitas_sistem():
    """Tugas A: Mencatat aktivitas sistem ke log"""
    print(f"[Task Parallel] Mencatat log ke sistem... | PID: {os.getpid()}")
    time.sleep(1.5)
    print("[Task Parallel] Pencatatan log selesai.")

def cek_status_koneksi():
    """Tugas B: Mengecek status koneksi jaringan (Tugas yang berbeda)"""
    print(f"[Task Parallel] Mengecek sinkronisasi database... | PID: {os.getpid()}")
    time.sleep(2.5)
    print("[Task Parallel] Sinkronisasi database OK.")

if __name__ == "__main__":
    print(f"=== Eksekusi Program - NRP: 022 ===")
    print(f"Main Process PID: {os.getpid()}\n")

    # 1. Implementasi Data Parallelism (Sesuai instruksi untuk NRP Genap)
    # Mengolah list data sensor menggunakan multiple cores
    dataset_sensor = [22, 45, 67, 12, 89, 34]
    print("--- Memulai Data Parallelism (Processing Sensor Array) ---")
    
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        hasil_akhir = pool.map(proses_sensor_data, dataset_sensor)
    
    print(f"Hasil Akhir Data: {hasil_akhir}")
    print(f"Waktu eksekusi Data Parallel: {time.time() - start_time:.4f} detik\n")

    # 2. Implementasi Task Parallelism
    # Menjalankan dua tugas berbeda (Log vs Network Check) secara bersamaan
    print("--- Memulai Task Parallelism (Multitasking Operations) ---")
    proses_log = multiprocessing.Process(target=log_aktivitas_sistem)
    proses_cek = multiprocessing.Process(target=cek_status_koneksi)

    proses_log.start()
    proses_cek.start()

    proses_log.join()
    proses_cek.join()

    print("\n=== Seluruh Proses Quiz Selesai ===")