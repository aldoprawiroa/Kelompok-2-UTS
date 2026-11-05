// File: MenuMakanan.java
// Penanggung Jawab: Zhafirah Haya Destiani (13242520008)
// Konsep OOP: Inheritance (extends MenuRestoran) & Polymorphism (@Override)

public class MenuMakanan extends MenuRestoran {

    public MenuMakanan(String idMenu, String namaMenu, int harga) {
        super(idMenu, namaMenu, harga);
    }

    @Override
    public String getJenisMenu() {
        return "Makanan Utama (Main Course)";
    }

    @Override
    public void tampilkanPenyajian() {
        System.out.println("Penyajian  : Disajikan hangat di atas piring keramik utama.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Dapur sedang memasak hidangan makanan [" + getNamaMenu() + "].");
    }
}
