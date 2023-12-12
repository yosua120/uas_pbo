# Penggunaan grafik dengan Python: Cara terbaik python adalah visualisasi.

## LINE CHART (GRAFIK GARIS)
Line chart paling tepat digunakan untuk menunjukkan tren dari waktu ke waktu. Sumbu X biasanya mewakili periode waktu, sumbu Y menggambarkan nilai/kuantitas. Contohnya jumlah penjualan/ penggunaan dari pekan ke pekan selama satu tahun.Grafik ini dapat memuat banyak titik data yang dapat diatur saling berdekatan sesuai kerapatan periode waktu. Karena visualnya yang simpel, bisa menggunakan banyak garis sekaligus dalam satu tampilan. Ini memudahkan penggambaran data tren dari beragam kategori.

```
from Matplotlib import pyplot as plt
from Matplotlib import style
# Mengatur gaya plot
style.use('ggplot')
# Data untuk plot
bahasa_pemrograman = 
["JavaScript","html/css","Python","SQL","TypeScript","Bash/Shells","Java", "C#", "C++", 
"PHP"]
persentase_pengguna = [65.82,52.83, 51.52, 45.32, 43.75 , 32.74,30.49, 29.16 , 20.21 , 19.03]
# Membuat plot
fig, ax = plt.subplots()
# Membuat diagram garis
ax.plot(bahasa_pemrograman, persentase_pengguna, marker='o', linestyle='-', color='skyblue', 
label='Persentase Pengguna')
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
7
# Menampilkan plot
plt.tight_layout()
plt.show()
```

#### PENJELASAN 
Source Code diatas adalah sebuah script dalam bahasa Python yang menggunakan pustaka Matplotlib untuk membuat diagram garis (line chart) yang menggambarkan persentase pengguna berbagai bahasa pemrograman yang sedang popular pada tahun 2023. Fungsi tight_layout() digunakan agar elemen-elemen plot tidak tumpang tindih. Fungsi show() menampilkan plot secara keseluruhan.

## BAR CHART (GRAFIK BATANG)
Bar Chart paling cocok untuk komparasi data dengan banyak kategori atau rangkaian data (data series). Untuk kemudahan membaca data, dapat mengurutkan kategori berdasarkan besar nilainya, misal dari nilai tertinggi hingga terendah. Lain halnya dengan data series, di mana data didistribusikan berdasarkan kategori berjenjang, misalnya populasi penduduk berdasarkan rentang usia atau tingkat pendidikan dan penggunaan bahasa pemograman.

```
from Matplotlib import pyplot as plt
from Matplotlib import style
# Mengatur gaya plot
9
style.use('ggplot')
# Data untuk plot
bahasa_pemrograman = 
["JavaScript","html/css","Python","SQL","TypeScript","Bash/Shells","Java", "C#", "C++", 
"PHP"]
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
plt.tight_layout() # Untuk memastikan label tidak tumpang tindih
plt.show()
```

#### PENJELASAN
Source Code diatas adalah sebuah script dalam bahasa Python yang menggunakan pustaka Matplotlib untuk membuat diagram batang (Bar Chart) yang menggambarkan persentase pengguna berbagai bahasa pemrograman pada tahun 2023. Kode ini kurang lebih sama dengan kode sebelumnya dimana Kode ini mengimpor dua modul dari pustaka Matplotlib, yaitu pyplot untuk membuat plot dan style untuk mengatur gaya plot dan  10 mengatur gaya plot menggunakan gaya ggplot dari Matplotlib. 

## PIE CHART (GRAFIK/DIAGRAM LINGKARAN)
Pie Chart digunakan untuk menggambarkan komposisi antarbagian pada suatu kesatuan utuh. Bagian ini biasanya direpresentasikan dalam satuan persen sehingga jika seluruh bagian dijumlahkan, hasilnya sama dengan seratus persen. Jenis grafik ini akan mudah dipahami jika kategori yang ditampilkan tidak banyak, misal 5 bagian. Semakin banyak bagiannya, apalagi jika proposinya sangat kecil, akan kian sulit membacanya

```
from Matplotlib import pyplot as plt
from Matplotlib import style
# Mengatur gaya plot
style.use('ggplot')
# Data untuk plot
bahasa_pemrograman = ["JavaScript", "HTML/CSS", "Python", "SQL", "TypeScript", 
"Bash/Shells", "Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82, 52.83, 51.52, 45.32, 43.75, 32.74, 30.49, 29.16, 20.21, 19.03]
# Membuat pie chart
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(persentase_pengguna, labels=bahasa_pemrograman, autopct='%1.1f%%', 
startangle=90, colors=plt.cm.Paired.colors)
ax_pie.set_title('Persentase Pengguna Bahasa Pemrograman Populer (2023)')
# Menampilkan plot
plt.tight_layout()
plt.show()
```

#### PENJELASAN
Source Code diatas adalah script dalam bahasa Python yang menggunakan pustaka Matplotlib untuk membuat diagram lingkaran (pie chart) yang menggambarkan persentase pengguna berbagai bahasa pemrograman pada tahun 2023.Kodenya pun kurang lebih sama dengan kode sebelumnya seperti Kode ini mengimpor dua modul dari pustaka Matplotlib, yaitu pyplot untuk membuat plot dan style untuk mengatur gaya plot dan Mengatur gaya plot menggunakan gaya 'ggplot' dari Matplotlib. Kemudian Menyediakan data yang akan digunakan untuk membuat plot.

## GELOMBANG SINUS
Gelombang sinusoidal adalah salah satu dari bentuk gelombang yang penting di Teknik Elektro. Gelombang sinus sangat penting dalam bidang fisika karena gelombang ini 13 mempertahankan bentuknya ketika ditambahkan kepada gelombang sinus berfrekuensi sama yang lain walaupun fasenya berbeda. Gelombang ini merupakan satu-satunya fungsi periodik yang memiliki sifat ini, menjadikan gelombang ini bagian penting dalam Analisis Fourier.

```
import numpy as np
import Matplotlib.pyplot as plt
import Matplotlib.style as style
# Mengatur gaya plot
style.use('ggplot')
# Data untuk plot
bahasa_pemrograman = ["JavaScript", "HTML/CSS", "Python", "SQL", "TypeScript", 
"Bash/Shells", "Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82, 52.83, 51.52, 45.32, 43.75, 32.74, 30.49, 29.16, 20.21, 19.03]
14
# Membuat data untuk contoh gelombang sinus
x_sinus = np.linspace(0, 5, 100) # 100 titik antara 0 dan 5
y_sinus = np.sin(x_sinus) * 5 + 25 # Gelombang sinus dengan amplitudo 5 dan fase 25
# Membuat plot
fig, ax = plt.subplots()
# Membuat diagram garis untuk persentase pengguna
ax.plot(bahasa_pemrograman, persentase_pengguna, marker='o', linestyle='-', color='skyblue', 
label='Persentase Pengguna')
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
```

#### PENJELASAN
Source Code diatas adalah membuat plot gabungan yang menggambarkan persentase pengguna bahasa pemrograman pada tahun 2023 dan contoh 15 gelombang sinus. Kode ini mengimpor modul NumPy untuk manipulasi array, dan modul Matplotlib untuk membuat plot dan mengatur gaya plot menggunakan gaya 'ggplot' dari Matplotlib.

## GRAFIK (SEMUA GRAFIK DIDALAM SATU KODE)

```
import numpy as np
import Matplotlib.pyplot as plt
import Matplotlib.style as style
# Mengatur gaya plot
style.use('ggplot')
# Data untuk plot
bahasa_pemrograman = ["JavaScript", "HTML/CSS", "Python", "SQL", "TypeScript", 
"Bash/Shells", "Java", "C#", "C++", "PHP"]
persentase_pengguna = [65.82, 52.83, 51.52, 45.32, 43.75, 32.74, 30.49, 29.16, 20.21, 19.03]
# Membuat data untuk contoh gelombang sinus
x_sinus = np.linspace(0, 5, 100) # 100 titik antara 0 dan 5
y_sinus = np.sin(x_sinus) * 5 + 25 # Gelombang sinus dengan amplitudo 5 dan fase 25
17
# Membuat subplot untuk line chart
fig, ax_line = plt.subplots()
ax_line.plot(bahasa_pemrograman, persentase_pengguna, marker='o', linestyle='-', 
color='skyblue', label='Line Chart')
ax_line.set_title('Persentase Pengguna Bahasa Pemrograman Populer (2023)')
ax_line.set_ylabel('Persentase Pengguna (%)')
ax_line.set_xlabel('Bahasa Pemrograman')
ax_line.legend()
# Membuat subplot untuk pie chart
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(persentase_pengguna, labels=bahasa_pemrograman, autopct='%1.1f%%', 
startangle=90, colors=plt.cm.Paired.colors)
ax_pie.set_title('Pie Chart')
# Membuat subplot untuk Bar Chart
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
```

#### PENJELASAN
Source Code diatas adalah membuat empat subplot yang menampilkan berbagai jenis plot berbeda, termasuk line chart, pie chart, Bar Chart, dan plot gelombang sinus. Kode ini mengimpor modul NumPy untuk manipulasi array, dan modul Matplotlib untuk membuat plot dan mengatur gaya plot menggunakan gaya 'ggplot' dari Matplotlib juga menyediakan data yang akan digunakan untuk membuat plot persentase pengguna bahasa pemrograman. Selanjutnya kits dapat membuat data untuk contoh gelombang sinus dengan menggunakan NumPy dan Membuat subplot untuk Line chart yang menampilkan persentase pengguna bahasa pemrograman. Dan selanjutnya kita dapat membuat subplot untuk Pie Chart yang menampilkan persentase pengguna bahasa pemrograman dan kemudian membuat subplot untuk Bar Chart yang menampilkan persentase pengguna bahasa pemrograman dan membuat subplot untuk plot gelombang sinus. Dan selanjutnya yang terakhir Menampilkan semua subplot secara bersamaan. Fungsi tight_layout() digunakan agar elemen-elemen plot tidak tumpang tindih. Fungsi show() menampilkan plot secara keseluruhan.



# KESIMPULAN 
Dengan menggunakan Python kita dapat membuat grafik apapun dengan mudah, dan untuk membuatnya Library/pustaka Python, dalam membuat penggunaan grafik pada Python, dalam membuat grafik ada beberapa ada tahapan Library yang dapat digunakan misalnya Matplotlib, Visualisasi Panda, Seaborn, ggplot dan Plotly dll. Disini kami menggunakan Matplotlib untuk penggunaakn pustakanya. Dan menambahkan kode kode perintah seperti diatas pada pembahasan.

# SARAN
Pada pembuatan tugas ini kami menyarankan sebelum menggunakan kode pada pyhton dalam oop sangat harus memahaminya terlebih dahulu karena jika tidak paham ap aitu pyhton dalam oop maka pada saat proses pembuatan akan terjadi error atau tidak bisa di jalankan.
