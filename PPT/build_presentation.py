# -*- coding: utf-8 -*-
"""
Script to generate Presentasi_SistemInformasiRestoran_Kelompok2.pptx
UTS PBO Kelas A Kelompok 2 - Universitas Muhammadiyah Semarang
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # blank layout

    # Colors
    C_NAVY = RGBColor(15, 30, 54)        # #0F1E36
    C_NAVY_LIGHT = RGBColor(26, 44, 76)  # #1A2C4C
    C_BLUE = RGBColor(37, 99, 235)       # #2563EB
    C_GOLD = RGBColor(217, 119, 6)       # #D97706
    C_GOLD_LIGHT = RGBColor(254, 243, 199) # #FEF3C7
    C_BG = RGBColor(248, 250, 252)       # #F8FAFC
    C_WHITE = RGBColor(255, 255, 255)
    C_DARK = RGBColor(30, 41, 59)        # #1E293B
    C_MUTED = RGBColor(100, 116, 139)    # #64748B
    C_CARD_BORDER = RGBColor(226, 232, 240)
    C_GREEN = RGBColor(16, 185, 129)
    C_RED = RGBColor(239, 68, 68)

    def add_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, dark=False):
        # Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(3.2), Inches(0.35))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_BLUE if dark else RGBColor(224, 231, 255)
        badge.line.fill.background()
        tf = badge.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = category.upper()
        run.font.name = "Segoe UI"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = C_WHITE if dark else C_BLUE

        # Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = tb.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        run_t = p_t.add_run()
        run_t.text = title
        run_t.font.name = "Segoe UI"
        run_t.font.size = Pt(22)
        run_t.font.bold = True
        run_t.font.color.rgb = C_WHITE if dark else C_NAVY

    def add_card(slide, left, top, width, height, bg_color=C_WHITE, border_color=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, C_NAVY)

    # Accent decorative bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(0.15), Inches(4.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_GOLD
    bar.line.fill.background()

    # Title box
    tb = s1.shapes.add_textbox(Inches(1.2), Inches(0.9), Inches(10.5), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    r0 = p0.add_run()
    r0.text = "LAPORAN PROJECT UJIAN TENGAH SEMESTER (UTS) | PBO 2026/2027\n"
    r0.font.name = "Segoe UI"
    r0.font.size = Pt(12)
    r0.font.bold = True
    r0.font.color.rgb = C_GOLD

    p1 = tf.add_paragraph()
    r1 = p1.add_run()
    r1.text = "Sistem Informasi Restoran"
    r1.font.name = "Segoe UI"
    r1.font.size = Pt(36)
    r1.font.bold = True
    r1.font.color.rgb = C_WHITE

    p2 = tf.add_paragraph()
    r2 = p2.add_run()
    r2.text = "Pengembangan Aplikasi Manajemen Restoran Berbasis Object-Oriented Programming (Java)"
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(16)
    r2.font.color.rgb = RGBColor(203, 213, 225)

    # UNIMUS Logo if available
    logo_path = 'presentation_assets/image1.png'
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(10.8), Inches(1.0), width=Inches(1.7))

    # Team Card at bottom
    add_card(s1, Inches(0.8), Inches(5.0), Inches(11.733), Inches(1.8), bg_color=C_NAVY_LIGHT, border_color=RGBColor(51, 65, 85))
    tb_team = s1.shapes.add_textbox(Inches(1.0), Inches(5.1), Inches(11.3), Inches(1.6))
    tf_team = tb_team.text_frame
    tf_team.word_wrap = True
    
    pt0 = tf_team.paragraphs[0]
    rt0 = pt0.add_run()
    rt0.text = "KELOMPOK 2 - KELAS A | TEKNOLOGI INFORMASI - FTIK UNIMUS"
    rt0.font.name = "Segoe UI"
    rt0.font.size = Pt(11)
    rt0.font.bold = True
    rt0.font.color.rgb = C_GOLD

    pt1 = tf_team.add_paragraph()
    rt1 = pt1.add_run()
    rt1.text = "1. Fadhil Anshor (13242520005) - Modul Pegawai  |  2. Aldo Prawiro Akbar (13242520007) - Modul Pesanan  |  3. Zhafirah Haya Destiani (13242520008) - Modul Menu"
    rt1.font.name = "Segoe UI"
    rt1.font.size = Pt(13)
    rt1.font.bold = True
    rt1.font.color.rgb = C_WHITE

    pt2 = tf_team.add_paragraph()
    rt2 = pt2.add_run()
    rt2.text = "Dosen Pengampu: Mata Kuliah Pemrograman Berorientasi Objek | Universitas Muhammadiyah Semarang"
    rt2.font.name = "Segoe UI"
    rt2.font.size = Pt(11)
    rt2.font.color.rgb = RGBColor(148, 163, 184)

    s1.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE - PEMBUKAAN (Fadhil Anshor):\n"
        "Assalamu'alaikum Warahmatullahi Wabarakatuh. Selamat pagi/siang kepada Bapak/Ibu Dosen Pengampu mata kuliah Pemrograman Berorientasi Objek dan rekan-rekan mahasiswa sekalian.\n"
        "Kami dari Kelompok 2 Kelas A yang beranggotakan: saya sendiri Fadhil Anshor, rekan saya Aldo Prawiro Akbar, dan Zhafirah Haya Destiani.\n"
        "Pada kesempatan kali ini, kami akan mempresentasikan hasil proyek UTS PBO kami yang berjudul: 'Pengembangan Aplikasi Sistem Informasi Restoran Berbasis Object Oriented Programming Menggunakan Java'."
    )

    # =========================================================================
    # SLIDE 2: AGENDA PRESENTASI
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2, C_BG)
    add_header(s2, "Rencana Paparan", "Agenda Presentasi Proyek UTS")

    agendas = [
        ("01", "Latar Belakang & Masalah", "Kebutuhan otomatisasi dan masalah human error operasional restoran."),
        ("02", "Ruang Lingkup & Arsitektur", "Pengelolaan 3 pilar: Menu, Pegawai, Pesanan dengan 14 Class Java."),
        ("03", "Diagram Pemodelan UML", "Analisis sistem melalui Class, Use Case, Sequence, & Activity Diagram."),
        ("04", "Penerapan 5 Pilar OOP", "Bukti kode: Class/Object, Encapsulation, Inheritance, Polymorphism, Abstraction."),
        ("05", "Demo Eksekusi Program", "Pengujian 6 fitur menu CLI, input data, update ID, & output polimorfik."),
        ("06", "Kendala & Kesimpulan", "Troubleshooting buffer Scanner, sinkronisasi tim, dan saran ekspansi.")
    ]

    for i, (num, title, desc) in enumerate(agendas):
        row = i // 3
        col = i % 3
        l = Inches(0.8 + col * 4.0)
        t = Inches(1.8 + row * 2.5)
        w = Inches(3.7)
        h = Inches(2.2)

        add_card(s2, l, t, w, h)
        # Number badge
        nb = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l + Inches(0.2), t + Inches(0.2), Inches(0.7), Inches(0.4))
        nb.fill.solid()
        nb.fill.fore_color.rgb = C_BLUE
        nb.line.fill.background()
        nb.text_frame.paragraphs[0].text = num
        nb.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        nb.text_frame.paragraphs[0].runs[0].font.name = "Segoe UI"
        nb.text_frame.paragraphs[0].runs[0].font.size = Pt(13)
        nb.text_frame.paragraphs[0].runs[0].font.bold = True
        nb.text_frame.paragraphs[0].runs[0].font.color.rgb = C_WHITE

        # Text
        tb = s2.shapes.add_textbox(l + Inches(0.2), t + Inches(0.7), w - Inches(0.4), h - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        r1 = p1.add_run()
        r1.text = title
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(14)
        r1.font.bold = True
        r1.font.color.rgb = C_NAVY

        p2 = tf.add_paragraph()
        r2 = p2.add_run()
        r2.text = desc
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(11)
        r2.font.color.rgb = C_MUTED

    s2.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor):\n"
        "Untuk mempermudah pemahaman Bapak/Ibu dosen dan rekan-rekan sekalian, presentasi kami bagi menjadi 6 agenda utama: diawali latar belakang masalah, ruang lingkup arsitektur sistem, pemodelan UML, pembuktian 5 pilar OOP pada kode, demonstrasi aplikasi, dan ditutup kendala serta kesimpulan."
    )

    # =========================================================================
    # SLIDE 3: LATAR BELAKANG & MASALAH
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3, C_BG)
    add_header(s3, "Pendahuluan", "Latar Belakang & Urgensi Sistem")

    # Card Kiri: Masalah Konvensional
    add_card(s3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_l = s3.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    r = p.add_run()
    r.text = "Tantangan Operasional Restoran"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_RED

    points_masalah = [
        ("Kompleksitas 3 Pilar Operasional:", "Restoran harus menyinkronkan data katalog menu, jadwal staf kerja, dan transaksi pesanan setiap hari."),
        ("Tingginya Risiko Human Error:", "Pencatatan manual atau kode linier rentan salah harga, kekeliruan pesanan meja/delivery, dan jadwal shift bentrok."),
        ("Data Statis & Tidak Fleksibel:", "Sistem tanpa struktur OOP sulit diperluas ketika restoran menambah variasi hidangan baru atau tipe layanan pengantaran."),
        ("Ketiadaan Enkapsulasi Keamanan:", "Perubahan data krusial seperti harga dan total tagihan rawan dimodifikasi sembarangan tanpa validasi method.")
    ]
    for h, b in points_masalah:
        p_item = tf_l.add_paragraph()
        p_item.space_before = Pt(8)
        r_h = p_item.add_run()
        r_h.text = f"• {h} "
        r_h.font.bold = True
        r_h.font.size = Pt(12)
        r_h.font.color.rgb = C_NAVY
        r_b = p_item.add_run()
        r_b.text = b
        r_b.font.size = Pt(11)
        r_b.font.color.rgb = C_MUTED

    # Card Kanan: Solusi Pendekatan OOP
    add_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_r = s3.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    r = p.add_run()
    r.text = "Solusi Melalui Paradigma OOP"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_GREEN

    points_solusi = [
        ("Modularitas Kelas Terisolasi:", "Setiap entitas bisnis (Menu, Pegawai, Pesanan) dimodelkan secara independen dan terorganisir."),
        ("Enkapsulasi Data Sensitif:", "Atribut dibuat 'private' dengan akses terbatas melalui method getter & setter publik demi integritas data."),
        ("Inheritance & Code Reusability:", "Subclass mewarisi logika dasar parent class tanpa menduplikasi kode baris program."),
        ("Polymorphism Dinamis:", "Penyajian informasi yang fleksibel saat runtime berdasarkan tipe objek sebenarnya."),
        ("Standarisasi via Interface:", "Kontrak method bersama menjamin keseragaman fungsi layanan di seluruh level sistem.")
    ]
    for h, b in points_solusi:
        p_item = tf_r.add_paragraph()
        p_item.space_before = Pt(8)
        r_h = p_item.add_run()
        r_h.text = f"• {h} "
        r_h.font.bold = True
        r_h.font.size = Pt(12)
        r_h.font.color.rgb = C_NAVY
        r_b = p_item.add_run()
        r_b.text = b
        r_b.font.size = Pt(11)
        r_b.font.color.rgb = C_MUTED

    s3.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor):\n"
        "Mengapa sistem ini penting? Operasional restoran harian melibatkan 3 pilar yang saling terhubung: menu makanan-minuman, pegawai yang bertugas, dan transaksi pelanggan.\n"
        "Bila dikelola secara konvensional, potensi kesalahan pesanan dan salah harga sangat besar. Melalui OOP berbasis Java, kami mentransformasikan proses ini menjadi arsitektur perangkat lunak yang modular, aman, dan mudah dikembangkan di masa depan."
    )

    # =========================================================================
    # SLIDE 4: TUJUAN & RUANG LINGKUP SISTEM
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4, C_BG)
    add_header(s4, "Spesifikasi Proyek", "Tujuan Praktikum & Ruang Lingkup Sistem")

    tujuan_cards = [
        ("PILAR MENU", "Zhafirah Haya Destiani", C_GOLD, [
            "Mengelola katalog hidangan restoran secara terstruktur.",
            "3 Kategori: Makanan Utama, Minuman Segar, dan Dessert.",
            "Mencakup ID, Nama Menu, Harga, dan format penyajian unik."
        ]),
        ("PILAR PEGAWAI", "Fadhil Anshor", C_BLUE, [
            "Mengelola manajemen sumber daya manusia restoran.",
            "3 Peran: Chef (Dapur), Pelayan (Meja), dan Kasir (Transaksi).",
            "Mencakup ID Pegawai, Nama, Shift Kerja, dan rincian tugas spesifik."
        ]),
        ("PILAR PESANAN", "Aldo Prawiro Akbar", C_GREEN, [
            "Mencatat seluruh transaksi pesanan pelanggan secara realtime.",
            "3 Saluran: Makan di Tempat (Dine-In), Dibungkus (Take-Away), dan Pesan Antar (Delivery).",
            "Menghitung total tagihan dan status layanan operasional."
        ])
    ]

    for i, (title, pj, col, pts) in enumerate(tujuan_cards):
        l = Inches(0.8 + i * 4.0)
        t = Inches(1.8)
        w = Inches(3.7)
        h = Inches(5.0)

        add_card(s4, l, t, w, h)
        # Top banner on card
        top_b = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, Inches(0.9))
        top_b.fill.solid()
        top_b.fill.fore_color.rgb = col
        top_b.line.fill.background()
        tf_b = top_b.text_frame
        tf_b.word_wrap = True
        p1 = tf_b.paragraphs[0]
        p1.alignment = PP_ALIGN.CENTER
        r1 = p1.add_run()
        r1.text = title
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(14)
        r1.font.bold = True
        r1.font.color.rgb = C_WHITE

        p2 = tf_b.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        r2 = p2.add_run()
        r2.text = f"PJ: {pj}"
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(10)
        r2.font.color.rgb = RGBColor(254, 243, 199)

        # Body
        tb = s4.shapes.add_textbox(l + Inches(0.2), t + Inches(1.1), w - Inches(0.4), h - Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        for pt in pts:
            p = tf.add_paragraph()
            p.space_before = Pt(12)
            r = p.add_run()
            r.text = f"✓ {pt}"
            r.font.name = "Segoe UI"
            r.font.size = Pt(12)
            r.font.color.rgb = C_DARK

    s4.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor):\n"
        "Sistem kami membagi operasional restoran ke dalam 3 modul spesifik dengan penanggung jawab masing-masing. Saudari Zhafirah bertanggung jawab pada pilar katalog Menu, saya sendiri pada pilar manajemen Pegawai, dan saudara Aldo bertanggung jawab pada pilar pencatatan Pesanan transaksi."
    )

    # =========================================================================
    # SLIDE 5: STRUKTUR CLASS & ARSITEKTUR TIM (14 CLASS)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5, C_BG)
    add_header(s5, "Arsitektur Kode", "Struktur 14 File Java & Pembagian Modul Tim")

    # Table of 14 Classes
    add_card(s5, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.0))
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(4.6))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "Komposisi 14 File .java Berdasarkan Standar Proyek Kelompok (3 Anggota)"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    class_info = [
        ("1. Interface Bersama", "LayananRestoran.java", "Kontrak method tampilkanAktivitas(): void untuk seluruh entitas restoran.", "Tim"),
        ("2. Modul Menu", "MenuRestoran.java (Parent Abstract)", "Turunan: MenuMakanan.java, MenuMinuman.java, MenuDessert.java (3 Subclass).", "Zhafirah Haya D."),
        ("3. Modul Pegawai", "Pegawai.java (Parent Abstract)", "Turunan: Chef.java, Pelayan.java, Kasir.java (3 Subclass).", "Fadhil Anshor"),
        ("4. Modul Pesanan", "Pesanan.java (Parent Abstract)", "Turunan: PesananDineIn.java, PesananTakeAway.java, PesananDelivery.java (3 Subclass).", "Aldo Prawiro A."),
        ("5. Controller Utama", "Main.java", "Mengelola 3 koleksi ArrayList dinamis, navigasi 6 opsi menu CLI, dan error handling Scanner.", "Tim")
    ]

    for cat, file_n, desc, pj in class_info:
        p_row = tf.add_paragraph()
        p_row.space_before = Pt(8)
        r_c = p_row.add_run()
        r_c.text = f"• [{cat}] "
        r_c.font.bold = True
        r_c.font.size = Pt(12)
        r_c.font.color.rgb = C_BLUE

        r_f = p_row.add_run()
        r_f.text = f"{file_n} — "
        r_f.font.bold = True
        r_f.font.size = Pt(12)
        r_f.font.color.rgb = C_NAVY

        r_d = p_row.add_run()
        r_d.text = f"{desc} "
        r_d.font.size = Pt(11)
        r_d.font.color.rgb = C_MUTED

        r_p = p_row.add_run()
        r_p.text = f"(Penanggung Jawab: {pj})"
        r_p.font.bold = True
        r_p.font.size = Pt(11)
        r_p.font.color.rgb = C_GOLD

    s5.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor -> serah terima ke Zhafirah):\n"
        "Sesuai pedoman tugas proyek UTS, sistem kami terdiri dari tepat 14 file Java: 1 Interface bersama, 3 Abstract Parent Class, 9 Child Class (3 per modul), dan 1 Main Class.\n"
        "Selanjutnya, untuk pembahasan pemodelan UML Diagram dan Modul Menu, akan disampaikan oleh rekan saya, saudari Zhafirah Haya Destiani. Kepada Zhafirah, dipersilakan."
    )

    # =========================================================================
    # SLIDE 6: UML - CLASS DIAGRAM
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6, C_BG)
    add_header(s6, "Pemodelan Sistem (UML)", "Class Diagram: Relasi Antar 14 Entitas Program")

    # Image Left
    cd_path = 'Diagram/Class Diagram.png'
    if os.path.exists(cd_path):
        s6.shapes.add_picture(cd_path, Inches(0.8), Inches(1.8), width=Inches(7.2))

    # Notes Card Right
    add_card(s6, Inches(8.2), Inches(1.8), Inches(4.3), Inches(5.0))
    tb_cd = s6.shapes.add_textbox(Inches(8.4), Inches(2.0), Inches(3.9), Inches(4.5))
    tf_cd = tb_cd.text_frame
    tf_cd.word_wrap = True

    p = tf_cd.paragraphs[0]
    r = p.add_run()
    r.text = "Analisis Hubungan Relasi OOP"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    cd_pts = [
        ("Realization (<<implements>>):", "Ketiga abstract class (MenuRestoran, Pegawai, Pesanan) mengimplementasikan interface LayananRestoran."),
        ("Generalization (<<extends>>):", "Masing-masing 3 child class mewarisi atribut dan method dari parent class abstraknya."),
        ("Dependency (<<uses>>):", "Class Main bergantung pada MenuRestoran, Pegawai, dan Pesanan melalui ArrayList dinamis."),
        ("Enkapsulasi Ketat:", "Seluruh atribut bertanda '-' (private), hanya bisa diakses lewat method '+' (public getter/setter).")
    ]
    for h, b in cd_pts:
        p_item = tf_cd.add_paragraph()
        p_item.space_before = Pt(8)
        r_h = p_item.add_run()
        r_h.text = f"• {h} "
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = C_BLUE
        r_b = p_item.add_run()
        r_b.text = b
        r_b.font.size = Pt(10)
        r_b.font.color.rgb = C_MUTED

    s6.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Zhafirah Haya Destiani):\n"
        "Terima kasih Fadhil. Pada layar dapat kita lihat Class Diagram resmi dari sistem informasi restoran kami.\n"
        "Di posisi teratas terdapat Interface LayananRestoran yang direalisasikan oleh ketiga parent class abstrak: MenuRestoran, Pegawai, dan Pesanan.\n"
        "Masing-masing parent memiliki 3 subclass turunan dengan relasi pewarisan (inheritance). Semua atribut private dienkapsulasi dan dimanipulasi secara polimorfik oleh Main Class menggunakan ArrayList."
    )

    # =========================================================================
    # SLIDE 7: UML - USE CASE DIAGRAM
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7, C_BG)
    add_header(s7, "Pemodelan Sistem (UML)", "Use Case Diagram: Interaksi Fungsional Pengguna")

    uc_path = 'Diagram/Use Case Diagram.png'
    if os.path.exists(uc_path):
        s7.shapes.add_picture(uc_path, Inches(0.8), Inches(1.8), width=Inches(6.8))

    add_card(s7, Inches(7.8), Inches(1.8), Inches(4.7), Inches(5.0))
    tb_uc = s7.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.3), Inches(4.5))
    tf_uc = tb_uc.text_frame
    tf_uc.word_wrap = True

    p = tf_uc.paragraphs[0]
    r = p.add_run()
    r.text = "Aktor & 6 Fungsionalitas Utama"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    uc_pts = [
        ("Aktor Sistem:", "Pengguna / Admin Kasir Restoran yang berinteraksi langsung dengan konsol CLI."),
        ("Input Data (dengan relasi <<extend>>):", "Input Menu (Makanan/Minuman/Dessert), Input Pegawai (Chef/Pelayan/Kasir), Input Pesanan (Dine-In/Take-Away/Delivery)."),
        ("Tampilkan Semua Data:", "Menampilkan seluruh entitas tersimpan secara polimorfik dalam satu waktu."),
        ("Ubah Data (Update by ID):", "Pencarian data berdasarkan ID unik dan pengubahan nilai atribut melalui setter."),
        ("Keluar Sistem:", "Menutup sesi eksekusi aplikasi dengan aman.")
    ]
    for h, b in uc_pts:
        p_item = tf_uc.add_paragraph()
        p_item.space_before = Pt(8)
        r_h = p_item.add_run()
        r_h.text = f"• {h} "
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = C_BLUE
        r_b = p_item.add_run()
        r_b.text = b
        r_b.font.size = Pt(10)
        r_b.font.color.rgb = C_MUTED

    s7.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Zhafirah Haya Destiani -> serah terima ke Aldo):\n"
        "Use Case Diagram ini memodelkan interaksi Aktor (Admin Kasir) dengan sistem. Terdapat 6 use case utama. Pada fitur input data, kami menerapkan relasi <<extend>> yang mencerminkan percabangan kategori spesifik pada masing-masing modul.\n"
        "Selanjutnya untuk alur Sequence Diagram dan Activity Diagram, akan dipaparkan oleh rekan saya Aldo Prawiro Akbar."
    )

    # =========================================================================
    # SLIDE 8: UML - ACTIVITY DIAGRAM
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8, C_BG)
    add_header(s8, "Pemodelan Alur Kerja (UML)", "Activity Diagram: 4 Swimlane Alur Eksekusi")

    act_path = 'Diagram/Activity Diagram.png'
    if os.path.exists(act_path):
        s8.shapes.add_picture(act_path, Inches(0.8), Inches(1.8), width=Inches(7.2))

    add_card(s8, Inches(8.2), Inches(1.8), Inches(4.3), Inches(5.0))
    tb_act = s8.shapes.add_textbox(Inches(8.4), Inches(2.0), Inches(3.9), Inches(4.5))
    tf_act = tb_act.text_frame
    tf_act.word_wrap = True

    p = tf_act.paragraphs[0]
    r = p.add_run()
    r.text = "Pemodelan 4 Swimlane"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    act_pts = [
        ("1. Swimlane Pengguna:", "Memulai aplikasi, memasukkan angka pilihan menu, dan menginput parameter objek."),
        ("2. Swimlane Main:", "Mengontrol alur looping do-while, memvalidasi menu, dan memanggil controller."),
        ("3. Swimlane LayananRestoran:", "Menjalankan kontrak interface metode tampilkanAktivitas()."),
        ("4. Swimlane Kelas Terkait:", "Instansiasi subclass spesifik dan penyimpanan ke dalam ArrayList dinamis.")
    ]
    for h, b in act_pts:
        p_item = tf_act.add_paragraph()
        p_item.space_before = Pt(10)
        r_h = p_item.add_run()
        r_h.text = f"{h}\n"
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = C_BLUE
        r_b = p_item.add_run()
        r_b.text = b
        r_b.font.size = Pt(10)
        r_b.font.color.rgb = C_MUTED

    s8.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Aldo Prawiro Akbar):\n"
        "Terima kasih Zhafirah. Pada Activity Diagram ini, alur kerja kami petakan secara rapi ke dalam 4 swimlane: Pengguna, Main, LayananRestoran, dan Kelas Terkait.\n"
        "Ketika pengguna memilih aksi, sistem mengevaluasi percabangan decision node, meneruskan data ke objek yang relevan, dan menyajikannya kembali ke layar konsol hingga mencapai Finish Node saat memilih menu Keluar."
    )

    # =========================================================================
    # SLIDE 9: UML - SEQUENCE DIAGRAM
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9, C_BG)
    add_header(s9, "Pemodelan Waktu & Pesan (UML)", "Sequence Diagram: Komunikasi Objek Berdasarkan Waktu")

    seq_path = 'Diagram/Sequence Diagram.png'
    if os.path.exists(seq_path):
        s9.shapes.add_picture(seq_path, Inches(0.8), Inches(1.8), width=Inches(7.2))

    add_card(s9, Inches(8.2), Inches(1.8), Inches(4.3), Inches(5.0))
    tb_seq = s9.shapes.add_textbox(Inches(8.4), Inches(2.0), Inches(3.9), Inches(4.5))
    tf_seq = tb_seq.text_frame
    tf_seq.word_wrap = True

    p = tf_seq.paragraphs[0]
    r = p.add_run()
    r.text = "4 Skenario Komunikasi Objek"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    seq_pts = [
        ("Skenario 1: Input Data:", "Pengguna -> Main -> new SubClass() -> ArrayList.add(). Objek baru terdaftar di memori."),
        ("Skenario 2: Tampilkan Data:", "Main melakukan loop pada ArrayList, memanggil tampilkanData() dan tampilkanAktivitas() secara polimorfik."),
        ("Skenario 3: Ubah Data:", "Pencarian objek berdasarkan ID -> Main memanggil setter (setNama, setHarga, setShift, setTotal) secara dinamis."),
        ("Skenario 4: Respon Kembali:", "Seluruh nilai konfirmasi pembaruan dikembalikan ke layar Pengguna.")
    ]
    for h, b in seq_pts:
        p_item = tf_seq.add_paragraph()
        p_item.space_before = Pt(8)
        r_h = p_item.add_run()
        r_h.text = f"• {h} "
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = C_BLUE
        r_b = p_item.add_run()
        r_b.text = b
        r_b.font.size = Pt(10)
        r_b.font.color.rgb = C_MUTED

    s9.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Aldo Prawiro Akbar):\n"
        "Sequence Diagram ini membuktikan runtutan pengiriman pesan antar objek. Dapat dilihat bahwa objek diinstansiasi secara dinamis, ditambahkan ke ArrayList, dan saat proses update, objek dicari lalu dimodifikasi melalui method setter yang tepat."
    )

    # =========================================================================
    # SLIDE 10: PILAR OOP 1 & 2: CLASS/OBJECT & ENCAPSULATION
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10, C_BG)
    add_header(s10, "5 Pilar Utama OOP", "Pilar 1 & 2: Class, Object, dan Encapsulation")

    # Card Kiri: Class & Object
    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_co = s10.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_co = tb_co.text_frame
    tf_co.word_wrap = True
    p = tf_co.paragraphs[0]
    r = p.add_run()
    r.text = "1. Class & Object"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_BLUE

    co_desc = (
        "• Konsep: Class adalah cetak biru (blueprint), sedangkan Object adalah instansiasi nyata di memori menggunakan kata kunci 'new'.\n\n"
        "• Bukti Implementasi Kode:\n"
        "  daftarMenu.add(new MenuMakanan(id, nama, harga));\n"
        "  daftarPegawai.add(new Chef(id, nama, shift));\n"
        "  daftarPesanan.add(new PesananDineIn(id, nama, total));\n\n"
        "• Manfaat: Data setiap transaksi dan entitas restoran disimpan sebagai entitas mandiri yang memiliki state dan behavior tersendiri di dalam ArrayList."
    )
    p2 = tf_co.add_paragraph()
    p2.space_before = Pt(10)
    r2 = p2.add_run()
    r2.text = co_desc
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(11)
    r2.font.color.rgb = C_DARK

    # Card Kanan: Encapsulation
    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_enc = s10.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_enc = tb_enc.text_frame
    tf_enc.word_wrap = True
    p = tf_enc.paragraphs[0]
    r = p.add_run()
    r.text = "2. Encapsulation (Enkapsulasi)"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_GOLD

    enc_desc = (
        "• Konsep: Memproteksi data sensitif dari modifikasi langsung di luar class dengan modifier 'private'. Akses hanya dibuka melalui Getter & Setter 'public'.\n\n"
        "• Bukti Implementasi Kode:\n"
        "  private String idPesanan;\n"
        "  private String namaPelanggan;\n"
        "  private int totalHarga;\n\n"
        "  public String getNamaPelanggan() { return namaPelanggan; }\n"
        "  public void setTotalHarga(int totalHarga) { this.totalHarga = totalHarga; }\n\n"
        "• Manfaat: Menjamin integritas data saat operasi 'Ubah Data' (Menu 5), mencegah manipulasi data secara tidak sengaja atau tidak sah."
    )
    p3 = tf_enc.add_paragraph()
    p3.space_before = Pt(10)
    r3 = p3.add_run()
    r3.text = enc_desc
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(11)
    r3.font.color.rgb = C_DARK

    s10.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor):\n"
        "Memasuki pembuktian 5 Pilar OOP: Pertama, Class & Object kami terapkan dengan mendefinisikan class cetak biru dan menginstansiasinya secara nyata menggunakan kata kunci new ke dalam ArrayList.\n"
        "Kedua, Enkapsulasi kami terapkan 100% pada seluruh parent class (MenuRestoran, Pegawai, Pesanan). Semua atribut dilindungi dengan modifier private, dan pembacaan atau pengubahan data wajib melalui method Getter dan Setter."
    )

    # =========================================================================
    # SLIDE 11: PILAR OOP 3: INHERITANCE (PEWARISAN)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11, C_BG)
    add_header(s11, "5 Pilar Utama OOP", "Pilar 3: Inheritance (Pewarisan Sifat Antar Kelas)")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.0))
    tb_inh = s11.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(11.1), Inches(4.5))
    tf_inh = tb_inh.text_frame
    tf_inh.word_wrap = True

    p = tf_inh.paragraphs[0]
    r = p.add_run()
    r.text = "Pewarisan Atribut & Constructor via 'extends' dan 'super(...)'"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_NAVY

    inh_columns = [
        ("Modul MenuRestoran", "MenuMakanan, MenuMinuman, MenuDessert mewarisi atribut idMenu, namaMenu, dan harga dari parent MenuRestoran. Subclass menambahkan spesialisasi tampilan penyajian."),
        ("Modul Pegawai", "Chef, Pelayan, dan Kasir mewarisi atribut idPegawai, namaPegawai, dan shiftKerja dari Pegawai. Setiap subclass mengimplementasikan deskripsi tugas unik masing-masing."),
        ("Modul Pesanan", "PesananDineIn, PesananTakeAway, dan PesananDelivery mewarisi idPesanan, namaPelanggan, dan totalHarga. Masing-masing subclass mendefinisikan tipe layanan dan status penyajiannya.")
    ]

    for col_t, col_b in inh_columns:
        p_c = tf_inh.add_paragraph()
        p_c.space_before = Pt(12)
        r_ct = p_c.add_run()
        r_ct.text = f"• {col_t}: "
        r_ct.font.bold = True
        r_ct.font.size = Pt(13)
        r_ct.font.color.rgb = C_BLUE
        r_cb = p_c.add_run()
        r_cb.text = f"\n  {col_b}"
        r_cb.font.size = Pt(11)
        r_cb.font.color.rgb = C_DARK

    p_super = tf_inh.add_paragraph()
    p_super.space_before = Pt(14)
    r_s = p_super.add_run()
    r_s.text = "Contoh Kode Pewarisan (Chef.java):\npublic class Chef extends Pegawai {\n    public Chef(String id, String nama, String shift) { super(id, nama, shift); }\n}"
    r_s.font.name = "Consolas"
    r_s.font.size = Pt(11)
    r_s.font.bold = True
    r_s.font.color.rgb = C_GOLD

    s11.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Zhafirah Haya Destiani):\n"
        "Pilar ketiga adalah Inheritance atau Pewarisan. Dengan kata kunci 'extends', subclass secara otomatis mewarisi seluruh atribut umum induknya tanpa perlu menulis ulang deklarasi variabel.\n"
        "Pada constructor child class, kata kunci 'super' dipanggil untuk mengisi nilai atribut induk. Ini menghasilkan kode yang sangat bersih, efisien, dan menerapkan prinsip DRY (Don't Repeat Yourself)."
    )

    # =========================================================================
    # SLIDE 12: PILAR OOP 4: POLYMORPHISM (DYNAMIC BINDING)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12, C_BG)
    add_header(s12, "5 Pilar Utama OOP", "Pilar 4: Polymorphism (Dynamic Method Dispatch)")

    # Left: Concept & Loop
    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_pl = s12.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_pl = tb_pl.text_frame
    tf_pl.word_wrap = True
    p = tf_pl.paragraphs[0]
    r = p.add_run()
    r.text = "Dynamic Polymorphism via Override"
    r.font.name = "Segoe UI"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = C_BLUE

    poly_text = (
        "• Satu Perintah, Beragam Perilaku:\n"
        "  Polymorphism memungkinkan objek dari class berbeda diakses melalui satu tipe referensi umum yang sama.\n\n"
        "• Iterasi Polimorfik pada Main.java:\n"
        "  for (Pegawai p : daftarPegawai) {\n"
        "      p.tampilkanData();\n"
        "      p.tampilkanAktivitas();\n"
        "  }\n\n"
        "• Eksekusi Runtime:\n"
        "  Java secara otomatis mengeksekusi method subclass yang sesuai. Jika objeknya Chef, ia menampilkan tugas dapur; jika Kasir, ia menampilkan tugas transaksi meja kasir."
    )
    p2 = tf_pl.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = poly_text
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(11)
    r2.font.color.rgb = C_DARK

    # Right: Output Polymorphic Screenshot
    add_card(s12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_pr = s12.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(0.6))
    tf_pr = tb_pr.text_frame
    p_pr = tf_pr.paragraphs[0]
    r_pr = p_pr.add_run()
    r_pr.text = "Bukti Eksekusi Polimorfisme Konsol"
    r_pr.font.name = "Segoe UI"
    r_pr.font.size = Pt(16)
    r_pr.font.bold = True
    r_pr.font.color.rgb = C_GREEN

    out_poly = 'presentation_assets/image30.png'
    if os.path.exists(out_poly):
        s12.shapes.add_picture(out_poly, Inches(7.0), Inches(2.7), width=Inches(5.3))

    s12.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Aldo Prawiro Akbar):\n"
        "Pilar keempat adalah Polymorphism. Dalam method tampilkanSemuaData() di Main.java, kami melakukan perulangan for-each pada ArrayList daftarPegawai dan daftarPesanan.\n"
        "Meskipun pemanggilannya sama-sama p.tampilkanData(), keluaran di layar otomatis berbeda: Chef mengeluarkan info memasak, Pelayan mengeluarkan info meja pelanggan, dan Kasir mencetak laporan nota pembayaran."
    )

    # =========================================================================
    # SLIDE 13: PILAR OOP 5: ABSTRACTION & INTERFACE
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13, C_BG)
    add_header(s13, "5 Pilar Utama OOP", "Pilar 5: Abstraction & Interface Contract")

    # Card Kiri: Interface
    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_if = s13.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_if = tb_if.text_frame
    tf_if.word_wrap = True
    p = tf_if.paragraphs[0]
    r = p.add_run()
    r.text = "Interface LayananRestoran"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_BLUE

    if_desc = (
        "• Definisi Kontrak Murni:\n"
        "  public interface LayananRestoran {\n"
        "      void tampilkanAktivitas();\n"
        "  }\n\n"
        "• Tujuan Standarisasi:\n"
        "  Menjamin bahwa setiap komponen dalam sistem restoran wajib memiliki method tampilkanAktivitas() untuk merefleksikan perannya dalam melayani pelanggan.\n\n"
        "• Implementasi Seragam:\n"
        "  MenuRestoran, Pegawai, dan Pesanan semuanya mengimplementasikan interface ini, membentuk standar arsitektur yang kokoh."
    )
    p2 = tf_if.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = if_desc
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(11)
    r2.font.color.rgb = C_DARK

    # Card Kanan: Abstract Class
    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_abs = s13.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_abs = tb_abs.text_frame
    tf_abs.word_wrap = True
    p = tf_abs.paragraphs[0]
    r = p.add_run()
    r.text = "3 Abstract Parent Class"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_GOLD

    abs_desc = (
        "• Proteksi Pembuatan Objek Parsial:\n"
        "  Class 'abstract' tidak dapat diinstansiasi langsung (misal: 'new Pegawai()' akan ditolak compiler Java).\n\n"
        "• Method Abstract Wajib Di-override:\n"
        "  - MenuRestoran: getJenisMenu(), tampilkanPenyajian()\n"
        "  - Pegawai: getJabatan(), tampilkanTugas()\n"
        "  - Pesanan: getJenisPesanan(), tampilkanStatusLayanan()\n\n"
        "• Manfaat Arsitektural:\n"
        "  Memaksa seluruh child class untuk memberikan implementasi konkret sesuai spesifikasi bisnis masing-masing."
    )
    p3 = tf_abs.add_paragraph()
    p3.space_before = Pt(8)
    r3 = p3.add_run()
    r3.text = abs_desc
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(11)
    r3.font.color.rgb = C_DARK

    s13.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Zhafirah Haya Destiani):\n"
        "Pilar kelima adalah Abstraction dan Interface. Interface LayananRestoran bertindak sebagai kontrak yang mewajibkan method tampilkanAktivitas().\n"
        "Sementara itu, 3 Parent Class sengaja kami deklarasikan sebagai 'abstract class' sehingga objek yang tidak lengkap tidak bisa diinstansiasi sembarangan. Setiap subclass diwajibkan meng-override method abstract yang telah didefinisikan."
    )

    # =========================================================================
    # SLIDE 14: DEMO PROGRAM 1: MENU UTAMA & INPUT DATA
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14, C_BG)
    add_header(s14, "Pengujian Program", "Hasil Uji Eksekusi: Menu Utama & Input Data CLI")

    # Image 1: Menu Utama
    img_menu = 'presentation_assets/image27.png'
    if os.path.exists(img_menu):
        s14.shapes.add_picture(img_menu, Inches(0.8), Inches(1.8), width=Inches(5.7))

    # Image 2: Input Data
    img_input = 'presentation_assets/image28.png'
    if os.path.exists(img_input):
        s14.shapes.add_picture(img_input, Inches(6.8), Inches(1.8), width=Inches(5.7))

    # Notes under pictures
    tb_n1 = s14.shapes.add_textbox(Inches(0.8), Inches(5.8), Inches(5.7), Inches(1.2))
    tb_n1.text_frame.word_wrap = True
    p1 = tb_n1.text_frame.paragraphs[0]
    r1 = p1.add_run()
    r1.text = "Gambar 1: Tampilan 6 Opsi Menu Utama Konsol CLI\nNavigasi interaktif menggunakan switch-case dan do-while loop."
    r1.font.name = "Segoe UI"
    r1.font.size = Pt(11)
    r1.font.color.rgb = C_NAVY

    tb_n2 = s14.shapes.add_textbox(Inches(6.8), Inches(5.8), Inches(5.7), Inches(1.2))
    tb_n2.text_frame.word_wrap = True
    p2 = tb_n2.text_frame.paragraphs[0]
    r2 = p2.add_run()
    r2.text = "Gambar 2: Proses Input Data Menu, Pegawai, & Pesanan\nInput terenkapsulasi langsung dimasukkan ke koleksi ArrayList dinamis."
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(11)
    r2.font.color.rgb = C_NAVY

    s14.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Aldo Prawiro Akbar):\n"
        "Berikut adalah bukti eksekusi program konsol kami. Pada Gambar 1 terlihat 6 menu utama yang menyambut pengguna.\n"
        "Pada Gambar 2, terlihat proses saat admin memasukkan data Menu Makanan, Pegawai, dan data Pesanan transaksi pelanggan. Sistem membaca input dengan Scanner secara interaktif dan menyimpannya ke dalam memori dinamis."
    )

    # =========================================================================
    # SLIDE 15: DEMO PROGRAM 2: UBAH DATA & TAMPILKAN SEMUA DATA
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_bg(s15, C_BG)
    add_header(s15, "Pengujian Program", "Hasil Uji Eksekusi: Ubah Data (Update) & Output Polimorfisme")

    # Image 3: Ubah Data
    img_ubah = 'presentation_assets/image29.png'
    if os.path.exists(img_ubah):
        s15.shapes.add_picture(img_ubah, Inches(0.8), Inches(1.8), width=Inches(5.7))

    # Image 4: Tampilkan Semua Data
    img_tampil = 'presentation_assets/image30.png'
    if os.path.exists(img_tampil):
        s15.shapes.add_picture(img_tampil, Inches(6.8), Inches(1.8), width=Inches(5.7))

    tb_n3 = s15.shapes.add_textbox(Inches(0.8), Inches(5.8), Inches(5.7), Inches(1.2))
    tb_n3.text_frame.word_wrap = True
    p3 = tb_n3.text_frame.paragraphs[0]
    r3 = p3.add_run()
    r3.text = "Gambar 3: Fitur Ubah Data (*Update by ID*)\nPencarian ID objek dan pemanggilan setter untuk memperbarui atribut."
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(11)
    r3.font.color.rgb = C_NAVY

    tb_n4 = s15.shapes.add_textbox(Inches(6.8), Inches(5.8), Inches(5.7), Inches(1.2))
    tb_n4.text_frame.word_wrap = True
    p4 = tb_n4.text_frame.paragraphs[0]
    r4 = p4.add_run()
    r4.text = "Gambar 4: Tampilkan Semua Data secara Polimorfik\nMethod overriding tampilkanData() dan tampilkanAktivitas() berjalan sempurna."
    r4.font.name = "Segoe UI"
    r4.font.size = Pt(11)
    r4.font.color.rgb = C_NAVY

    s15.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Aldo Prawiro Akbar):\n"
        "Pada Gambar 3 terlihat fitur Ubah Data. Admin cukup memasukkan ID, misalnya ID Menu atau ID Pesanan, dan sistem memanggil method setter untuk memperbarui harga atau total tagihan.\n"
        "Dan pada Gambar 4, ketika menu Tampilkan Semua Data dipilih, seluruh objek menampilkan informasi lengkapnya sesuai perilaku polimorfisme masing-masing child class."
    )

    # =========================================================================
    # SLIDE 16: KENDALA DAN SOLUSI TEKNIS
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_bg(s16, C_BG)
    add_header(s16, "Refleksi Proyek", "Kendala Teknis yang Dihadapi & Solusi")

    # Card 1: Scanner Issue
    add_card(s16, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_k1 = s16.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_k1 = tb_k1.text_frame
    tf_k1.word_wrap = True
    p = tf_k1.paragraphs[0]
    r = p.add_run()
    r.text = "1. Buffer Scanner Skipped Line"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_RED

    k1_desc = (
        "• Kendala:\n"
        "  Saat menggunakan method input.nextInt() untuk memilih angka menu atau harga, perintah input string berikutnya (input.nextLine()) otomatis terlewat tanpa menunggu ketikan pengguna.\n\n"
        "• Penyebab Teknis:\n"
        "  nextInt() hanya membaca karakter integer, meninggalkan karakter newline (enter '\\n') di dalam buffer Scanner stream.\n\n"
        "• Solusi:\n"
        "  Menambahkan satu baris 'input.nextLine();' tepat setelah setiap pemanggilan nextInt() untuk menguras buffer sisa enter secara tuntas."
    )
    p2 = tf_k1.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = k1_desc
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(11)
    r2.font.color.rgb = C_DARK

    # Card 2: Penyelarasan Tim
    add_card(s16, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_k2 = s16.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_k2 = tb_k2.text_frame
    tf_k2.word_wrap = True
    p = tf_k2.paragraphs[0]
    r = p.add_run()
    r.text = "2. Penyelarasan Modul Tim"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_BLUE

    k2_desc = (
        "• Kendala:\n"
        "  Pada fase awal, masing-masing anggota kelompok menggunakan penamaan method yang berbeda pada modulnya, sehingga terjadi ketidakcocokan pemanggilan di Main.java.\n\n"
        "• Dampak:\n"
        "  Terjadi inkonsistensi antarmuka method antar modul dan menyulitkan integrasi perulangan polimorfisme.\n\n"
        "• Solusi:\n"
        "  Menyepakati Interface LayananRestoran.java bersama dan menstandarisasi kontrak abstract method di 3 parent class sebelum mulai mengoding subclass."
    )
    p3 = tf_k2.add_paragraph()
    p3.space_before = Pt(8)
    r3 = p3.add_run()
    r3.text = k2_desc
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(11)
    r3.font.color.rgb = C_DARK

    s16.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor):\n"
        "Selama proses pengerjaan proyek UTS ini, kami menemui dua kendala utama: Pertama, kendala teknis buffer enter pada Scanner saat pembacaan angka ke teks, yang kami atasi dengan buffer cleansing nextLine().\n"
        "Kedua, koordinasi antar 3 anggota kelompok yang kami selesaikan dengan menyepakati Interface bersama di awal sebelum penulisan kode child class dimulai."
    )

    # =========================================================================
    # SLIDE 17: KESIMPULAN & SARAN PENGEMBANGAN
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_bg(s17, C_BG)
    add_header(s17, "Penutup", "Kesimpulan Proyek & Saran Pengembangan")

    add_card(s17, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_ks = s17.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_ks = tb_ks.text_frame
    tf_ks.word_wrap = True
    p = tf_ks.paragraphs[0]
    r = p.add_run()
    r.text = "Kesimpulan Utama"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_GREEN

    ks_pts = [
        "Aplikasi Sistem Informasi Restoran berhasil dibangun menggunakan 14 file Java yang modular dan terstruktur rapi.",
        "Kelima pilar OOP (Class/Object, Encapsulation, Inheritance, Polymorphism, Abstraction & Interface) telah diterapkan secara utuh 100%.",
        "Empat diagram UML (Class, Use Case, Sequence, Activity) telah terbukti sinkron dan selaras dengan implementasi kode Java yang dieksekusi.",
        "Pembagian tugas pengerjaan modul antar 3 anggota kelompok terlaksana secara adil dan terintegrasi solid."
    ]
    for pt in ks_pts:
        p_item = tf_ks.add_paragraph()
        p_item.space_before = Pt(10)
        r_item = p_item.add_run()
        r_item.text = f"✓ {pt}"
        r_item.font.name = "Segoe UI"
        r_item.font.size = Pt(11)
        r_item.font.color.rgb = C_DARK

    add_card(s17, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_sr = s17.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_sr = tb_sr.text_frame
    tf_sr.word_wrap = True
    p = tf_sr.paragraphs[0]
    r = p.add_run()
    r.text = "Saran Pengembangan (Future Work)"
    r.font.name = "Segoe UI"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = C_GOLD

    sr_pts = [
        "Implementasi Antarmuka GUI: Mengembangkan GUI desktop interaktif berbasis Java Swing atau JavaFX menggantikan tampilan CLI konsol.",
        "Integrasi Database Relasional: Menghubungkan sistem ke database MySQL / PostgreSQL melalui JDBC untuk persistensi data permanen.",
        "Fitur Cetak Struk Fisik: Menambahkan library pencetakan nota transaksi otomatis ke printer thermal restoran.",
        "Manajemen Stok Bahan Baku: Menambahkan relasi modul inventori dapur (Chef) untuk otomatisasi pengurangan bahan baku saat menu dipesan."
    ]
    for pt in sr_pts:
        p_item = tf_sr.add_paragraph()
        p_item.space_before = Pt(10)
        r_item = p_item.add_run()
        r_item.text = f"→ {pt}"
        r_item.font.name = "Segoe UI"
        r_item.font.size = Pt(11)
        r_item.font.color.rgb = C_DARK

    s17.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE (Fadhil Anshor):\n"
        "Sebagai kesimpulan, proyek Sistem Informasi Restoran ini telah berhasil memenuhi seluruh kriteria praktikum UTS PBO dengan mengimplementasikan 14 class dan 5 pilar OOP secara utuh.\n"
        "Ke depan, sistem ini memiliki potensi besar untuk dikembangkan lebih lanjut dengan menambahkan GUI berbasis JavaFX, koneksi database MySQL permanen, serta fitur pencetakan struk pembayaran."
    )

    # =========================================================================
    # SLIDE 18: PENUTUP & SESI Q&A
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_bg(s18, C_NAVY)

    # Center card
    add_card(s18, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), bg_color=C_NAVY_LIGHT, border_color=RGBColor(51, 65, 85))
    tb_end = s18.shapes.add_textbox(Inches(1.8), Inches(1.5), Inches(9.7), Inches(4.5))
    tf_end = tb_end.text_frame
    tf_end.word_wrap = True

    p0 = tf_end.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    r0 = p0.add_run()
    r0.text = "TERIMA KASIH\n"
    r0.font.name = "Segoe UI"
    r0.font.size = Pt(36)
    r0.font.bold = True
    r0.font.color.rgb = C_GOLD

    p1 = tf_end.add_paragraph()
    p1.alignment = PP_ALIGN.CENTER
    r1 = p1.add_run()
    r1.text = "Sesi Tanya Jawab (Q & A)\n"
    r1.font.name = "Segoe UI"
    r1.font.size = Pt(22)
    r1.font.bold = True
    r1.font.color.rgb = C_WHITE

    p2 = tf_end.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    r2 = p2.add_run()
    r2.text = "Kami mengundang Bapak/Ibu Dosen Pengampu serta rekan-rekan mahasiswa untuk memberikan pertanyaan, kritik, dan saran yang membangun.\n\n"
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(13)
    r2.font.color.rgb = RGBColor(203, 213, 225)

    p3 = tf_end.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    r3 = p3.add_run()
    r3.text = "Kelompok 2 - Kelas A | Teknologi Informasi UNIMUS\nFadhil Anshor (13242520005)  •  Aldo Prawiro Akbar (13242520007)  •  Zhafirah Haya Destiani (13242520008)"
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(12)
    r3.font.bold = True
    r3.font.color.rgb = C_GOLD

    s18.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTE - PENUTUP (Fadhil Anshor):\n"
        "Demikian presentasi dari Kelompok 2 mengenai Pengembangan Aplikasi Sistem Informasi Restoran Berbasis Object Oriented Programming.\n"
        "Kami memohon maaf apabila terdapat kekurangan dalam penyampaian. Selanjutnya, sesi tanya jawab kami buka. Kepada Bapak/Ibu dosen atau rekan-rekan yang ingin bertanya, kami persilakan dengan senang hati. Terima kasih.\nWassalamu'alaikum Warahmatullahi Wabarakatuh."
    )

    output_file = "Presentasi_SistemInformasiRestoran_Kelompok2.pptx"
    prs.save(output_file)
    print(f"Presentation successfully created and saved as: {output_file}")

if __name__ == "__main__":
    create_deck()
