# PROGRES PROJECT — CHATBOT KESEHATAN TERPADU

## Informasi Project

- Judul: Chatbot Kesehatan Terpadu
- Editor: VS Code
- Bahasa pemrograman: Python

## Tahap yang Sudah Selesai

### Langkah 1 — Konsep Agen Cerdas
Sudah memahami:
- Environment
- Perception
- Action
- Goal
- Goal-based agent

### Langkah 2 — Desain Agen
Chatbot berfungsi sebagai agen cerdas untuk triase awal dan edukasi kesehatan.

Tujuan:
- Memberikan informasi kesehatan awal.
- Membantu menentukan tingkat urgensi keluhan.
- Mengarahkan pengguna ke tenaga medis jika diperlukan.
- Bukan alat diagnosis dan bukan pengganti dokter.

### Langkah 3 — System Prompt
Sudah merancang konsep system prompt dengan aturan:
- Hanya menangani keluhan ringan dan umum.
- Tidak memberikan diagnosis pasti.
- Tidak memberikan resep.
- Tidak memberikan dosis obat.
- Tidak memberikan instruksi pengobatan spesifik.
- Menggunakan bahasa Indonesia yang sederhana.
- Mengarahkan pengguna ke tenaga medis jika diperlukan.

### Langkah 4 — Guardrail
Memahami bahwa guardrail adalah lapisan keamanan di luar AI.

Alur:
User → Guardrail → AI

Jika darurat:
User → Guardrail → Eskalasi medis

### Langkah 5 — Guardrail V1
Sudah berhasil membuat guardrail menggunakan Python.

Struktur project:

chatbot-kesehatan-terpadu/
├── main.py
├── guardrail.py
└── PROGRES.md

Guardrail saat ini memiliki kategori:
- DARURAT
- SEDANG
- RINGAN
- TIDAK DIKENALI

Contoh pengujian:
- "saya pilek dan bersin sejak kemarin" → RINGAN
- "saya sesak napas berat" → DARURAT

## TAHAP BERIKUTNYA

### Langkah 6 — Guardrail V2
Membuat guardrail lebih cerdas agar dapat mengenali berbagai variasi kalimat pengguna.

Contoh:
- "Saya sulit sekali bernapas"
- "Napas saya terasa berat"
- "Saya susah menarik napas"
- "Dada saya terasa sangat sakit"

Setelah itu:
### Langkah 7 — Integrasi API AI

Kemudian dilanjutkan:
- System Prompt ke API
- Chatbot percakapan
- Testing 3 skenario
- Dokumentasi
- Diagram alur
- Laporan akhir


“Saya sudah selesai Langkah 5. Ini file PROGRES.md saya. Lanjutkan ke Langkah 6.”

🔖 CHECKPOINT PROJECT CHATBOT KESEHATAN — 19 Agustus 2026

Project: chatbot-kesehatan-terpadu

Sudah selesai:

Integrasi OpenAI API berhasil.
guardrail.py memiliki:
cek_urgensi()
cek_permintaan_obat()
cek_scope()
respons_urgensi()
respons_permintaan_obat()
respons_di_luar_scope()
Guardrail darurat berhasil diuji.
Permintaan dosis/resep berhasil diblokir sebelum AI.
Pertanyaan di luar scope berhasil diblokir.
Disclaimer otomatis sudah ditambahkan.

Masalah terakhir:
chatbot.py sebelumnya memiliki masalah indentasi/logika sehingga input hanya muncul tanpa respons.

Solusi terakhir yang diberikan:
Mengganti seluruh chatbot.py dengan versi yang memiliki:

tampilkan_disclaimer()
generate_response()
urutan guardrail: darurat → obat/dosis → scope → AI
while True
perintah keluar
generate_response(pesan) berada di dalam loop.

Tugas BESOK:

Jalankan python chatbot.py.
Uji dalam satu sesi:
saya pilek dan bersin
saya mengalami sesak napas berat
berapa dosis obat untuk demam
bagaimana cara melakukan operasi jantung
keluar
Pastikan semua hasil sesuai.
Setelah itu jangan buru-buru menambah fitur.
Lanjut ke pengujian formal 3+ skenario, dokumentasi fungsi setiap kode, diagram arsitektur, dan persiapan laporan/refleksi.

Catatan penting: Project harus selalu mengikuti ketentuan tugas: edukasi/triase awal saja, disclaimer wajib, eskalasi darurat tanpa AI, tidak memberikan diagnosis/resep/dosis/instruksi pengobatan spesifik.

Besok cukup bilang “lanjut dari checkpoint chatbot kesehatan”, lalu tempel checkpoint ini jika diperlukan.