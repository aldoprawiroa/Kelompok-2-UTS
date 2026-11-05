// File: MenuMinuman.java
// Penanggung Jawab: Zhafirah Haya Destiani (13242520008)
// Konsep OOP: Inheritance (extends MenuRestoran) & Polymorphism (@Override)

public class MenuMinuman extends MenuRestoran {

    public MenuMinuman(String idMenu, String namaMenu, int harga) {
        super(idMenu, namaMenu, harga);
    }

    @Override
    public String getJenisMenu() {
        return "Minuman Segar (Beverage)";
    }

    @Override
    public void tampilkanPenyajian() {
        System.out.println("Penyajian  : Disajikan di dalam gelas saji lengkap dengan sedotan.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Barista sedang meracik minuman [" + getNamaMenu() + "].");
    }
}
