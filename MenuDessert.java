// File: MenuDessert.java
// Penanggung Jawab: Zhafirah Haya Destiani (13242520008)
// Konsep OOP: Inheritance (extends MenuRestoran) & Polymorphism (@Override)

public class MenuDessert extends MenuRestoran {

    public MenuDessert(String idMenu, String namaMenu, int harga) {
        super(idMenu, namaMenu, harga);
    }

    @Override
    public String getJenisMenu() {
        return "Hidangan Penutup (Dessert)";
    }

    @Override
    public void tampilkanPenyajian() {
        System.out.println("Penyajian  : Disajikan dingin dengan garnis manis di piring kecil.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Bagian pastry sedang menyiapkan dessert [" + getNamaMenu() + "].");
    }
}
