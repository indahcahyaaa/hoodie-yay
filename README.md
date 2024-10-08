# TUGAS INDIVIDU 6
# 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- *Interaksi di Halaman Web*, JavaScript memungkinkan interaksi _interface_ user yang dinamis dan responsif. Dengan JavaScript, developer dapat merespon tindakan user, seperti mengklik tombol, mengisi formulir, menggerakkan mouse, dll. Selain itu, JavaScript juga dapat memvalidasi input user, mengubah tampilan halaman, menampilkan pesan peringatan, atau tindakan lainnya berdasarkan interaksi user.

- *Pemanggilan HTTP (AJAX)*, JavaScript memungkinkan pemanggilan asikron ke server menggunakan AJAX _(Asynchronous JavaScript and XML)._ Dengan AJAX, kita dapat mengambil dan mengirim data ke server tanpa harus memuat ulang seluruh halaman. Hal ini memungkinkan pengembangan aplikasi web yang responsif dan dapat memperbarui konten secara dinamis.

- *Manipulasi dan pengendalian DOM*, JavaScript memungkinkan manipulasi elemen HTML dan struktur halaman menggunakan DOM (_Document Object Model_). Dengan DOM, kita dapat menambahkan, menghapus, atau memodifikasi elemen HTML, mengubah atribut, mengganti isi teks, atau mengubah tata letak halaman. Sehingga, perubahan pada elemen HTML lebih dinamis berdasarkan kondisi atau interaksi user.

- *Integrasi dengan API*, JavaScript memungkinkan integrasi dengan berbagai API (_Application Programming Interface_) untuk mengakses dan memanfaatkan data dan layanan dari pihak ketiga. Contohnya, mengambil data dari API Twitter untuk menampilkan tweet terbaru, menggunakan API Google Maps untuk menampilkan peta interaktif, atau memanfaatkan Open Finance API untuk untuk mengintegrasikan metode pembayaran yang aman dan efisien ke dalam website. 

# 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Keyword *await*, berfungsi untuk memberi tahu JavaScript untuk menunggu tindakan asinkron selesai sebelum melanjutkan fungsi. Penggunaan `await` saat melakukan `fetch()` berfungsi untuk menunggu hasil dari operasi asynchronous, sehingga code akan berhenti sejenak hingga permintaan HTTP selesai dan respons diterima. `fetch()` mengembalikan sebuah Promise, `await` memungkinkan kita menunggu penyelesaian Promise tersebut, sehingga kita dapat langsung menangani hasilnya, seperti parsing data menjadi JSON. 

Jika kita tidak menggunakan `await`, eksekusi kode akan terus berjalan tanpa menunggu hasil dari `fetch()`, hal ini menyebabkan variabel yang seharusnya menyimpan hasil permintaan hanya berisi `Promise` yang belum diselesaikan.

# 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator `csrf_exempt` digunakan untuk menonaktifkan perlindungan CSRF pada view tertentu, sehingga Django tidak memeriksa `csrf_token` pada request POST. Secara default, Django memeriksa token CSRF pada setiap request POST untuk melindungi dari serangan CSRF (Cross-Site Request Forgery). Jika token ini tidak ada, Django akan memblokir request tersebut dan menghasilkan error 403. Oleh karena itu, jika kita tidak ingin Django memeriksa token CSRF pada request AJAX tertentu, kita bisa menggunakan `csrf_exempt`.

# 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Melakukan pembersihan data input pengguna di backend, seperti menggunakan `strip_tags`, sangat penting meskipun sudah terdapat validasi di frontend. Hal ini karena validasi frontend dapat dilewati atau dimodifikasi oleh user yang tidak bertanggung jawab. Seperti contohnya, dengan mematikan JavaScript atau memodifikasi permintaan yang dikirimkan ke server. Maka dari itu, dengan melakukan pembersihan di backend, kita dapat memastikan bahwa data yang masuk ke sistem aman dari serangan seperti cross-site scripting (XSS).

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- [ ] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
    - [ ] AJAX GET
        1. Ubahlah kode cards data product agar dapat mendukung AJAX GET.
            - Pada `views.py`, kita tambahkan kedua import ini:
            `from django.views.decorators.csrf import csrf_exempt`
            `from django.views.decorators.http import require_POST`
            - Kemudian pada `views.py`, kita menghapus kode bagian berikut pada fungsi `show_main` untuk nantinya mendapatkan objek product dari endpoint/json
            `products = Product.objects.filter(user=request.user)` dan `'products': products,`
            - Masih pada di file yang sama, `views.py`, ubah baris pertama _views_ untuk `show_json` dan `show_xml`, dengan: 
            ```
            data = Products.objects.filter(user=request.user)
            ```
            - Selanjutnya, pada `main.html`, kita hapus bagian block conditional `product_entries` untuk menampilkan card product ketika kosong atau tidak. Setelah itu, kita tambahkan code berikut, `<div id="products_cards"></div>`

        2. Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
            - Menambahkan code berikut pada `main.html`:
                ```
                async function getProducts() {
                    return fetch("{% url 'main:show_json' %}").then((res) => res.json())
                }
                ```

    - [ ] AJAX POST
        - [ ] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.
            - Menambahkan code berikut pada `main.html`:
                ```
                <div class="px-3 mb-4">
                    <div class="flex justify-start mb-6 space-x-4">
                        <a href="{% url 'main:create_products_entry' %}" class="bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                        Add New Product
                        </a>
                        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-pink-400 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
                        Add New Product by AJAX
                        </button>
                    </div>
                </div>
                <div id="products_cards">
                </div>
                    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
                        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
                            <!-- Modal header -->
                            <div class="flex items-center justify-between p-4 border-b rounded-t">
                                <h3 class="text-xl font-semibold text-gray-900">
                                    Add New Product
                                </h3>
                                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                                    </svg>
                                    <span class="sr-only">Close modal</span>
                                </button>
                            </div>
                    
                            <!-- Modal body -->
                            <div class="px-6 py-4 space-y-6 form-style">
                                <form id="ProductsForm">
                                    <!-- Product Name -->
                                    <div class="mb-4">
                                        <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
                                        <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product name" required>
                                    </div>

                                    <!-- Price -->
                                    <div class="mb-4">
                                        <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                                        <input type="text" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product price" required>
                                    </div>

                                    <!-- Description -->
                                    <div class="mb-4">
                                        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                                        <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Describe product" required></textarea>
                                    </div>

                                    <!-- Stock -->
                                    <div class="mb-4">
                                        <label for="stock" class="block text-sm font-medium text-gray-700">Stock</label>
                                        <input type="number" id="stock" name="stock" min="1" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product stock" required>
                                    </div>

                                    <!-- Image -->
                                    <div class="mb-4">
                                        <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
                                        <input type="text" id="image" name="image" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-pink-700" placeholder="Enter product image" required>
                                    </div>
                                </form>
                            </div>

                            <!-- Modal footer -->
                            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-blur-200 rounded-b justify-center md:justify-end">
                                <button type="button" class="bg-blue-400 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                                <button type="submit" id="submitProducts" form="ProductsForm" class="bg-pink-400 hover:bg-pink-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
                            </div>
                        </div>
                    </div>
                </div>
                ```
        - [ ] Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
            - Menambahkan code berikut pada `views.py`:
                ```
                @csrf_exempt
                @require_POST
                def add_products_ajax(request):
                    name = strip_tags(request.POST.get("name"))
                    price = request.POST.get("price")
                    description = strip_tags(request.POST.get("description"))
                    stock = strip_tags(request.POST.get("stock"))
                    user = request.user
                    image = strip_tags(request.POST.get("image"))

                    new_product = Products(
                        name=name, price=price, description=description, stock=stock, user=user, image=image
                    )
                    new_product.save()

                    return HttpResponse(b"CREATED", status=201)
                ``` 
        - [ ] Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
            - Pada `urls.py`, tambahkan URL untuk view yang telah dibuat:
                    ```
                    urlpatterns = [
                        ...
                        path('add-products-ajax', add_products_ajax, name='add_products_ajax'),
                    ]
                    ```
        - [ ] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
            - Pada `main.html`, tambahkan code berikut ke section script: 
                ```
                function addProducts() {
                    fetch("{% url 'main:add_products_ajax' %}", {
                    method: "POST",
                    body: new FormData(document.querySelector('#ProductsForm')),
                    })
                    .then(response => refreshProducts())

                    document.getElementById("ProductsForm").reset(); 
                    document.querySelector("[data-modal-toggle='crudModal']").click();

                    return false;
                }
                document.getElementById("ProductsForm").addEventListener("submit", (e) => {
                    e.preventDefault();
                    addProducts();
                })
                ```
        - [ ] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
            - Tambahkan function `refreshProducts()`, pada `main.htlm`:
                ```
                ...
                async function refreshProducts(){
                    document.getElementById("products_cards").innerHTML = "";
                    document.getElementById("products_cards").className = "";
                    const products = await getProducts();
                    let htmlString = "";
                    let classNameString = "";

                    if (products.length === 0) {
                        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
                        htmlString = `
                            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                                <img src="{% static 'image/product-empty.png' %}" alt="Empty products" class="w-32 h-32 mb-4"/>
                                <p class="text-center text-gray-600 mt-4">Belum ada products yang ditambahkan pada Hoodie-Yay!</p>
                            </div>
                        `;
                    }
                    else {
                        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
                        products.forEach((item) => {
                            const name = DOMPurify.sanitize(item.fields.name);
                            const price = DOMPurify.sanitize(item.fields.price);
                            const description = DOMPurify.sanitize(item.fields.description);
                            const stock = DOMPurify.sanitize(item.fields.stock);
                            const image = DOMPurify.sanitize(item.fields.image);
                            htmlString += `
                            <div class="relative break-inside-avoid">
                            <div class="relative bg-white shadow-md border border-blue-500 rounded-lg mb-6 break-inside-avoid flex flex-col p-4">
                                <div class="mb-4">
                                <img src="${image}" alt="${name}" class="rounded-lg w-full">
                                </div>
                                <div class="mb-4">
                                <h3 class="font-bold text-xl text-gray-800 mb-2">${name}</h3>
                                <p class="text-gray-500 text-md">Rp ${price}</p>
                                <p class="mt-4 text-gray-700 leading-snug">${description}</p>
                                </div>
                                <hr class="border-t border-gray-300 my-4">
                                <div>
                                <p class="font-semibold text-lg text-gray-700 mb-1">Stock</p>
                                <p class="text-gray-600">${stock}</p>
                                </div>
                                <hr class="border-t border-gray-300 my-4">
                                <div class="mt-auto flex justify-center space-x-2">
                                    <a href="/edit-product/${item.pk}" class="bg-yellow-400 hover:bg-yellow-500 text-white text-sm font-bold px-3 py-2 rounded-md transition duration-300">
                                    Edit
                                    </a>
                                    <a href="/delete/${item.pk}" class="bg-red-400 hover:bg-red-500 text-white text-sm font-bold px-3 py-2 rounded-md transition duration-300">
                                    Delete
                                    </a>
                                </div>
                            </div>
                            </div>
                            `;
                        });
                    }
                    document.getElementById("products_cards").className = classNameString;
                    document.getElementById("products_cards").innerHTML = htmlString;
                }
                refreshProducts();
                ```

# TUGAS INDIVIDU 5
# 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, maka urutan prioritas pengambilan CSS selector *(rendah -> tinggi)* tersebut:
1. Element selector, memilih berdasarkan jenis elemen HTML, misalnya `p, div, h1.` Selector ini memiliki prioritas paling rendah.
2. Class selector, menargetkan elemen berdasarkan atribut class. Diawali dengan tanda titik. `.highlight{}`
3. Attribute selector, memilih elemen berdasarkan atribut yang dimiliki, seperti `[type="text"]`.
4. ID selector, ID selector menargetkan elemen berdasarkan atribut ID-nya. Untuk menandai elemen dengan ID selector, kita perlu menggunakan tanda pagar `#`
5. Inline selector, style yang diterapkan langsung pada elemen HTML melalui atribut style memiliki spesifisitas yang sangat tinggi dan akan mengesampingkan semua selector CSS yang ada di stylesheet. Contoh: `<p style="color: orange;">Ini teks berwarna oranye</p>`

# 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive web design merupakan desain situs web yang dapat beradaptasi dan merespon perubahan lebar layar sesuai dengan perangkat atau browser yang digunakan oleh users. Responsive web design merupakan desain situs web yang dapat beradaptasi dan merespon perubahan lebar layar sesuai dengan perangkat atau browser yang digunakan oleh users. 

Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena dapat memberi banyak keuntungan antara lain:
- Dapat diakses oleh berbagai device dengan ukuran layar berbeda-beda. Sehingga dapat diakses melalui perangkat yang berbeda (smartphone, tablet, maupun deskop).
- Meningkatkan user experience, yang dimana user akan mendapatkan web yang memiliki tampilan yang lebih rapi dan mudah dioperasikan.
- Biaya maintenance yang lebih rendah 

Contoh aplikasi yang sudah dan belum menerapkan responsive design:
- Aplikasi yang sudah menerapkan Responsive Design :
    - *Twitter*, tampilan yang responsif, baik di desktop, tablet, maupun smartphone. Tampilan seperti timeline dapat beradaptasi dengan ukuran layar.
    - *Google*, situs dan aplikasi Google dirancang untuk beradaptasi dengan berbagai ukuran layar, baik itu desktop, tablet, maupun ponsel. Elemen seperti berbagai fitur interaktifl ditata ulang agar mudah digunakan pada berbagai ukuran layar.
    - *YouTube*, menerapkan responsive design dengan baik, baik di versi web maupun aplikasi mobile. Desainnya secara otomatis menyesuaikan dengan ukuran dan jenis perangkat yang digunakan, memastikan tata letak tetap fungsional dan mudah dinavigasi. 

# 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- *Margin*
    - Space antara suatu elemen (bagian luarnya) denan elemen-elemen lain(diluar elemen itu sendiri).
    - Transparan(tidak terlihat).
    - Mempengaruhi jarak dengan elemen lain.
    - Tidak memengaruhi ukuran elemen.
- *Border*
    - Garis tepian yang membungkus konten dan paddingnya.
    - Bisa terlihat (punya warna, ketebalan, dan style).
    - Mempengaruhi ukuran dan tampilan elemen itu sendiri.
    - Menambah ukuran dan tampilan itu sendiri.
- *Padding*
    - Space antara batas suatu elemen dengan konten yang ada di dalam elemen itu sendiri.
    - Transparant (terlihat jika elemen memiliki background).
    - Mempengaruhi jarak antara konten dan border di dalam elemen.
    - Menambah ruang dalam elemen tanpa mempengaruhi elemen lain.

# 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flek box merupakan sistem dalam desain web yang mempermudah developer mengatur dan menyusun elemen-elemen di dalam suatu wadah dengan cara yang fleksibel. Dengan flex box, developer bisa menentukan arah susunan tata letak dan mengatur jarak antar elemen. Kegunaan dari flex box antara lain: 
    - Memberikan kontrol yang baik untuk mengatur elemen dalam satu dimensi dan sangat fleksibel dalam menyesuaikan elemen terhadap ruang yang tersedia.
    - Cocok untuk komponen dan layout sederhana yang hanya membutuhkan pengaturan dalam satu dimensi (horizontal atau vertikal) 
    - Dapat membuat elemen-elemen berpindah tempat atau dibungkus ke baris baru jika ruang tidak cukup.

- Grid merupakan sistem tata letak yang digunakan untuk mengatur elemen-elemen dalam dua dimensi (baris dan kolom). Sehingga developer bisa membuat layout halaman web yang terstruktur dan fleksibel. Kegunaan dari grid antara lain: 
    - Menawarkan kontrol penuh atas tata letak halaman, memungkinkan pengaturan layout yang lebih kompleks.
    - Fleksibel untuk tata letak dua dimensi yang lebih kompleks, seperti tata letak halaman yang terdiri dari header, konten utama, sidebar, dan footer.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- []Implementasikan fungsi untuk menghapus dan mengedit product.
    - Tambahkan fungsi bernama `edit_product` yang menerima parameter request dan id.
    ```
    def edit_product(request, id):
    # Get products berdasarkan id
    product = Products.objects.get(pk = id)

    #Set products sebagai instance dari form
    form = ProductsForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST" :
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form' : form}
    return render(request, "edit_product.html", context)
    ``` 
    - Pada urls.py import fungsi edit_product, `from main.views import edit_product`.
    - Lalu tambahkan path url `path('edit-product/<uuid:id>', edit_product, name='edit_product'),` ke dalam urlpattrens untuk mengakses fungsi yang sudah diimport tadi.
    - Kemudian kita buat berkas HTML baru dnegan nama `edit_product.html` pada direktori main/templates dengan code seperti ini,
    ```
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Edit Product</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}
    <div class="flex flex-col min-h-screen bg-white">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
        <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product👕</h1>
    
        <div class="bg-white shadow-lg rounded-lg p-6 form-style border border-blue-500">
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
                <div class="flex flex-col">
                    <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                        {{ field.label }}
                    </label>
                    <div class="w-full">
                        {{ field }}
                    </div>
                    {% if field.help_text %}
                        <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                    {% endif %}
                    {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
                <button type="submit" class="bg-pink-300 text-white font-semibold px-6 py-3 rounded-lg hover:bg-pink-700 transition duration-300 ease-in-out w-full">
                    Edit Product
                </button>
            </div>
        </form>
    </div>
    </div>
    </div>
    {% endblock %}
    ```
    - Selanjutnya kita tambahkan code seperti ini,
    ```
    <td>
        <a href="{% url 'main:edit_product' products.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    ```
    yang dimana `{% url 'main:edit_product' products.pk %}` digunakan untuk membangun URL dengan menambahkan primary key (pk) dari objek products sebagai parameter.

- []Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas 
    sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
    - []Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
        - *Halaman Login* (`login.html`):
            - Membuat sebuah login box berupa container yang dimana Elemen login berada di dalam box dengan warna bg putih dan border biru muda, serta di modif sudutnya lebih melengkung.
            - Membuat dua header di dalam login.
            - Memodifikasi warna fokus pada input dan warna border dan placeholder.
            ```
            {% extends 'base.html' %}
            {% block meta %}
            <title>Login</title>
            {% endblock meta %}
            {% block content %}
            <div class="min-h-screen flex items-center justify-center w-screen bg-pink-100 py-12 px-4 sm:px-6 lg:px-8">
            <div class="max-w-md w-full space-y-8" style="background-color: white; padding: 2rem; border-radius: 0.5rem; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); border: 2px solid lightskyblue;">
                <div>
                <h2 class="mt-6 text-center text-black text-3xl font-extrabold">
                    Welcome to Hoodie-Yay!
                </h2>
                <h2 class="mt-4 text-center text-black text-l font-medium"></p>
                    Login to Your Account
                </h2>
                </div>
                <form class="mt-8 space-y-6" method="POST" action="">
                {% csrf_token %}
                <input type="hidden" name="remember" value="true">
                <div class="rounded-md shadow-sm -space-y-px">
                    <div>
                    <label for="username" class="sr-only">Username</label>
                    <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-pink-300 placeholder-pink-500 text-pink-900 rounded-t-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm" placeholder="Username">
                    </div>
                    <div>
                    <label for="password" class="sr-only">Password</label>
                    <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-pink-300 placeholder-pink-500 text-blue-900 rounded-b-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm" placeholder="Password">
                    </div>
                </div>

                <div>
                    <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-pink-600 hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Sign in
                    </button>
                </div>
                </form>

                {% if messages %}
                <div class="mt-4">
                {% for message in messages %}
                {% if message.tags == "success" %}
                        <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                            <span class="block sm:inline">{{ message }}</span>
                        </div>
                    {% elif message.tags == "error" %}
                        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                            <span class="block sm:inline">{{ message }}</span>
                        </div>
                    {% else %}
                        <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                            <span class="block sm:inline">{{ message }}</span>
                        </div>
                    {% endif %}
                {% endfor %}
                </div>
                {% endif %}

                <div class="text-center mt-4">
                <p class="text-sm text-black">
                    Don't have an account yet?
                    <a href="{% url 'main:register' %}" class="font-medium text-pink-200 hover:text-pink-300">
                    Register Now
                    </a>
                </p>
                </div>
            </div>
            </div>
            {% endblock content %}
            ```

        - *Halaman Register* (`register.html`):
            - Membuat sebuah register box berupa container yang dimana Elemen login berada di dalam box dengan warna bg putih dan border biru muda, serta di modif sudutnya lebih melengkung.
            - Memodifikasi tautan ke halaman login menggunakan warna pink muda (text-pink-200) dengan efek hover yang sedikit lebih terang (hover:text-pink-300).
            - - Memodifikasi warna fokus pada input dan warna border dan placeholder.
            ```
            {% extends 'base.html' %}

            {% block meta %}
            <title>Register</title>
            {% endblock meta %}

            {% block content %}
            <div class="min-h-screen flex items-center justify-center w-screen bg-pink-100 py-12 px-4 sm:px-6 lg:px-8">
            <div class="max-w-md w-full space-y-8 form-style">
            <div class="max-w-md w-full space-y-8" style="background-color: white; padding: 2rem; border-radius: 0.5rem; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); border: 2px solid lightskyblue;">
                <div>
                <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
                    Create Your Account
                </h2>
                </div>
                <form class="mt-8 space-y-6" method="POST">
                {% csrf_token %}
                <input type="hidden" name="remember" value="true">
                <div class="rounded-md shadow-sm -space-y-px">
                    {% for field in form %}
                    <div class="{% if not forloop.first %}mt-4{% endif %}">
                        <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                        {{ field.label }}
                        </label>
                        <div class="relative">
                        {{ field }}
                        <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                            {% if field.errors %}
                            <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                            </svg>
                            {% endif %}
                        </div>
                        </div>
                        {% if field.errors %}
                        {% for error in field.errors %}
                            <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                        {% endfor %}
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>

                <div>
                    <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-pink-600 hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Register
                    </button>
                </div>
                </form>

                {% if messages %}
                <div class="mt-4">
                {% for message in messages %}
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
                {% endfor %}
                </div>
                {% endif %}

                <div class="text-center mt-4">
                <p class="text-sm text-black">
                    Already have an account?
                    <a href="{% url 'main:login' %}" class="font-medium text-pink-200 hover:text-pink-300">
                    Login here
                    </a>
                </p>
                </div>
            </div>
            </div>
            {% endblock content %}
            ```
        
        - *Tambah Product*
            - Menambahkan container box dengan border biru.
            - Memodifikasi warna submit button dan focus input fields.
            ```
            {% extends 'base.html' %}
            {% load static %}
            {% block meta %}
            <title>Create Product</title>
            {% endblock meta %}

            {% block content %}
            {% include 'navbar.html' %}

            <div class="flex flex-col min-h-screen bg-white">
            <div class="container mx-auto 
            x-4 py-8 mt-16 max-w-xl">
                <h1 class="text-3xl font-bold text-center mb-8 text-black">Create Product👕</h1>
            
                <div class="bg-white shadow-md rounded-lg p-6 form-style border border-blue-500">
                <form method="POST" class="space-y-6">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="flex flex-col">
                        <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                        {{ field.label }}
                        </label>
                        <div class="w-full">
                        {{ field }}
                        </div>
                        {% if field.help_text %}
                        <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                        {% endif %}
                        {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                        {% endfor %}
                    </div>
                    {% endfor %}
                    <div class="flex justify-center mt-6">
                    <button type="submit" class="bg-pink-300 text-white font-semibold px-6 py-3 rounded-lg hover:bg-pink-700 transition duration-300 ease-in-out w-full">
                        Create Product
                    </button>
                    </div>
                </form>
                </div>
            </div>
            </div>

            {% endblock %}
            ```

    - []Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
        - []Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
        Di dalam `main.html` kita tambahkan code berikut,
        ```
        {% if not products_entries %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/product-empty.png' %}" alt="Empty products" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">Belum ada products yang ditambahkan pada Hoodie-Yay!</p>
        </div>
        {% else %}
        ```
        `<img src="{% static 'image/product-empty.png' %}" `, menunjukkan path file gambar, yang berarti gambar ini berada di dalam folder image di bawah direktori static.

        - []Jika sudah ada product yang tersimpan, halaman  daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
            - Membuat cointainer product card dengan border biru, dan memiliki sudut melengkung.
            - Gambar produk ditampilkan di bagian atas card, menggunakan atribut *src* untuk menampilkan gambar yang berasal dari `{{ products.image }}`.
            - Nama produk ditampilkan dengan `font-bold text-xl text-gray-800 mb-2`
            - Harga produk ditampilkan dibawah nama dengan ukuran ditampilkan di bawah nama dalam ukuran lebih kecil.
            - Deskripsi produk ditampilkan di bawah harga dengan warna teks lebih gelap.
            - Terdapat garis pemisah antara deskripsi dan stok produk, serta memisahkan bagain stok dengan bagian tombol edit dan delete.
            ```
            <div class="relative break-inside-avoid">
            <div class="relative bg-white shadow-md border border-blue-500 rounded-lg mb-6 break-inside-avoid flex flex-col p-4">
                <div class="mb-4">
                <img src="{{ products.image }}" alt="{{ products.name }}" class="rounded-lg w-full">
                </div>
                <div class="mb-4">
                <h3 class="font-bold text-xl text-gray-800 mb-2">{{products.name}}</h3>
                <p class="text-gray-500 text-md">Rp {{products.price}}</p>
                <p class="mt-4 text-gray-700 leading-snug">{{products.description}}</p>
                </div>
                <hr class="border-t border-gray-300 my-4">
                <div>
                <p class="font-semibold text-lg text-gray-700 mb-1">Stock</p>
                <p class="text-gray-600">{{products.stock}}</p>
                </div>
                <hr class="border-t border-gray-300 my-4">
                <div class="mt-auto flex justify-center space-x-2">
                    <a href="{% url 'main:edit_product' products.pk %}" class="bg-yellow-400 hover:bg-yellow-500 text-white text-sm font-bold px-3 py-2 rounded-md transition duration-300">
                    Edit
                    </a>
                    <a href="{% url 'main:delete_product' products.pk %}" class="bg-red-400 hover:bg-red-500 text-white text-sm font-bold px-3 py-2 rounded-md transition duration-300">
                    Delete
                    </a>
                </div>
            </div>
            </div>
            ```

    - []Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
        - Tombol edit dengan warna latar kuning dan berubah menjadi lebih gelap saat di hover. Dengan teks "edit" berwarna putih bold.
        - Tombol delete dengan warna latar merah dan berubah menjadi lebih gelap saat di hover. Dengan teks "delete" berwarna putih bold.
        ```
        <div class="mt-auto flex justify-center space-x-2">
            <a href="{% url 'main:edit_product' products.pk %}" class="bg-yellow-400 hover:bg-yellow-500 text-white text-sm font-bold px-3 py-2 rounded-md transition duration-300">
            Edit
            </a>
            <a href="{% url 'main:delete_product' products.pk %}" class="bg-red-400 hover:bg-red-500 text-white text-sm font-bold px-3 py-2 rounded-md transition duration-300">
            Delete
            </a>
        </div>
        ```

    - []Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
        ```
        <nav class="bg-pink-400 shadow-lg fixed top-0 left-0 z-40 w-screen">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center">
                <h1 class="text-2xl font-bold text-center text-white">Hoodie-Yay!</h1>
                </div>

                <div class="hidden md:flex items-center space-x-4">
                <a href="#" class="text-white hover:bg-blue-500 px-3 py-2 rounded">Home</a>
                <a href="#" class="text-white hover:bg-blue-500 px-3 py-2 rounded">Products</a>
                <a href="#" class="text-white hover:bg-blue-500 px-3 py-2 rounded">Categories</a>
                {% if user.is_authenticated %}
                    <span class="text-white mr-4">Welcome, {{ user.username }}</span>
                    <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                    Login
                    </a>
                    <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                    </a>
                {% endif %}
                </div>

                <div class="md:hidden flex items-center">
                <button class="mobile-menu-button">
                    <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                    <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
                </div>
            </div>
            </div>
            
            <!-- Mobile menu -->
            <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
            <div class="pt-2 pb-3 space-y-1 mx-auto">
                <a href="#" class="block text-white hover:bg-blue-500 px-3 py-2 rounded">Home</a>
                <a href="#" class="block text-white hover:bg-blue-500 px-3 py-2 rounded">Products</a>
                <a href="#" class="block text-white hover:bg-blue-500 px-3 py-2 rounded">Categories</a>
                {% if user.is_authenticated %}
                <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                </a>
                {% else %}
                <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                </a>
                {% endif %}
            </div>
            </div>
            <script>
            const btn = document.querySelector("button.mobile-menu-button");
            const menu = document.querySelector(".mobile-menu");
            
            btn.addEventListener("click", () => {
                menu.classList.toggle("hidden");
            });
            </script>
        </nav>
        ```

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
    - Selanjutnya, mengubah value `product_entries` dan `context` untuk key 'name' pada fungsi `show_main` menjadi :
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