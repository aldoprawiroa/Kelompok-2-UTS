// File: Pegawai.java
// Penanggung Jawab: Fadhil Anshor (13242520005)
// Konsep OOP: Abstraction, Encapsulation, Interface Implementation

public abstract class Pegawai implements LayananRestoran {
    // Encapsulation: Atribut bersifat private
    private String idPegawai;
    private String namaPegawai;
    private String shiftKerja;

    // Constructor
    public Pegawai(String idPegawai, String namaPegawai, String shiftKerja) {
        this.idPegawai = idPegawai;
        this.namaPegawai = namaPegawai;
        this.shiftKerja = shiftKerja;
    }

    // Getter dan Setter
    public String getIdPegawai() {
        return idPegawai;
    }

    public String getNamaPegawai() {
        return namaPegawai;
    }

    public void setNamaPegawai(String namaPegawai) {
        this.namaPegawai = namaPegawai;
    }

    public String getShiftKerja() {
        return shiftKerja;
    }

    public void setShiftKerja(String shiftKerja) {
        this.shiftKerja = shiftKerja;
    }

    // Method Abstract
    public abstract String getJabatan();
    public abstract void tampilkanTugas();

    // Menampilkan data lengkap pegawai
    public void tampilkanData() {
        System.out.println("ID Pegawai : " + idPegawai);
        System.out.println("Nama       : " + namaPegawai);
        System.out.println("Jabatan    : " + getJabatan());
        System.out.println("Shift Kerja: " + shiftKerja);
        tampilkanTugas();
    }
}
