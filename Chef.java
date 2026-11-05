// File: Chef.java
// Penanggung Jawab: Fadhil Anshor (13242520005)
// Konsep OOP: Inheritance (extends Pegawai) & Polymorphism (@Override)

public class Chef extends Pegawai {

    public Chef(String idPegawai, String namaPegawai, String shiftKerja) {
        super(idPegawai, namaPegawai, shiftKerja);
    }

    @Override
    public String getJabatan() {
        return "Chef (Juru Masak Dapur)";
    }

    @Override
    public void tampilkanTugas() {
        System.out.println("Tugas Utama: Memasak hidangan dan menjaga kualitas rasa masakan.");
    }

    @Override
    public void tampilkanAktivitas() {
        System.out.println("Aktivitas  : Chef " + getNamaPegawai() + " sedang bertugas memasak pada shift " + getShiftKerja() + ".");
    }
}
