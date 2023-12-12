from matplotlib import pyplot as plt
from matplotlib import style

# Mengatur gaya plot
style.use('ggplot')

# Data untuk plot
bahasa_pemrograman = ["JavaScript","html/css","Python","SQL","TypeScript","Bash/Shells","Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82,52.83, 51.52, 45.32, 43.75 , 32.74,30.49, 29.16 , 20.21 , 19.03]

# Membuat plot
fig, ax = plt.subplots()

# Membuat diagram garis
ax.plot(bahasa_pemrograman, persentase_pengguna, marker='o', linestyle='-', color='skyblue', label='Persentase Pengguna')

# Menambahkan label dan judul
ax.set_title('Bahasa Pemrograman Populer (2023)')
ax.set_ylabel('Persentase Pengguna (%)')
ax.set_xlabel('Bahasa Pemrograman')

# Menambahkan label pada setiap titik data
for i, v in enumerate(persentase_pengguna):
    ax.text(i, v + 0.5, str(v), color='black', ha='center')

# Menambahkan legend
ax.legend()

# Menampilkan grid
ax.grid(True, linestyle='--', alpha=0.7)

# Menampilkan plot
plt.tight_layout()
plt.show()
