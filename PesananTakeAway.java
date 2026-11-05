// File: PesananTakeAway.java
// Penanggung Jawab: Aldo Prawiro Akbar (13242520007)
// Konsep OOP: Inheritance (extends Pesanan) & Polymorphism (@Override)

public class PesananTakeAway extends Pesanan {

    public PesananTakeAway(String idPesanan, String namaPelanggan, int totalHarga) {
        super(idPesanan, namaPelanggan, totalHarga);
    }

    @Override
    public String getJenisPesanan() {
        return "Take-Away (Dibungkus / Bawa Pulang)";
    }

    @Override
    public void tampilkanStatusLayanan() {
        System.out.println("Status     : Makanan dikemas rapi dalam kemasan food-grade untuk dibawa pulang.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Pesanan Take-Away milik " + getNamaPelanggan() + " siap diambil di loket kasir.");
    }
}
