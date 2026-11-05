// File: Main.java
// Program Utama Sistem Informasi Restoran - Kelompok 2

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private static Scanner input = new Scanner(System.in);
    private static ArrayList<MenuRestoran> daftarMenu = new ArrayList<>();
    private static ArrayList<Pegawai> daftarPegawai = new ArrayList<>();
    private static ArrayList<Pesanan> daftarPesanan = new ArrayList<>();

    public static void main(String[] args) {
        int pilihan;
        do {
            System.out.println("\n=============================================");
            System.out.println("       SISTEM INFORMASI RESTORAN (KLP 2)     ");
            System.out.println("=============================================");
            System.out.println("1. Input Data Menu Restoran");
            System.out.println("2. Input Data Pegawai Restoran");
            System.out.println("3. Input Data Pesanan Pelanggan");
            System.out.println("4. Tampilkan Semua Data (Polymorphism)");
            System.out.println("5. Ubah Data");
            System.out.println("6. Keluar");
            System.out.print("Pilih menu (1-6): ");
            pilihan = input.nextInt();
            input.nextLine(); // Membersihkan buffer enter

            switch (pilihan) {
                case 1:
                    inputDataMenu();
                    break;
                case 2:
                    inputDataPegawai();
                    break;
                case 3:
                    inputDataPesanan();
                    break;
                case 4:
                    tampilkanSemuaData();
                    break;
                case 5:
                    ubahData();
                    break;
                case 6:
                    System.out.println("Terima kasih telah menggunakan Sistem Informasi Restoran!");
                    break;
                default:
                    System.out.println("Pilihan tidak valid!");
            }
        } while (pilihan != 6);
    }

    // 1. Method Input Data Menu (Bagian Zhafirah)
    public static void inputDataMenu() {
        System.out.println("\n--- Pilih Jenis Menu ---");
        System.out.println("1. Menu Makanan");
        System.out.println("2. Menu Minuman");
        System.out.println("3. Menu Dessert");
        System.out.print("Pilihan (1-3): ");
        int jenis = input.nextInt();
        input.nextLine();

        System.out.print("Masukkan ID Menu   : ");
        String id = input.nextLine();
        System.out.print("Masukkan Nama Menu : ");
        String nama = input.nextLine();
        System.out.print("Masukkan Harga (Rp): ");
        int harga = input.nextInt();
        input.nextLine();

        MenuRestoran menuBaru = null;
        if (jenis == 1) {
            menuBaru = new MenuMakanan(id, nama, harga);
        } else if (jenis == 2) {
            menuBaru = new MenuMinuman(id, nama, harga);
        } else if (jenis == 3) {
            menuBaru = new MenuDessert(id, nama, harga);
        }

        if (menuBaru != null) {
            daftarMenu.add(menuBaru);
            System.out.println("-> Data menu berhasil disimpan!");
        } else {
            System.out.println("-> Jenis menu tidak valid!");
        }
    }

    // 2. Method Input Data Pegawai (Bagian Fadhil)
    public static void inputDataPegawai() {
        System.out.println("\n--- Pilih Jabatan Pegawai ---");
        System.out.println("1. Chef (Juru Masak)");
        System.out.println("2. Pelayan (Waiter)");
        System.out.println("3. Kasir");
        System.out.print("Pilihan (1-3): ");
        int jenis = input.nextInt();
        input.nextLine();

        System.out.print("Masukkan ID Pegawai   : ");
        String id = input.nextLine();
        System.out.print("Masukkan Nama Pegawai : ");
        String nama = input.nextLine();
        System.out.print("Masukkan Shift Kerja  : ");
        String shift = input.nextLine();

        Pegawai pegawaiBaru = null;
        if (jenis == 1) {
            pegawaiBaru = new Chef(id, nama, shift);
        } else if (jenis == 2) {
            pegawaiBaru = new Pelayan(id, nama, shift);
        } else if (jenis == 3) {
            pegawaiBaru = new Kasir(id, nama, shift);
        }

        if (pegawaiBaru != null) {
            daftarPegawai.add(pegawaiBaru);
            System.out.println("-> Data pegawai berhasil disimpan!");
        } else {
            System.out.println("-> Pilihan jabatan tidak valid!");
        }
    }

    // 3. Method Input Data Pesanan (Bagian Aldo)
    public static void inputDataPesanan() {
        System.out.println("\n--- Pilih Jenis Layanan Pesanan ---");
        System.out.println("1. Pesanan Dine-In (Makan di Tempat)");
        System.out.println("2. Pesanan Take-Away (Bungkus)");
        System.out.println("3. Pesanan Delivery (Pesan Antar)");
        System.out.print("Pilihan (1-3): ");
        int jenis = input.nextInt();
        input.nextLine();

        System.out.print("Masukkan ID Pesanan     : ");
        String id = input.nextLine();
        System.out.print("Masukkan Nama Pelanggan : ");
        String pelanggan = input.nextLine();
        System.out.print("Masukkan Total Harga(Rp): ");
        int total = input.nextInt();
        input.nextLine();

        Pesanan pesananBaru = null;
        if (jenis == 1) {
            pesananBaru = new PesananDineIn(id, pelanggan, total);
        } else if (jenis == 2) {
            pesananBaru = new PesananTakeAway(id, pelanggan, total);
        } else if (jenis == 3) {
            pesananBaru = new PesananDelivery(id, pelanggan, total);
        }

        if (pesananBaru != null) {
            daftarPesanan.add(pesananBaru);
            System.out.println("-> Data pesanan berhasil disimpan!");
        } else {
            System.out.println("-> Jenis pesanan tidak valid!");
        }
    }

    // 4. Method Tampilkan Semua Data (Bukti Polymorphism)
    public static void tampilkanSemuaData() {
        System.out.println("\n================ DAFTAR MENU RESTORAN ================");
        if (daftarMenu.isEmpty()) {
            System.out.println("(Belum ada data menu)");
        } else {
            for (MenuRestoran m : daftarMenu) {
                m.tampilkanData();
                m.tampilkanAktivitas();
                System.out.println("------------------------------------------------------");
            }
        }

        System.out.println("\n=============== DAFTAR PEGAWAI RESTORAN ==============");
        if (daftarPegawai.isEmpty()) {
            System.out.println("(Belum ada data pegawai)");
        } else {
            for (Pegawai p : daftarPegawai) {
                p.tampilkanData();
                p.tampilkanAktivitas();
                System.out.println("------------------------------------------------------");
            }
        }

        System.out.println("\n=============== DAFTAR PESANAN PELANGGAN =============");
        if (daftarPesanan.isEmpty()) {
            System.out.println("(Belum ada data pesanan)");
        } else {
            for (Pesanan ps : daftarPesanan) {
                ps.tampilkanData();
                ps.tampilkanAktivitas();
                System.out.println("------------------------------------------------------");
            }
        }
    }

    // 5. Method Ubah Data Menggunakan Setter (Encapsulation)
    public static void ubahData() {
        System.out.println("\n--- Pilih Kategori Data yang Ingin Diubah ---");
        System.out.println("1. Ubah Data Menu");
        System.out.println("2. Ubah Data Pegawai");
        System.out.println("3. Ubah Data Pesanan");
        System.out.print("Pilihan (1-3): ");
        int kat = input.nextInt();
        input.nextLine();

        if (kat == 1) {
            System.out.print("Masukkan ID Menu yang ingin diubah: ");
            String cariId = input.nextLine();
            for (MenuRestoran m : daftarMenu) {
                if (m.getIdMenu().equalsIgnoreCase(cariId)) {
                    System.out.print("Nama Menu Baru  : ");
                    m.setNamaMenu(input.nextLine());
                    System.out.print("Harga Baru (Rp) : ");
                    m.setHarga(input.nextInt());
                    input.nextLine();
                    System.out.println("-> Data menu berhasil diperbarui!");
                    return;
                }
            }
            System.out.println("-> ID Menu tidak ditemukan.");
        } else if (kat == 2) {
            System.out.print("Masukkan ID Pegawai yang ingin diubah: ");
            String cariId = input.nextLine();
            for (Pegawai p : daftarPegawai) {
                if (p.getIdPegawai().equalsIgnoreCase(cariId)) {
                    System.out.print("Nama Pegawai Baru : ");
                    p.setNamaPegawai(input.nextLine());
                    System.out.print("Shift Kerja Baru  : ");
                    p.setShiftKerja(input.nextLine());
                    System.out.println("-> Data pegawai berhasil diperbarui!");
                    return;
                }
            }
            System.out.println("-> ID Pegawai tidak ditemukan.");
        } else if (kat == 3) {
            System.out.print("Masukkan ID Pesanan yang ingin diubah: ");
            String cariId = input.nextLine();
            for (Pesanan ps : daftarPesanan) {
                if (ps.getIdPesanan().equalsIgnoreCase(cariId)) {
                    System.out.print("Nama Pelanggan Baru : ");
                    ps.setNamaPelanggan(input.nextLine());
                    System.out.print("Total Harga Baru(Rp): ");
                    ps.setTotalHarga(input.nextInt());
                    input.nextLine();
                    System.out.println("-> Data pesanan berhasil diperbarui!");
                    return;
                }
            }
            System.out.println("-> ID Pesanan tidak ditemukan.");
        }
    }
}
