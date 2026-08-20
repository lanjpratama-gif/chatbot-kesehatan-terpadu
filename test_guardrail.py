from guardrail import cek_urgensi, respons_urgensi


pesan = [
    "saya sesak napas berat",
    "saya sulit sekali bernapas",
    "napas saya terasa berat",
    "saya susah menarik napas",
    "dada saya terasa sangat sakit",
    "saya pilek dan bersin",
    "saya demam tidak membaik",
    "saya merasa tidak enak badan",
    "saya tidak mengalami sesak napas",
"saya tidak mengalami nyeri dada"
]


for teks in pesan:
    urgensi = cek_urgensi(teks)
    respons = respons_urgensi(urgensi)

    print(f"Input   : {teks}")
    print(f"Urgensi : {urgensi}")
    print(f"Respons : {respons}")
    print("-" * 60)