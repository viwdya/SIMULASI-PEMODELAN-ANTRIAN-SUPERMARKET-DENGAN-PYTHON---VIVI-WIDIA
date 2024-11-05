import numpy as np
import matplotlib.pyplot as plt

# Parameter simulasi
jumlah_pelanggan = 10           # Jumlah pelanggan yang akan disimulasikan
lmbda_kedatangan = 1/5          # Rata-rata waktu antar kedatangan (5 menit)
lmbda_layanan = 1/4             # Rata-rata waktu layanan per pelanggan (4 menit)

# Variabel untuk menyimpan data
waktu_kedatangan = []           # Waktu kedatangan setiap pelanggan
waktu_layanan = []              # Waktu layanan setiap pelanggan
waktu_mulai_layanan = []        # Waktu mulai layanan
waktu_selesai_layanan = []      # Waktu selesai layanan
waktu_tunggu = []               # Waktu tunggu setiap pelanggan dalam antrian

# Fungsi untuk menghasilkan waktu antar kedatangan dan waktu layanan
def generate_kedatangan(lmbda):
    return np.random.exponential(1 / lmbda)

def generate_layanan(lmbda):
    return np.random.exponential(1 / lmbda)

# Simulasi antrian
waktu_kedatangan.append(0)  # Waktu kedatangan pelanggan pertama
for i in range(1, jumlah_pelanggan):
    waktu_kedatangan.append(waktu_kedatangan[i-1] + generate_kedatangan(lmbda_kedatangan))
    
for i in range(jumlah_pelanggan):
    waktu_layanan.append(generate_layanan(lmbda_layanan))
    if i == 0:
        waktu_mulai_layanan.append(waktu_kedatangan[i])
    else:
        waktu_mulai_layanan.append(max(waktu_kedatangan[i], waktu_selesai_layanan[i-1]))
    waktu_selesai_layanan.append(waktu_mulai_layanan[i] + waktu_layanan[i])
    waktu_tunggu.append(waktu_mulai_layanan[i] - waktu_kedatangan[i])

# Hasil Simulasi
rata_rata_waktu_tunggu = np.mean(waktu_tunggu)
rata_rata_waktu_layanan = np.mean(waktu_layanan)

print("Rata-rata waktu tunggu: {:.2f} menit".format(rata_rata_waktu_tunggu))
print("Rata-rata waktu layanan: {:.2f} menit".format(rata_rata_waktu_layanan))

# Plotting
plt.figure(figsize=(10, 6))

# Grafik waktu tunggu
plt.subplot(2, 1, 1)
plt.plot(range(jumlah_pelanggan), waktu_tunggu, color="blue", marker="o", linestyle="dashed")
plt.title("Waktu Tunggu Pelanggan")
plt.xlabel("Pelanggan ke-")
plt.ylabel("Waktu Tunggu (menit)")

# Grafik waktu kedatangan vs waktu selesai layanan
plt.subplot(2, 1, 2)
plt.plot(range(jumlah_pelanggan), waktu_kedatangan, label="Waktu Kedatangan", color="green", marker="o")
plt.plot(range(jumlah_pelanggan), waktu_selesai_layanan, label="Waktu Selesai Layanan", color="red", marker="o")
plt.title("Waktu Kedatangan vs Waktu Selesai Layanan")
plt.xlabel("Pelanggan ke-")
plt.ylabel("Waktu (menit)")
plt.legend()

plt.tight_layout()
plt.show()
