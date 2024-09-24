# TUGAS INDIVIDU 4
# 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
-> `HttpResponseRedirect()` dan `redirect()` adalah cara untuk mengarahkan pengguna dari satu halaman ke halaman lain. HttpResponseRedirect() adalah kelas yang digunakan untuk membuat respons redirect dengan status kode 302 dan membutuhkan URL lengkap sebagai argumen. Sebaliknya, redirect() adalah fungsi shortcut yang lebih sederhana dan fleksibel karena dapat menerima URL, view, atau model, dan secara otomatis mengonversinya menjadi URL yang tepat. redirect() sering digunakan karena lebih mudah dan praktis, terutama saat ingin mengarahkan pengguna ke view tertentu tanpa perlu memikirkan URL lengkapnya.

# 2. Jelaskan cara kerja penghubungan model Product dengan User!
-> Untuk menghubungkan model *Product* dengan *User* di Django, kita bisa menggunakan relasi ForeignKey yang memungkinkan setiap entri Products terhubung dengan satu User dari model bawaan Django. ForeignKey ini akan menyimpan referensi ke user yang terkait dengan setiap produk. Pada model Products, tambahkan field `user = models.ForeignKey(User, on_delete=models.CASCADE)` untuk mengaitkan product dengan user. 

Parameter `on_delete=models.CASCADE` memastikan bahwa jika pengguna dihapus, semua produk yang terhubung dengannya juga akan dihapus. Di dalam fungsi pembuatan produk, seperti `create_product`, diperlukan untuk mengusu field user dengan Objek User dari return value `request.user` (user yang sedang login) sebelum menyimpan produk ke database. 

Hal ini diperlukan untuk memastikan produk yang dibuat oleh user selalu terhubung. Ketika menampilkan produk, nantinya program akan memfilter product berdasarkan user yang sedang login, dengan `Product.objects.filter(user=request.user)`, sehingga hanya product milik user tersebut yang muncul. 

# 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
-> Authentication dan Authorization adalah dua hal penting dalam keamanan aplikasi yang mempunyai fungsi berbeda. Authentication adalah proses memverifikasi identitas user dan memastikan apakah user tersebut terdaftar di sistem. Authentication penting karena merupakan semacam crucial step dari user untuk dapat mengakses web page yang menerapkan authorization, apabila user tidak terdaftar maka user tidak akan dapat mengakses web page tersebut. Misalnya, pada halaman login SCELE, user diminta memasukkan username dan password yang selanjutnya akan diperiksa oleh sistem. Jika autentikasi berhasil, user baru akan dapat mengakses halaman SCELE, namun jika tidak, user akan diminta untuk menginput ulang kredensialnya.

Sementara itu, authorization adalah proses yang menentukan apa saja yang boleh diakses atau dilakukan oleh user yang sudah terautentikasi. Hal ini penting untuk pengelolaan user agar tidak ada user yang dapat mengakses/mengubah suatu hal yang seharusnya hanya dapat diakses oleh beberapa user saja. Sebagai contoh, authorization pada sistem SIAKNG, di mana dosen memiliki hak untuk melihat dan mengelola nilai mahasiswa dalam jumlah banyak, sedangkan mahasiswa hanya bisa melihat nilai mereka sendiri setelah dipublikasikan.

Dalam Django, autentikasi dilakukan dengan memeriksa kredensial pengguna menggunakan fungsi seperti `authenticate()` dan `login()`, sementara otorisasi diimplementasikan melalui permissions dan groups yang mengatur hak akses pengguna berdasarkan perannya, sehingga keduanya bekerja bersama untuk memastikan keamanan dan pengelolaan akses aplikasi.

# 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
-> Django mengingat user yang telah login dengan menggunakan mekanisme sessions, dimana setelah login, Django menyimpan informasi tentang user dalam sebuah session di server dan memberikan session ID kepada user. Session ID ini disimpan di browser user sebagai *cookie*, dan setiap kali user mengirim permintaan ke server, cookie tersebut dikirim kembali untuk memverifikasi identitas pengguna yang telah login. Selain itu, cookies juga memiliki berbagai kegunaan lain, seperti menyimoan preferensi pengguna, melacak aktivitas pengguna untuk keperluan analisis dan pemasan, dan lainnya. Namun, tidak semua cookies aman untuk digunakan.

Cookies yang tidak dienkripsi atau diberi atribute secure dapat dieksploitasi melalui serangan man-in-the-middle, sementara cookies yang tidak memiliki atribut HttpOnly bisa rentan terhadap serangan Cross-Site Scripting (XSS), di mana penyerang dapat mencuri data cookie. Selain itu, cookies juga rentan terhadap serangan Cross-Site Request Forgery (CSRF), di mana penyerang mencoba memanfaatkan session yang sudah ada untuk melakukan tindakan yang tidak sah. Django sendiri telah menerapkan perlindungan CSRF untuk menjaga keamanan ini.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    - Mengaktifkan virtual environment
    - Pada `views.py`, kita menambahkan code berikut untuk mengimplementasikan register, login, dan logout:
    ```
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    
    def register(request):
    form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    - `form = UserCreationForm(request.POST)` digunakan untuk membuat `UserCreationForm` baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada `request.POST.`
    - Fungsi `register` untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
    - `form.is_valid()` digunakan untuk memvalidasi isi input dari form tersebut.
    - `form.save()` digunakan untuk membuat dan menyimpan data dari form tersebut.
    - `return redirect('main:show_main')` digunakan untuk melakukan redirect setelah data form berhasil disimpan.
    - Lalu pada urls.py untuk handlo routing kite memerluka kode berikut ini:
    ```
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    ```
    - Kemudian, kita juga membuat template yang berjudul `register.html`, `main.html`, dan `login.html`.

- [] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal :`
    - Runserver dengan menjalankan `python manage.py runserver`
    - Buka localhost:8000 dan register untuk 2 username dengan username dan password yang berbeda.
    - Login kedua akun tersebut, kemudian buat 3 product baru dengan klik tombol Add New Product dan isi seluruh detail product yang kita inginkan. Setelah selesai, cek apakah product yang ditambahkan sudah terdapat pada tabel. Apabila sudah, maka setiap akun mempunyai isi product yang berbeda-beda. 
    - Bukti dummy data pada masing-masing akun:
        - Akun 1 :
        ![]https://github.com/indahcahyaaa/hoodie-yay/blob/main/Akun%201.png
        - Akun 2 :
        ![]https://github.com/indahcahyaaa/hoodie-yay/blob/main/Akun%202.png

- [] Menghubungkan model Product dengan User.
    - Pada `models.py`, kita tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` untuk menghubungkan satu Products class dengan satu user melalui sebuah  relationship, dimana sebuah Products pasti terasosiasikan dengan seorang user.
    - Kemudian pada fungsi `create_product` yang ada pada `views.py` kita ubah menjadi :
    ```
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
    - Di mana parameter commit=False berguna untuk mencegah Django untuk tidak menyimpan objek secara langsung yang telah dibuat dari form langsung ke database.
    - Selanjutnya, mengubah value `mood_entries` dan `context` untuk key 'name' pada fungsi `show_main` menjadi :
    ```
    def show_main(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
    ```
    - Terakhir, lakukan migrasi `makemigration` untuk menyimpan semua perubahan dan mengaplikasikan migrasi tersebut `(migrate)`. 

- [] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
    - Untuk menampilkan username dan class user dapat menggunakan, `<h5>Name: {{name}}</h5>`, `<h5>NPM: {{ npm }}</h5>` dan `<h5>Class: {{ class }}</h5>`
    - Untuk menampilkan data last login user, kita dapat memanfaatkan Cookies dengan menggunakan, `<p>Sesi terakhir login: {{ last_login }}</p>`
    - Kemudian, untuk implementasi cookies kita bisa menggunakan:
        - `response.set_cookie('last_login', str(datetime datetime.now()))` pada function login_user di views.py untuk set cookie kapan user login terakhir kali.
        - `response.delete_cookie('last_login')` pada function logout_user di views.py untuk menghapus cookie
        - `'last_login': request.COOKIES['last_login']`, pada context function show_main di views.py.

# TUGAS INDIVIDU 3
# 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
-> Dalam mengembangkan suatu platform ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Maka dari itu, kita memerlukan data delivery pada pengimplementasian sebuah platform untuk memastikan data dapat dikirim dengan cepat, aman, dan efisien antar komponen dalam sebuah platform. Tanpa mekanisme pengiriman data yang efektif, platform tidak dapat berfungsi secara optimal, yang bisa mengakibatkan masalah seperti keterlambatan dalam pengambilan data, kehilangan informasi, atau kegagalan komunikasi antar sistem. Data delivery yang baik juga menjaga konsistensi informasi, sehingga data yang diterima selalu up-to-date dan akurat. Hal ini penting agar platform berjalan dengan baik, menjaga konsistensi data, meningkatkan responsivitas, dan memungkinkan integrasi dengan sistem lain.

# 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
-> JSON dan XML adalah representasi data yang digunakan dalam pertukaran data antar platform. JSON digunakan sebagai format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai platform. XML menggunakan tanda untuk membedakan antara atribut data dan data aktual. Meskipun kedua format tersebut digunakan dalam pertukaran data, JSON adalah opsi yang lebih baru, lebih fleksibel,dan lebih populer.

JSON lebih populer dikarenakan kesederhanaan dan kemudahan dalam penggunaannya (key-value), sedangkan XML menggunakan struktur yang lebih kompleks dengan tag pembuka dan penutup yang memakan lebih banyak ruang dan lebih sulit dibaca. JSON sendiri memiliki beberapa keunggulan dibanding XML yaitu antara lain, ukurannya yang lebih kecil karena tidak menggunakan tag berlebih sehingga lebih efisien dalam penggunaannya. Kecepatan parsing JSON juga lebih tinggi dibanding XML karena JSON didukung langsung oleh JavaScript. Selain itu, JSON menjadi standar dalam RESTful API, sehingga lebih mudah diitegrasikan ke dalam aplikasi web. Beberapa hal ini lah yang membuat JSON lebih populer dibandingkan dengan XML.

# 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
-> Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dikirimkan ke form memenuhi semua validasi yang telah ditentukan atau tidak. Ketika form menerima input dari pengguna melalui metode POST, Django perlu memverifikasi data tersebut valid terlebih dahulu sebelum di executed lebih lanjut. Kita memerlukan method is_valid() karena untuk memastikan data yang dikirimkan aman, konsisten, dan sesuai sebelum disimpan atau proses, serta untuk memberikan feedback kepada pengguna jika ada kesalahan dalam pengisian form.

# 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
-> csrf_token diperlukan untuk melindungi aplikasi dari serangan CSRF, yaitu serangan dimana penyerang mengirimkan permintaan berbahaya. Jika kita tidak menambahkan csrf_token, aplikasi menjadi rentan, karena penyerang bisa memanfaatkan sesi user yang sudah login dan tanpa sengaja mengirim permintaan yang tidak diinginkan. Tanpa perlindungan CSRF, aplikasi tidak dapat membedakan apakah permintaan tersebut berasal dari pengguna yang sah atau dari penyerang. Dengan csrf_token, Django memastikan bahwa setiap permintaan berasal dari sumber yang sah dan mencegah penyerang dari membuat permintaan palsu atas nama pengguna.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-> Membuat input form untuk menambahkan objek model pada app sebelumnya : 
Kita memerlukan base template (base.html). Template ini berfungsi sebagai kerangka utama untuk halaman web yang bisa diisi dengan konten seperti form atau daftar produk dengan menggunakan {% something %} sebagai _placeholder._ Kemudian kita membuat forms.py untuk mendefinisikan file form yang terhubung dengan model yang ingin kita tambahkan datanya (Products), dan juga fields sebagai tanda bahwa object Product memilki 4 atribut yang dapat diisi melalui form. Setelah itu, kita mengubah show_main pada views.py dengan menambahkan fungsi Products.objects.all() yang digunakan untuk mengambil seluruh objek Products yang tersimpan pada _database._ Lalu tambahkan path URL ke dalam variabel urlpatterns pada urls.py di main untuk mengakses fungsi yang sudah di-import. 

-> Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID :
- show_xml, digunakan untuk menampilkan semua data produk yang ada dalam format XML. Ketika mengakses URL (xml), data dari model Products akan diambil, dokonversi menjadi format XML, lalu dikirim sebagai respons.
- show_json, sama halnya denga show_xml, fungsi ini digunakan untuk menampilkan semua produk dalam format JSON. 
- show_xml_by_id, fungsi ini digunakan untuk menampilkan satu produk tertentu berdasarkan ID-nya dalam format XML. Fungsi ini akan mencari produk dengan ID yang diminta, lalu menampilkannya dalam format XML.
- show_json_by_id, sama halnya dengan show_xml_by_id, fungsi ini akan mengambil produk dengan ID yang diminta dan menampilkan data tersebut dalam format JSON.

-> Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2 :
Pada urls.py, kita isi variable urlpatterns dengan path URL, yang akan digunakan agar function yang telah dicantumkan pada views.py dpaat diakses dengan url yang diinginkan. 

-> Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman :
Format XML :
![](https://github.com/indahcahyaaa/hoodie-yay/blob/main/Format%20xml.png)

Format JSON:
![](https://github.com/indahcahyaaa/hoodie-yay/blob/main/Format%20json.png)

Format XML dengan ID :
![](https://github.com/indahcahyaaa/hoodie-yay/blob/main/Format%20xml%20dengan%20id.png)

Format JSON dengan ID :
![](https://github.com/indahcahyaaa/hoodie-yay/blob/main/Formal%20json%20dengan%20id.png)

# TUGAS INDIVIDU 2
# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/indahcahyaaa/hoodie-yay/blob/main/No2BaganPBP.JPG)

Client's device mengirimkan request ke Internet -> diteruskan ke Python/Django -> diarahkan ke urls.py -> diteruskan ke views.py untuk memproses URL -> mengambil/menulis data dari/ke models.py dan database -> memasukkan/menampilkan data dari/ke template -> mengembalikan file HTML yang sudah digabung dengan nilai-nilai yang diinginkan -> mengirimkan kembali ke Internet -> ditampilkan di perangkat client.

# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Git digunakan untuk kolaborasi dnegan banyak individu memungkinkan bekerja pada proyek yang sama secara efisien 
- Proyek open source, git merupakan tools yang bersifat open souce, jadi bisa dipakai untuk membuat software secara open source.
- Dapat melacak perubahan / version control, karena git mencatat setiap perubahan yang dilakukan pada source code. 
- Branching, memungkinkan developer untuk membuat branch terpisah dari basis code utama
- Merging, setelah pengembangan di branch selesai dan di uji, branch dapat di merge / gabungkan kembali ke branch utama. 

# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django memiliki arsitektur MTV (Model-Template-View) yang terstruktur dengan baik, sehingga memudahkan pemahaman tentang bagaimana siklus data dalam aplikasi web.
- Django memiliki ORM bawaan yang memudahkan interaksi dengan database tanpa harus menulis SQL secara langsung. Sehingga mengurangi kompleksitas bagi pemula.
- Dengan Django, developer dapat terhindar dari berbagai kesalahan keamanan yang lazim terjadi ketika proses coding.
- Django menerapkan prinsip DRY atau Don’t Repeat Yourself. Artinya, Anda cukup menulis satu atau beberapa baris kode untuk membuat sebuah perintah. Lalu, perintah tersebut bisa diterapkan di bagian website yang lain.

# 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan teknik ORM untuk memetakan class model di Python menjadi tabel dalam database. 