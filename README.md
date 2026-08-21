# Chatbot Kesehatan Terpadu

## Deskripsi Project

Chatbot Kesehatan Terpadu merupakan sistem konsultasi kesehatan awal berbasis Generative AI menggunakan OpenAI API.

Sistem ini dirancang sebagai intelligent agent yang membantu pengguna memperoleh edukasi kesehatan ringan dan melakukan triase awal berdasarkan keluhan pengguna.

Chatbot ini bukan pengganti dokter atau tenaga medis profesional dan tidak digunakan untuk memberikan diagnosis, resep obat, atau dosis pengobatan.

# Tujuan Sistem

Tujuan pembuatan chatbot ini adalah:

- Memberikan edukasi kesehatan umum.
- Membantu pengguna memahami keluhan ringan.
- Melakukan deteksi awal terhadap kondisi yang membutuhkan perhatian medis.
- Menyediakan mekanisme keamanan agar AI tidak memberikan respons yang berisiko.

# Teknologi yang Digunakan

- Python
- OpenAI API
- python-dotenv
- Git & GitHub

# Struktur Project

# Penjelasan File

## chatbot.py

Program utama chatbot yang mengatur alur percakapan pengguna.

## guardrail.py

Lapisan keamanan yang melakukan pemeriksaan:
- Kondisi darurat.
- Permintaan obat/dosis.
- Pertanyaan di luar scope.

## ai_service.py

Penghubung aplikasi Python dengan OpenAI API.

## test_guardrail.py

File pengujian otomatis untuk memastikan guardrail berjalan sesuai rancangan.

# Fitur Sistem

- Konsultasi kesehatan ringan.
- Deteksi kondisi darurat.
- Penolakan permintaan resep dan dosis obat.
- Pembatasan pertanyaan di luar cakupan kesehatan.

# Cara Menjalankan

Install dependency:

pip install -r requirements.txt


Jalankan program:

python chatbot.py

# Pengujian Sistem

Hasil pengujian:

| Pengujian | Hasil |
|---|---|
| Deteksi urgensi | 18/18 PASS |
| Permintaan obat/dosis | 5/5 PASS |
| Pembatasan scope | 11/11 PASS |
| Pengujian sintaks Python | PASS |
| Pengujian program utama | PASS |

# Catatan

Chatbot ini dibuat untuk edukasi kesehatan awal dan triase sederhana.

Sistem bukan pengganti dokter atau tenaga medis profesional.