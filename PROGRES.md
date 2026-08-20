# PROGRES PROJECT — CHATBOT KESEHATAN TERPADU

## Informasi Project

- Judul: Chatbot Kesehatan Terpadu
- Editor: VS Code
- Bahasa pemrograman: Python
- Model AI: OpenAI API
- Program utama: `chatbot.py`

---

## Tahap yang Sudah Selesai

### Langkah 1 — Konsep Agen Cerdas

Memahami konsep dasar agen cerdas:

- Environment
- Perception
- Action
- Goal
- Goal-based agent

Chatbot dirancang sebagai agen yang menerima input keluhan pengguna, memproses informasi melalui guardrail, kemudian memberikan respons sesuai tingkat urgensi dan cakupan sistem.

---

### Langkah 2 — Desain Agen

Chatbot berfungsi sebagai sistem untuk:

- Edukasi kesehatan umum.
- Triase awal keluhan kesehatan.
- Mengenali indikasi kondisi yang membutuhkan perhatian medis.
- Mengarahkan pengguna ke tenaga medis jika diperlukan.

Sistem bukan alat diagnosis dan bukan pengganti dokter atau tenaga medis profesional.

---

### Langkah 3 — System Prompt

System prompt dirancang untuk membatasi perilaku AI.

Aturan utama:

- Tidak memberikan diagnosis pasti.
- Tidak mengklaim sebagai dokter atau tenaga medis.
- Tidak memberikan resep obat.
- Tidak memberikan dosis obat.
- Tidak memberikan instruksi pengobatan spesifik.
- Menggunakan bahasa yang sederhana dan hati-hati.
- Mengajukan pertanyaan klarifikasi jika informasi tidak cukup.
- Mengarahkan pengguna ke tenaga medis jika terdapat tanda bahaya.
- Tidak menangani kondisi darurat sebagai konsultasi biasa.
- Membatasi pembahasan pada keluhan kesehatan ringan dan umum.

---

### Langkah 4 — Guardrail

Guardrail digunakan sebagai lapisan keamanan sebelum input diteruskan ke AI.

Alur utama:

```text
User
  ↓
Guardrail
  ↓
Pemeriksaan urgensi
  ↓
Pemeriksaan permintaan obat/dosis
  ↓
Pemeriksaan scope
  ↓
AI

Guardrail memiliki beberapa kategori urgensi:

DARURAT
SEDANG
RINGAN
TIDAK DIKENALI

Selain pemeriksaan urgensi, guardrail juga memeriksa:

Permintaan obat atau dosis.
Apakah input masih berada dalam cakupan sistem.
Langkah 5 — Guardrail V1

Guardrail berhasil dibuat menggunakan Python.

Fungsi utama:

cek_urgensi()
respons_urgensi()
cek_permintaan_obat()
respons_permintaan_obat()
cek_scope()
respons_di_luar_scope()

Guardrail menggunakan daftar kata/frasa untuk mengenali pola keluhan.

Contoh:

"saya sesak napas berat" → DARURAT
"saya sulit sekali bernapas" → DARURAT
"napas saya terasa berat" → DARURAT
"dada saya terasa sangat sakit" → DARURAT
"saya demam tidak membaik" → SEDANG
"saya pilek dan bersin" → RINGAN
Langkah 6 — Integrasi AI

OpenAI API berhasil diintegrasikan melalui file:

ai_service.py

Library yang digunakan:

openai==3.1.0
python-dotenv==1.2.2

API key disimpan dalam file .env dan tidak dimasukkan ke repository.

Program menggunakan:

OpenAI Responses API

dengan model:

gpt-5-mini

System prompt digunakan untuk membatasi respons AI agar tetap berada pada tujuan edukasi dan triase awal kesehatan.

Langkah 7 — Program Chatbot Utama

Program utama berada pada:

chatbot.py

Alur program:

Input pengguna
      ↓
Cek urgensi
      ↓
Jika DARURAT → Eskalasi medis
      ↓
Cek permintaan obat/dosis
      ↓
Jika terdeteksi → Tolak permintaan
      ↓
Cek scope
      ↓
Jika di luar scope → Tolak pertanyaan
      ↓
Jika lolos → Kirim ke AI
      ↓
Respons chatbot

Program juga menyediakan perintah:

keluar

untuk mengakhiri percakapan.

Langkah 8 — Pengujian Guardrail

Pengujian dilakukan menggunakan:

test_guardrail.py

Skenario yang telah diuji meliputi:

Gejala darurat.
Gejala ringan.
Gejala dengan urgensi sedang.
Input yang belum dapat dikenali.
Pernyataan negatif mengenai gejala darurat.
Respons guardrail.

Contoh hasil pengujian:

"saya sesak napas berat" → DARURAT
"saya sulit sekali bernapas" → DARURAT
"napas saya terasa berat" → DARURAT
"dada saya terasa sangat sakit" → DARURAT
"saya pilek dan bersin" → RINGAN
"saya demam tidak membaik" → SEDANG

Pengujian berhasil dijalankan dengan:

python test_guardrail.py
Langkah 9 — Pengujian Program Utama

Program utama berhasil dijalankan dengan:

python chatbot.py

Beberapa skenario yang telah diuji:

Skenario 1 — Kondisi darurat

Input:

saya sesak napas

Hasil:

Urgensi: darurat

Input tidak diteruskan ke AI dan sistem memberikan arahan untuk mencari pertolongan medis.

Skenario 2 — Permintaan dosis obat

Input:

berapa dosis obat untuk demam

Hasil:

Permintaan obat/dosis terdeteksi.

Sistem menolak memberikan dosis atau resep.

Skenario 3 — Pertanyaan di luar scope

Input:

bagaimana cara memperbaiki mobil

Hasil:

Input berada di luar scope.

Pertanyaan tidak diteruskan ke AI.

Skenario 4 — Keluhan ringan

Input:

saya pilek dan bersin

Hasil:

Urgensi: ringan

Input diteruskan ke AI untuk edukasi umum.

Langkah 10 — Pengujian Sintaks Python

Seluruh file Python utama berhasil diperiksa menggunakan:

python -m py_compile ai_service.py chatbot.py guardrail.py test_guardrail.py

Tidak terdapat error sintaks.

Langkah 11 — Repository Git

Repository Git lokal berhasil dibuat.

Branch utama:

main

Commit pertama:

Initial version of health chatbot

Repository berhasil terhubung ke GitHub dan berhasil melakukan push.

Remote:

origin

Status terakhir:

Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean

File yang masuk repository:

.gitignore
PROGRES.md
ai_service.py
chatbot.py
guardrail.py
requirements.txt
test_guardrail.py

File yang tidak dimasukkan:

.env
__pycache__/
*.pyc
Struktur Project Saat Ini
chatbot-kesehatan-terpadu/
│
├── .gitignore
├── PROGRES.md
├── requirements.txt
├── ai_service.py
├── chatbot.py
├── guardrail.py
└── test_guardrail.py
Dependency

File requirements.txt berisi:

openai==3.1.0
python-dotenv==1.2.2

Dependency dapat dipasang menggunakan:

pip install -r requirements.txt
Status Project

Status saat ini:

IMPLEMENTASI UTAMA SELESAI

Komponen utama sudah tersedia:

 Konsep agen cerdas
 Desain agen
 System prompt
 Guardrail
 Integrasi OpenAI API
 Program chatbot utama
 Pengujian guardrail
 Pengujian program utama
 Pengujian sintaks
 requirements.txt
 .gitignore
 Repository Git
 Push ke GitHub
Tahap Selanjutnya

Tahap berikutnya adalah penyempurnaan dan dokumentasi project:

Memperbaiki beberapa edge case pada guardrail.
Menambahkan pengujian untuk permintaan obat/dosis.
Menambahkan pengujian untuk input di luar scope.
Menambahkan pengujian variasi penulisan seperti nafas dan napas.
Menyusun tabel hasil pengujian.
Membuat diagram alur sistem.
Menyusun dokumentasi dan laporan akhir.
Melakukan pemeriksaan akhir repository sebelum dikumpulkan.

---

---

## Langkah 10 — Pengujian End-to-End

Pengujian dilakukan terhadap program utama `chatbot.py` untuk memastikan seluruh alur sistem berjalan sesuai rancangan.

### Skenario 1 — Kondisi Darurat

Input:

```text
saya sulit bernapas