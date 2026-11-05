// File: PesananDelivery.java
// Penanggung Jawab: Aldo Prawiro Akbar (13242520007)
// Konsep OOP: Inheritance (extends Pesanan) & Polymorphism (@Override)

public class PesananDelivery extends Pesanan {

    public PesananDelivery(String idPesanan, String namaPelanggan, int totalHarga) {
        super(idPesanan, namaPelanggan, totalHarga);
    }

    @Override
    public String getJenisPesanan() {
        return "Delivery (Layanan Pesan Antar)";
    }

    @Override
    public void tampilkanStatusLayanan() {
        System.out.println("Status     : Pesanan disegel aman dan dikirim melalui kurir restoran.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Kurir sedang mengantarkan pesanan Delivery ke alamat " + getNamaPelanggan() + ".");
    }
}
