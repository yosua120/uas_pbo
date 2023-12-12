from matplotlib import pyplot as plt
from matplotlib import style

# Mengatur gaya plot
style.use('ggplot')

# Data untuk plot
bahasa_pemrograman = ["JavaScript", "HTML/CSS", "Python", "SQL", "TypeScript", "Bash/Shells", "Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82, 52.83, 51.52, 45.32, 43.75, 32.74, 30.49, 29.16, 20.21, 19.03]

# Membuat pie chart
fig_pie, ax_pie = plt.subplots()

ax_pie.pie(persentase_pengguna, labels=bahasa_pemrograman, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax_pie.set_title('Persentase Pengguna Bahasa Pemrograman Populer (2023)')

# Menampilkan plot
plt.tight_layout()
plt.show()
