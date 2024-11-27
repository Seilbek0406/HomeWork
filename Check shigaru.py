tauarlar = {
    1: {"aty": "алма", "baga": 550, "sany": 250, "olshem": "кг"},
    2: {"aty": "нан", "baga": 100, "sany": 35, "olshem": "шт"},
    3: {"aty": "кола", "baga": 500, "sany": 30, "olshem": "шт"}
}

for id, data in tauarlar.items():
    print(f"{id}: {data['aty']} бағасы: {data['baga']}тг, Складта: {data['sany']} {data['olshem']} қалды")

tt = int(input("Тауар айдиін таңдаңыз: "))
ttsany = int(input("Қанша алғыңыз келеді: "))

x = tauarlar[tt]
print(f"\nТаңдалған тауар: {x['aty']}, бағасы: {x['baga']}тг, Складта: {x['sany']} {x['olshem']} қалды")

if ttsany <= x['sany']:
    x['sany'] -= ttsany
    total_price = x['baga'] * ttsany

    print("\n---------------------- Чек ----------------------")
    print(f"Тауар: {x['aty']}")
    print(f"Саны: {ttsany} {x['olshem']}")
    print(f"Бағасы: {x['baga']} тг")
    print(f"Жалпы құн: {total_price} тг")
    print("\n--------------------- Рахмет! ---------------------")

    print(f"Қалған саны: {x['sany']} {x['olshem']}")
else:
    print("Кешіріңіз, жеткілікті тауар жоқ!")