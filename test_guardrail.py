from guardrail import (
    cek_urgensi,
    cek_permintaan_obat,
    cek_scope
)


def test_urgensi():
    kasus = [
        ("saya sesak napas berat", "darurat"),
        ("saya sesak npas berat", "darurat"),
        ("saya sesak nafas", "darurat"),
        ("saya sulit sekali bernapas", "darurat"),
        ("napas saya terasa berat", "darurat"),
        ("saya susah menarik napas", "darurat"),
        ("dada saya terasa sangat sakit", "darurat"),
        ("saya pingsan", "darurat"),
        ("saya kejang", "darurat"),

        ("saya demam tidak membaik", "sedang"),
        ("saya muntah berulang", "sedang"),
        ("kondisi saya semakin memburuk", "sedang"),

        ("saya pilek", "ringan"),
        ("saya bersin", "ringan"),
        ("saya batuk ringan", "ringan"),
        ("saya sakit kepala ringan", "ringan"),

        ("saya tidak mengalami sesak napas", "tidak_dikenali"),
        ("saya tidak mengalami nyeri dada", "tidak_dikenali"),
    ]

    print("\n=== TEST URGENSI ===")

    gagal = 0

    for teks, expected in kasus:
        actual = cek_urgensi(teks)

        if actual == expected:
            print(f"PASS | {teks} -> {actual}")
        else:
            print(
                f"FAIL | {teks} -> "
                f"expected={expected}, actual={actual}"
            )
            gagal += 1

    print(f"\nHasil: {len(kasus) - gagal}/{len(kasus)} PASS")

    return gagal == 0


def test_permintaan_obat():
    kasus = [
        ("berapa dosis obat untuk demam", True),
        ("berapa mg obat ini", True),
        ("obat apa yang harus saya minum", True),
        ("berapa kali minum obat", True),
        ("saya pilek dan bersin", False),
    ]

    print("\n=== TEST PERMINTAAN OBAT ===")

    gagal = 0

    for teks, expected in kasus:
        actual = cek_permintaan_obat(teks)

        if actual == expected:
            print(f"PASS | {teks} -> {actual}")
        else:
            print(
                f"FAIL | {teks} -> "
                f"expected={expected}, actual={actual}"
            )
            gagal += 1

    print(f"\nHasil: {len(kasus) - gagal}/{len(kasus)} PASS")

    return gagal == 0


def test_scope():
    kasus = [
        ("saya pilek", True),
        ("saya bersin-bersin", True),
        ("saya batuk", True),
        ("saya sakit kepala", True),
        ("saya sakit tenggorokan", True),
        ("saya maag", True),
        ("saya mual", True),
        ("saya alergi", True),

        ("bagaimana cara memperbaiki mobil", False),
        ("bagaimana cara memperbaiki komputer", False),
        ("berapa harga mobil", False),
    ]

    print("\n=== TEST SCOPE ===")

    gagal = 0

    for teks, expected in kasus:
        actual = cek_scope(teks)

        if actual == expected:
            print(f"PASS | {teks} -> {actual}")
        else:
            print(
                f"FAIL | {teks} -> "
                f"expected={expected}, actual={actual}"
            )
            gagal += 1

    print(f"\nHasil: {len(kasus) - gagal}/{len(kasus)} PASS")

    return gagal == 0


if __name__ == "__main__":
    hasil_urgensi = test_urgensi()
    hasil_obat = test_permintaan_obat()
    hasil_scope = test_scope()

    print("\n==============================")
    print("HASIL AKHIR TEST")
    print("==============================")

    if hasil_urgensi and hasil_obat and hasil_scope:
        print("SEMUA TEST BERHASIL")
    else:
        print("ADA TEST YANG GAGAL")