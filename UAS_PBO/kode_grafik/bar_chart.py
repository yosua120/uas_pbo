from matplotlib import pyplot as plt
from matplotlib import style

# Mengatur gaya plot
style.use('ggplot')

# Data untuk plot
bahasa_pemrograman = ["JavaScript","html/css","Python","SQL","TypeScript","Bash/Shells","Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82,52.83, 51.52, 45.32, 43.75 , 32.74,30.49, 29.16 , 20.21 , 19.03]

# Membuat plot
fig, ax = plt.subplots()

# Membuat diagram batang
ax.bar(bahasa_pemrograman, persentase_pengguna, align='center', color='skyblue')
  
# Menambahkan label dan judul
ax.set_title('Bahasa Pemrograman Populer (2023)')
ax.set_ylabel('Persentase Pengguna (%)')
ax.set_xlabel('Bahasa Pemrograman')

# Menambahkan label pada sumbu x
ax.set_xticks(bahasa_pemrograman)
ax.set_xticklabels(bahasa_pemrograman, rotation=45, ha='right')

# Menambahkan label pada setiap bar
for i, v in enumerate(persentase_pengguna):
    ax.text(i, v + 0.5, str(v), color='black', ha='center')

# Menampilkan plot
plt.tight_layout()  # Untuk memastikan label tidak tumpang tindih
plt.show()
