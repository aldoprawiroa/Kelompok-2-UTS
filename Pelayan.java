// File: Pelayan.java
// Penanggung Jawab: Fadhil Anshor (13242520005)
// Konsep OOP: Inheritance (extends Pegawai) & Polymorphism (@Override)

public class Pelayan extends Pegawai {

    public Pelayan(String idPegawai, String namaPegawai, String shiftKerja) {
        super(idPegawai, namaPegawai, shiftKerja);
    }

    @Override
    public String getJabatan() {
        return "Pelayan (Waiter / Pramusaji)";
    }

    @Override
    public void tampilkanTugas() {
        System.out.println("Tugas Utama: Mencatat pesanan tamu dan mengantarkan makanan ke meja.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Pelayan " + getNamaPegawai() + " sedang melayani pelanggan di area makan.");
    }
}
