// File: Pesanan.java
// Penanggung Jawab: Aldo Prawiro Akbar (13242520007)
// Konsep OOP: Abstraction, Encapsulation, Interface Implementation

public abstract class Pesanan implements LayananRestoran {
    // Encapsulation: Atribut dibuat private
    private String idPesanan;
    private String namaPelanggan;
    private int totalHarga;

    // Constructor
    public Pesanan(String idPesanan, String namaPelanggan, int totalHarga) {
        this.idPesanan = idPesanan;
        this.namaPelanggan = namaPelanggan;
        this.totalHarga = totalHarga;
    }

    // Getter dan Setter
    public String getIdPesanan() {
        return idPesanan;
    }

    public String getNamaPelanggan() {
        return namaPelanggan;
    }

    public void setNamaPelanggan(String namaPelanggan) {
        this.namaPelanggan = namaPelanggan;
    }

    public int getTotalHarga() {
        return totalHarga;
    }

    public void setTotalHarga(int totalHarga) {
        this.totalHarga = totalHarga;
    }

    // Method Abstract
    public abstract String getJenisPesanan();
    public abstract void tampilkanStatusLayanan();

    // Menampilkan data lengkap pesanan
    public void tampilkanData() {
        System.out.println("ID Pesanan : " + idPesanan);
        System.out.println("Pelanggan  : " + namaPelanggan);
        System.out.println("Tipe Order : " + getJenisPesanan());
        System.out.println("Total Bayar: Rp" + totalHarga);
        tampilkanStatusLayanan();
    }
}
