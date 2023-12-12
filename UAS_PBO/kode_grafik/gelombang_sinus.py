import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

# Mengatur gaya plot
style.use('ggplot')

# Data untuk plot
bahasa_pemrograman = ["JavaScript", "HTML/CSS", "Python", "SQL", "TypeScript", "Bash/Shells", "Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82, 52.83, 51.52, 45.32, 43.75, 32.74, 30.49, 29.16, 20.21, 19.03]

# Membuat data untuk contoh gelombang sinus
x_sinus = np.linspace(0, 5, 100)  # 100 titik antara 0 dan 5
y_sinus = np.sin(x_sinus) * 5 + 25  # Gelombang sinus dengan amplitudo 5 dan fase 25

# Membuat plot
fig, ax = plt.subplots()

# Membuat diagram garis untuk persentase pengguna
ax.plot(bahasa_pemrograman, persentase_pengguna, marker='o', linestyle='-', color='skyblue', label='Persentase Pengguna')

# Membuat plot gelombang sinus
ax.plot(x_sinus, y_sinus, linestyle='--', color='orange', label='Gelombang Sinus')

# Menambahkan label dan judul
ax.set_title('Bahasa Pemrograman Populer (2023) dan Gelombang Sinus')
ax.set_ylabel('Persentase Pengguna (%) / Nilai Gelombang Sinus')
ax.set_xlabel('Bahasa Pemrograman')

# Menambahkan label pada setiap titik data persentase pengguna
for i, v in enumerate(persentase_pengguna):
    ax.text(i, v + 0.5, str(v), color='black', ha='center')

# Menambahkan legend
ax.legend()

# Menampilkan grid
ax.grid(True, linestyle='--', alpha=0.7)

# Menampilkan plot
plt.tight_layout()
plt.show()
