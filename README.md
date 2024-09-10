1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-> Membuat sebuah proyek Django baru:
Pertama-tama saya membuat direktori baru dengan nama hoodie-yay, kemudian saya melakukan git init untuk menginisialisasi repositori baru. Selanjutnya, saya melakukan configuration account github saya dengan git config --global user.name dan user.emai. Setelah itu, saya melakukan verifikasi konfigurasi dengan menjalankan perintah git config --list. Lalu, saya menghubungkan repositori lokal saya dengan repositori github dengan membuat branch utama baru dan menjalankan git remote add origin <URL_REPO_SAYA> untuk menghubungkan repositori di github, kemudian saya melakukan pengecekan dengan membuat sebuah file README.md, lalu melakukan penyimpanan ke github dengan melakukan git add, commit dan push. 

Selanjutnya, saya melakukan aktivasi virtuan environment dan menyiapkan dependencies dengan membuat requirement.txt yang berisi beberapa dependencies, kemudian saya melakukan instalasi terhadap dependencies, baru lah saya membuat proyek Django baru bernama hoodie_yay. Setelah itu, saya melakukan konfigurasi proyek dan menjalankan server. Lalu saya mengunggah proyek ke repositori github, sebelum itu saya menambahkan berkas .gitignore terlebih dahulu untuk menentukan berkas-berkas dan direktori apa saja yang harus diabaikan oleh Git. Baru lah setelah itu, saya melakukan add, commit, dan push kembali ke github.

-> Membuat aplikasi dengan nama main pada proyek : 
Didalam terminal yang sama, saya menjalankan perintah python manage.py startapp main untuk membuat aplikasi dengan nama main. Lalu, saya mendaftarkan aplikasi main ke dalam proyek dengan membuka file settings.py pada direktori hoodie-yay dan menambahkan main ke variabel INSTALLED_APPS. Setelah itu, saya membuat direktori baru bernama templates pada direktori main untuk menyimpan file .html, karena django menggunakan MVT. 

-> Melakukan routing pada proyek agar dapat menjalankan aplikasi main: 
Pertama-tama membuka file urls.py pada direktori hoodie-yay, kemudian saya menambahkan django.urls import path, include. Setelah itu menambahkan rute URL untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.

-> Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
- name sebagai nama item dengan tipe CharField.
- price sebagai harga item dengan tipe IntegerField.
- description sebagai deskripsi item dengan tipe TextField
Saya membuka models.py dan mengisinya dengan attributes yang diperlukan, yang sudah saya sebutkan diatas. 

-> Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu :
Membuka views.py yang ada di main, lalu saya check apakah from django.shortcuts import render sudah ada atau belum. Jika sudah ada, kemudian saya menambahkan fungsi show_main di bawah import.

-> Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py :
Buat berkas urls.py di dalam direktori main, lalu isi urls.py dengan kode :

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]

-> Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet : 
Akses halaman PWS, kemudian mengisi data diri sesuai required, lalu create new project sesuai dengan nama yang kita inginkan. Setelah itu, tambahkan URL deployment PWS kita pada ALLOWED_HOSTS yang ada pada settings.py. 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/indahcahyaaa/hoodie-yay/blob/main/No2BaganPBP.JPG)

Client's device mengirimkan request ke Internet -> diteruskan ke Python/Django -> diarahkan ke urls.py -> diteruskan ke views.py untuk memproses URL -> mengambil/menulis data dari/ke models.py dan database -> memasukkan/menampilkan data dari/ke template -> mengembalikan file HTML yang sudah digabung dengan nilai-nilai yang diinginkan -> mengirimkan kembali ke Internet -> ditampilkan di perangkat client.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Git digunakan untuk kolaborasi dnegan banyak individu memungkinkan bekerja pada proyek yang sama secara efisien 
- Proyek open source, git merupakan tools yang bersifat open souce, jadi bisa dipakai untuk membuat software secara open source.
- Dapat melacak perubahan / version control, karena git mencatat setiap perubahan yang dilakukan pada source code. 
- Branching, memungkinkan developer untuk membuat branch terpisah dari basis code utama
- Merging, setelah pengembangan di branch selesai dan di uji, branch dapat di merge / gabungkan kembali ke branch utama. 

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django memiliki arsitektur MTV (Model-Template-View) yang terstruktur dengan baik, sehingga memudahkan pemahaman tentang bagaimana siklus data dalam aplikasi web.
- Django memiliki ORM bawaan yang memudahkan interaksi dengan database tanpa harus menulis SQL secara langsung. Sehingga mengurangi kompleksitas bagi pemula.
- Dengan Django, developer dapat terhindar dari berbagai kesalahan keamanan yang lazim terjadi ketika proses coding.
- Django menerapkan prinsip DRY atau Don’t Repeat Yourself. Artinya, Anda cukup menulis satu atau beberapa baris kode untuk membuat sebuah perintah. Lalu, perintah tersebut bisa diterapkan di bagian website yang lain.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan teknik ORM untuk memetakan class model di Python menjadi tabel dalam database. 