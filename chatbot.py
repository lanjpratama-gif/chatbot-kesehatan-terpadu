from guardrail import (
    cek_urgensi,
    cek_permintaan_obat,
    cek_scope,
    respons_urgensi,
    respons_permintaan_obat,
    respons_di_luar_scope
)

from ai_service import ask_ai


def tampilkan_disclaimer():
    print()
    print("=== CHATBOT KESEHATAN TERPADU ===")
    print()
    print("DISCLAIMER:")
    print(
        "Chatbot ini hanya digunakan untuk edukasi dan "
        "triase awal kesehatan."
    )
    print(
        "Chatbot bukan pengganti dokter atau tenaga medis "
        "profesional dan tidak digunakan untuk diagnosis "
        "atau pengobatan."
    )
    print(
        "Jika mengalami kondisi darurat, segera hubungi "
        "layanan gawat darurat atau tenaga medis."
    )
    print()


def generate_response(user_message):
    # Lapisan 1: cek tingkat urgensi
    urgency = cek_urgensi(user_message)

    print(f"\n[Guardrail] Urgensi: {urgency}")

    # Jika darurat, jangan teruskan ke AI
    if urgency == "darurat":
        return respons_urgensi(urgency)

    # Lapisan 2: cek permintaan obat/dosis
    if cek_permintaan_obat(user_message):
        print("[Guardrail] Permintaan obat/dosis terdeteksi.")
        return respons_permintaan_obat()

    # Lapisan 3: cek apakah pertanyaan masih dalam scope
    if not cek_scope(user_message):
        print("[Guardrail] Input berada di luar scope.")
        return respons_di_luar_scope()

    # Jika lolos semua guardrail, kirim ke AI
    return ask_ai(user_message)


if __name__ == "__main__":
    tampilkan_disclaimer()

    while True:
        pesan = input("Anda: ")

        # Perintah untuk keluar
        if pesan.lower().strip() == "keluar":
            print("Chatbot: Terima kasih. Sampai jumpa.")
            break

        # Memproses pesan melalui guardrail dan AI
        jawaban = generate_response(pesan)

        # Menampilkan jawaban
        print("\nChatbot:", jawaban)