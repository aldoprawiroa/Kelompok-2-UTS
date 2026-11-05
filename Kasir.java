// File: Kasir.java
// Penanggung Jawab: Fadhil Anshor (13242520005)
// Konsep OOP: Inheritance (extends Pegawai) & Polymorphism (@Override)

public class Kasir extends Pegawai {

    public Kasir(String idPegawai, String namaPegawai, String shiftKerja) {
        super(idPegawai, namaPegawai, shiftKerja);
    }

    @Override
    public String getJabatan() {
        return "Kasir (Bagian Pembayaran)";
    }

    @Override
    public void tampilkanTugas() {
        System.out.println("Tugas Utama: Melayani pembayaran pelanggan dan mencetak struk transaksi.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Kasir " + getNamaPegawai() + " sedang memproses pembayaran di meja kasir.");
    }
}
