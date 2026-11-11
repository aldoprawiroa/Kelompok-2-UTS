# PANDUAN LENGKAP PRESENTASI & TANYA JAWAB (Q&A)
## Proyek UTS Pemrograman Berorientasi Objek (PBO)
**Judul Proyek:** Pengembangan Aplikasi Sistem Informasi Restoran Berbasis Object Oriented Programming (Java)  
**Kelompok:** Kelompok 2 - Kelas A  
**Program Studi:** S1 Teknologi Informasi, FTIK - Universitas Muhammadiyah Semarang (UNIMUS)  
**Tahun Akademik:** 2026/2027  

---

## 👥 Profil Anggota Tim & Pembagian Tugas
1. **Fadhil Anshor (13242520005)**
   - *Peran Utama:* Moderator, Presenter Pembuka & Penutup, Penanggung Jawab Modul Pegawai.
   - *File Java:* `Pegawai.java` (Parent Abstract), `Chef.java`, `Pelayan.java`, `Kasir.java`.
2. **Aldo Prawiro Akbar (13242520007)**
   - *Peran Utama:* Presenter Diagram UML (Sequence & Activity), Penanggung Jawab Modul Pesanan.
   - *File Java:* `Pesanan.java` (Parent Abstract), `PesananDineIn.java`, `PesananTakeAway.java`, `PesananDelivery.java`.
3. **Zhafirah Haya Destiani (13242520008)**
   - *Peran Utama:* Presenter Diagram UML (Class & Use Case), Penanggung Jawab Modul Menu Restoran.
   - *File Java:* `MenuRestoran.java` (Parent Abstract), `MenuMakanan.java`, `MenuMinuman.java`, `MenuDessert.java`.
4. **Pengerjaan Bersama (Tim):**
   - `LayananRestoran.java` (Interface Puncak)
   - `Main.java` (Controller Menu Utama CLI & Koleksi `ArrayList`)

---

## ⏱️ Alokasi Waktu Presentasi (Estimasi 10 - 15 Menit)

| No | Bagian Slide | Pembicara | Durasi | Topik Utama |
|---|---|---|---|---|
| 1 | Slide 1 - 4 | **Fadhil Anshor** | 2.5 Menit | Pembukaan, Latar Belakang Masalah, Solusi OOP, Tujuan Sistem |
| 2 | Slide 5 - 7 | **Zhafirah Haya Destiani** | 3.0 Menit | Struktur 14 Class, Modul Menu, Class Diagram, Use Case Diagram |
| 3 | Slide 8 - 9 | **Aldo Prawiro Akbar** | 2.5 Menit | Modul Pesanan, Activity Diagram (4 Swimlane), Sequence Diagram |
| 4 | Slide 10 - 13 | **Bergantian (Fadhil, Zhafirah, Aldo)** | 3.5 Menit | Pembuktian 5 Pilar OOP pada Kode (Class/Object, Enkapsulasi, Inheritance, Polymorphism, Abstraction) |
| 5 | Slide 14 - 15 | **Aldo Prawiro Akbar** | 1.5 Menit | Demonstrasi Eksekusi Program (Menu Utama, Input Data, Update ID, Output Polimorfik) |
| 6 | Slide 16 - 18 | **Fadhil Anshor** | 2.0 Menit | Kendala & Solusi (Buffer Scanner, Standarisasi Tim), Kesimpulan, Saran GUI/DB, Penutup |

---

## 🎤 Skrip Presentasi Lengkap (Kata Demi Kata)

### Bagian 1: Pembukaan & Latar Belakang (Fadhil Anshor)
> *"Assalamu’alaikum Warahmatullahi Wabarakatuh. Selamat pagi/siang kepada Bapak/Ibu Dosen Pengampu mata kuliah Pemrograman Berorientasi Objek dan rekan-rekan mahasiswa yang kami banggakan.*  
> *Kami dari Kelompok 2 Kelas A yang beranggotakan: saya sendiri Fadhil Anshor, rekan saya Aldo Prawiro Akbar, dan Zhafirah Haya Destiani. Pada hari ini, kami akan mempresentasikan hasil proyek Ujian Tengah Semester kami yang berjudul: **Pengembangan Aplikasi Sistem Informasi Restoran Berbasis Object Oriented Programming Menggunakan Java**.*  
>  
> *Latar belakang proyek ini berakar dari kompleksitas operasional restoran modern yang harus mengelola tiga hal krusial setiap harinya: katalog hidangan, giliran kerja staf pegawai, dan transaksi pesanan pelanggan. Jika dicatat secara konvensional atau menggunakan paradigma prosedural linier, risiko human error seperti salah harga, jadwal kerja bentrok, dan salah tipe pengantaran akan sangat tinggi.*  
> *Oleh karena itu, kami menerapkan paradigma OOP berbasis Java. Melalui OOP, seluruh entitas dimodelkan menjadi kelas-kelas modular, aman dengan enkapsulasi data, efisien melalui pewarisan, dan adaptif melalui polimorfisme."*

### Bagian 2: Arsitektur 14 Class & Pemodelan UML (Zhafirah Haya Destiani)
> *"Terima kasih saudara Fadhil. Saya Zhafirah Haya Destiani akan melanjutkan penjelasan mengenai arsitektur sistem dan pemodelan UML.*  
> *Sesuai pedoman praktikum untuk kelompok 3 orang, sistem kami dirancang terdiri dari **tepat 14 file Java**: 1 Interface puncak (`LayananRestoran`), 3 Parent Abstract Class (`MenuRestoran`, `Pegawai`, `Pesanan`), 9 Child Subclass (masing-masing 3 turunan per modul), dan 1 Main Class.*  
>  
> *Pada **Class Diagram**, terlihat bahwa interface `LayananRestoran` mendefinisikan kontrak method `tampilkanAktivitas()`. Ketiga abstract class utama merealisasikan interface ini. Saya bertanggung jawab pada Modul Menu (`MenuRestoran`), yang memiliki 3 turunan: `MenuMakanan`, `MenuMinuman`, dan `MenuDessert`. Seluruh atribut dilindungi secara private dan hanya diakses melalui getter dan setter publik.*  
>  
> *Pada **Use Case Diagram**, Aktor utama yaitu Admin Kasir berinteraksi dengan 6 menu operasional. Pada use case Input Data, kami menyertakan relasi `<<extend>>` yang merepresentasikan percabangan kategori spesifik sesuai modul yang dipilih pengguna."*

### Bagian 3: Activity & Sequence Diagram (Aldo Prawiro Akbar)
> *"Terima kasih Zhafirah. Saya Aldo Prawiro Akbar akan memaparkan alur Activity Diagram dan Sequence Diagram.*  
> *Pada **Activity Diagram**, alur sistem kami kelompokkan ke dalam 4 swimlane: Pengguna, Main, LayananRestoran, dan Kelas Terkait. Diagram ini menggambarkan bagaimana sistem mengevaluasi percabangan menu, menginstansiasi objek yang tepat, hingga menyajikan informasi kembali ke layar konsol sampai pengguna memilih menu Keluar.*  
>  
> *Pada **Sequence Diagram**, kami memodelkan 4 skenario pertukaran pesan antar objek secara runut waktu: proses pembuatan objek baru via constructor dan penyimpanannya ke `ArrayList`, proses penelusuran data polimorfik, serta proses pencarian ID dan pemanggilan method setter saat pengguna memperbarui data transaksi pada modul Pesanan yang saya kelola (`PesananDineIn`, `PesananTakeAway`, dan `PesananDelivery`)."*

### Bagian 4: Pembuktian 5 Pilar OOP pada Kode (Kolaboratif)
- **Fadhil (Pilar 1 & 2):**  
  > *"Untuk Pilar 1: Class & Object, kami mendefinisikan class sebagai blueprint dan menginstansiasinya secara nyata menggunakan operator `new` ke dalam ArrayList dinamis.*  
  > *Untuk Pilar 2: Encapsulation, kami memproteksi seluruh atribut (seperti `idPegawai`, `harga`, `totalHarga`) dengan modifier `private`. Akses baca dan tulis diatur ketat melalui getter dan setter demi integritas data."*
- **Zhafirah (Pilar 3 & 5):**  
  > *"Untuk Pilar 3: Inheritance, subclass menggunakan keyword `extends` dan constructor memanggil `super(...)` untuk mewarisi atribut induk tanpa menulis ulang kode.*  
  > *Untuk Pilar 5: Abstraction & Interface, kami menggunakan Interface `LayananRestoran` sebagai kontrak murni, dan 3 parent class abstrak untuk mencegah pembuatan objek setengah jadi."*
- **Aldo (Pilar 4):**  
  > *"Untuk Pilar 4: Polymorphism, dalam method `tampilkanSemuaData()`, kami melakukan loop pada ArrayList. Melalui satu baris perintah `p.tampilkanData()`, sistem secara otomatis mengeksekusi method overriding yang sesuai dengan jenis objek aslinya saat runtime."*

### Bagian 5: Demonstrasi Program (Aldo Prawiro Akbar)
> *"Berikut adalah bukti eksekusi program konsol CLI kami:*  
> *Gambar 1 menampilkan 6 menu navigasi utama. Gambar 2 memperlihatkan alur input data yang interaktif. Gambar 3 memperlihatkan fitur Ubah Data berdasarkan ID unik, dan Gambar 4 menunjukkan keberhasilan polimorfisme di mana seluruh data makanan, pegawai, dan pesanan ditampilkan dengan format tugas dan layanan spesifik masing-masing."*

### Bagian 6: Kendala, Solusi, Kesimpulan & Penutup (Fadhil Anshor)
> *"Selama pengerjaan, kami menghadapi dua kendala teknis: Pertama, buffer Scanner yang meloncat saat membaca teks setelah angka (`nextInt()` diikuti `nextLine()`), yang kami selesaikan dengan menambahkan buffer cleanser `input.nextLine();`.*  
> *Kedua, sinkronisasi struktur penamaan antar anggota, yang kami selesaikan dengan menyepakati Interface bersama di awal.*  
>  
> *Kesimpulannya, proyek ini berhasil membuktikan penerapan 5 pilar OOP secara utuh pada 14 file Java yang selaras 100% dengan diagram UML. Ke depan, sistem ini siap dikembangkan ke antarmuka GUI JavaFX dan database MySQL permanen.*  
> *Sekian presentasi dari Kelompok 2. Kami membuka sesi tanya jawab untuk Bapak/Ibu dosen dan rekan-rekan sekalian. Terima kasih. Wassalamu’alaikum Warahmatullahi Wabarakatuh."*

---

## 🎯 Bocoran Pertanyaan Dosen Penguji & Kunci Jawaban (FAQ)

### Pertanyaan 1: Mengapa parent class dibuat `abstract`, kenapa tidak dibuat class biasa saja?
- **Siapa yang menjawab:** Zhafirah atau Fadhil
- **Kunci Jawaban:**  
  *"Alasannya adalah untuk mencegah instansiasi objek yang belum lengkap atau 'setengah jadi'. Dalam logika bisnis restoran, tidak ada entitas pegawai yang berdiri sendiri tanpa jabatan jelas; pegawai haruslah konkret sebagai Chef, Pelayan, atau Kasir. Begitu pula dengan Menu dan Pesanan. Dengan menjadikannya `abstract class`, Java compiler akan melarang perintah seperti `new Pegawai()`, sehingga memaksa program untuk hanya menginstansiasi subclass yang spesifik dan konkret."*

### Pertanyaan 2: Mengapa butuh `Interface LayananRestoran` jika sudah ada `Abstract Class`? Apa bedanya?
- **Siapa yang menjawab:** Zhafirah
- **Kunci Jawaban:**  
  *"Perbedaannya terletak pada hierarki dan tujuan: Abstract Class digunakan untuk kelas-kelas yang memiliki hubungan keturunan atau 'is-a' (misal Chef adalah Pegawai), dan dapat menyimpan atribut state (variabel) serta method konkret.*  
  *Sedangkan Interface digunakan untuk mendefinisikan kontrak perilaku murni atau 'can-do' tanpa mempedulikan hierarki kelas. Menu (barang/katalog), Pegawai (manusia/SDM), dan Pesanan (transaksi) tidak memiliki hubungan keturunan biologis, tetapi ketiganya sama-sama merupakan komponen dari operasional pelayanan restoran. Karena Java tidak mendukung multiple inheritance pada class, Interface adalah solusi terbaik untuk menstandarisasikan method `tampilkanAktivitas()` di seluruh level sistem."*

### Pertanyaan 3: Tunjukkan di mana letak Polymorphism di kode `Main.java`!
- **Siapa yang menjawab:** Aldo
- **Kunci Jawaban:**  
  *"Polimorfisme dinamis (dynamic method dispatch) terletak pada method `tampilkanSemuaData()` di `Main.java`. Di sana kami menuliskan perulangan:*  
  ```java
  for (Pegawai p : daftarPegawai) {
      p.tampilkanData();
      p.tampilkanAktivitas();
  }
  ```  
  *Variabel referensi `p` bertipe parent `Pegawai`, namun objek aslinya di memori bisa berupa `Chef`, `Pelayan`, atau `Kasir`. Saat runtime, Java secara dinamis mengeksekusi method overriding milik masing-masing subclass tanpa memerlukan percabangan `if-else` manual."*

### Pertanyaan 4: Apa yang terjadi jika atribut tidak dibuat `private` (Enkapsulasi diabaikan)?
- **Siapa yang menjawab:** Fadhil
- **Kunci Jawaban:**  
  *"Jika atribut dibiarkan berstatus `public`, maka nilai seperti harga menu atau total harga pesanan dapat diakses dan diubah secara bebas dari luar class tanpa melalui validasi. Hal ini membuka risiko data corruption, misalnya harga diisi angka negatif atau total bayar diubah secara ilegal. Dengan membuat atribut `private` dan menyediakan `setter/getter`, kita menerapkan information hiding dan memastikan setiap pembaruan data terkontrol secara aman."*

### Pertanyaan 5: Mengapa menggunakan constructor `super(...)` pada child class?
- **Siapa yang menjawab:** Zhafirah atau Aldo
- **Kunci Jawaban:**  
  *"Karena atribut umum (seperti `idMenu`, `namaMenu`, `harga` pada Menu, atau `idPesanan` pada Pesanan) dideklarasikan di parent class dan bersifat `private`. Child class tidak bisa langsung mengakses atau menginisialisasi atribut private milik parent secara sembarangan. Oleh karena itu, constructor child class memanggil `super(...)` untuk meneruskan nilai argumen ke constructor parent class agar diinisialisasi dengan benar."*

### Pertanyaan 6: Kenapa kalian menggunakan `ArrayList` bukan array biasa (misal `Pegawai[]`)?
- **Siapa yang menjawab:** Aldo atau Fadhil
- **Kunci Jawaban:**  
  *"Karena jumlah data menu, pegawai, dan pesanan pelanggan di restoran bersifat dinamis dan tidak bisa diprediksi jumlah pastinya di awal. Array biasa berukuran tetap (fixed-size). Sedangkan `ArrayList` dari Java Collection Framework memiliki ukuran dinamis yang otomatis menyesuaikan kapasitas memori saat ada penambahan data baru menggunakan method `.add()`."*

### Pertanyaan 7: Jelaskan apa kendala teknis Scanner yang kalian temui dan bagaimana solusinya!
- **Siapa yang menjawab:** Fadhil
- **Kunci Jawaban:**  
  *"Kendalanya adalah Scanner skipping. Saat kita membaca input angka menggunakan `input.nextInt()` dan kemudian langsung memanggil `input.nextLine()` untuk membaca teks, input teks tersebut terlewat otomatis. Penyebabnya adalah `nextInt()` hanya membaca karakter angka dan menyisakan karakter newline (`\n` alias tombol enter) di buffer Scanner. Solusinya, kami menambahkan satu baris `input.nextLine();` tepat setelah setiap pemanggilan `nextInt()` untuk membersihkan buffer sebelum membaca input string berikutnya."*
