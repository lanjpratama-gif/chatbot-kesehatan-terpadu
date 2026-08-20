KATA_DARURAT = [
    "sesak napas berat",
    "sesak npas",
    "sesak npas berat",
    "sesak napas",
    "sesak nafas",
    "sulit bernapas",
    "sulit bernafas",
    "sulit sekali bernapas",
    "susah bernapas",
    "susah bernafas",
    "susah menarik napas",
    "susah menarik nafas",
    "sulit menarik napas",
    "sulit menarik nafas",
    "napas terasa berat",
    "nafas terasa berat",
    "napas saya terasa berat",
    "nafas saya terasa berat",
    "tidak bisa bernapas",
    "tidak bisa bernafas",

    "nyeri dada hebat",
    "sakit dada hebat",
    "dada terasa sangat sakit",
    "dada saya terasa sangat sakit",

    "pendarahan hebat",
    "perdarahan hebat",

    "tidak sadar",
    "pingsan",
    "kejang",
    "penurunan kesadaran"
]

KATA_NEGASI_DARURAT = [
    "tidak mengalami sesak napas",
    "tidak mengalami nyeri dada",
    "tidak sesak napas",
    "tidak ada sesak napas",
    "tidak ada nyeri dada"
]

KATA_SEDANG = [
    "demam beberapa hari",
    "demam tidak membaik",
    "muntah berulang",
    "nyeri cukup berat",
    "semakin memburuk",
    "tidak kunjung membaik"
]

KATA_RINGAN = [
    "pilek",
    "bersin",
    "batuk ringan",
    "sakit kepala ringan",
    "sakit tenggorokan ringan",
    "maag ringan"
]

KATA_SCOPE = [
    "pilek",
    "bersin",
    "batuk",
    "sakit kepala",
    "sakit tenggorokan",
    "maag",
    "mual",
    "alergi",
    "hidung tersumbat",
    "bersin-bersin"
]
KATA_OBAT = [
     "berapa dosis",
    "dosis obat",
    "berapa mg",
    "berapa miligram",
    "obat apa yang harus diminum",
    "obat apa yang harus saya minum",
    "resep obat",
    "resep untuk",
    "berapa kali minum obat",
    "cara minum obat"
]

def cek_permintaan_obat(teks):
    teks = teks.lower().strip()

    for kata in KATA_OBAT:
        if kata in teks:
            return True

    return False

def respons_permintaan_obat():
    return (
         "Maaf, chatbot ini tidak memberikan resep, dosis, "
        "atau instruksi penggunaan obat secara spesifik. "
        "Untuk informasi penggunaan obat yang sesuai kondisi "
        "Anda, silakan membaca petunjuk pada kemasan atau "
        "berkonsultasi dengan apoteker atau tenaga medis."
    )

def cek_scope(teks):
    teks = teks.lower().strip()

    for kata in KATA_SCOPE:
        if kata in teks:
            return True

    return False


def respons_di_luar_scope():
    return (
        "Maaf, chatbot ini memiliki cakupan terbatas untuk "
        "edukasi dan triase awal keluhan kesehatan ringan-umum. "
        "Saya tidak dapat menangani pertanyaan tersebut sebagai "
        "diagnosis atau konsultasi medis. Untuk kondisi atau "
        "keluhan yang lebih kompleks, silakan berkonsultasi "
        "dengan tenaga medis profesional."
    )


def cek_urgensi(teks):
    teks = teks.lower().strip()

    for kata in KATA_NEGASI_DARURAT:
        if kata in teks:
            return "tidak_dikenali"

    for kata in KATA_DARURAT:
        if kata in teks:
            return "darurat"

    for kata in KATA_SEDANG:
        if kata in teks:
            return "sedang"

    for kata in KATA_RINGAN:
        if kata in teks:
            return "ringan"

    return "tidak_dikenali"

def respons_urgensi(urgensi):
    if urgensi == "darurat":
        return (
            "⚠️ Kondisi yang Anda sampaikan dapat memerlukan "
            "penanganan medis segera. Silakan segera mencari "
            "bantuan medis atau menghubungi layanan gawat darurat "
            "setempat. Chatbot ini bukan pengganti tenaga medis."
        )

    elif urgensi == "sedang":
        return (
            "Keluhan Anda perlu diperhatikan. Chatbot akan "
            "memerlukan beberapa informasi tambahan untuk membantu "
            "triase awal. Jika kondisi semakin memburuk atau "
            "mengkhawatirkan, segera konsultasikan dengan tenaga medis."
        )

    elif urgensi == "ringan":
        return (
            "Keluhan Anda tampak termasuk dalam cakupan keluhan "
            "ringan yang dapat dibahas untuk edukasi kesehatan umum. "
            "Informasi yang diberikan chatbot bukan diagnosis medis."
        )

    else:
        return (
            "Saya belum dapat menentukan tingkat urgensi dari "
            "informasi yang diberikan. Silakan jelaskan gejala, "
            "sejak kapan terjadi, dan tingkat keparahannya."
        )