// File: PesananDineIn.java
// Penanggung Jawab: Aldo Prawiro Akbar (13242520007)
// Konsep OOP: Inheritance (extends Pesanan) & Polymorphism (@Override)

public class PesananDineIn extends Pesanan {

    public PesananDineIn(String idPesanan, String namaPelanggan, int totalHarga) {
        super(idPesanan, namaPelanggan, totalHarga);
    }

    @Override
    public String getJenisPesanan() {
        return "Dine-In (Makan di Tempat)";
    }

    @Override
    public void tampilkanStatusLayanan() {
        System.out.println("Status     : Hidangan diantarkan langsung ke meja pelanggan.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Pesanan Dine-In atas nama " + getNamaPelanggan() + " sedang disajikan di meja.");
    }
}
