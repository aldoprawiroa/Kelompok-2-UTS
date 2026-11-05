// File: MenuRestoran.java
// Penanggung Jawab: Zhafirah Haya Destiani (13242520008)
// Konsep OOP: Abstraction, Encapsulation, Interface Implementation

public abstract class MenuRestoran implements LayananRestoran {
    // Encapsulation: Atribut dibuat private
    private String idMenu;
    private String namaMenu;
    private int harga;

    // Constructor
    public MenuRestoran(String idMenu, String namaMenu, int harga) {
        this.idMenu = idMenu;
        this.namaMenu = namaMenu;
        this.harga = harga;
    }

    // Getter dan Setter
    public String getIdMenu() {
        return idMenu;
    }

    public String getNamaMenu() {
        return namaMenu;
    }

    public void setNamaMenu(String namaMenu) {
        this.namaMenu = namaMenu;
    }

    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        this.harga = harga;
    }

    // Method Abstract yang wajib di-override oleh Child Class
    public abstract String getJenisMenu();
    public abstract void tampilkanPenyajian();

    // Method untuk menampilkan informasi dasar menu
    public void tampilkanData() {
        System.out.println("ID Menu    : " + idMenu);
        System.out.println("Nama Menu  : " + namaMenu);
        System.out.println("Kategori   : " + getJenisMenu());
        System.out.println("Harga      : Rp" + harga);
        tampilkanPenyajian();
    }
}
