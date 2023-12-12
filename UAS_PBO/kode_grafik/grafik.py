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

# Membuat subplot untuk line chart
fig, ax_line = plt.subplots()

ax_line.plot(bahasa_pemrograman, persentase_pengguna, marker='o', linestyle='-', color='skyblue', label='Line Chart')
ax_line.set_title('Persentase Pengguna Bahasa Pemrograman Populer (2023)')
ax_line.set_ylabel('Persentase Pengguna (%)')
ax_line.set_xlabel('Bahasa Pemrograman')
ax_line.legend()

# Membuat subplot untuk pie chart
fig_pie, ax_pie = plt.subplots()

ax_pie.pie(persentase_pengguna, labels=bahasa_pemrograman, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax_pie.set_title('Pie Chart')

# Membuat subplot untuk bar chart
fig_bar, ax_bar = plt.subplots()

ax_bar.bar(bahasa_pemrograman, persentase_pengguna, color='skyblue', label='Bar Chart')
ax_bar.set_title('Bar Chart')
ax_bar.set_ylabel('Persentase Pengguna (%)')
ax_bar.set_xlabel('Bahasa Pemrograman')
ax_bar.legend()

# Membuat subplot untuk gelombang sinus
fig_sinus, ax_sinus = plt.subplots()

ax_sinus.plot(x_sinus, y_sinus, linestyle='--', color='orange', label='Gelombang Sinus')
ax_sinus.set_title('Contoh Gelombang Sinus')
ax_sinus.set_ylabel('Nilai Gelombang Sinus')
ax_sinus.set_xlabel('Waktu')
ax_sinus.legend()

# Menampilkan semua plot
plt.tight_layout()
plt.show()
