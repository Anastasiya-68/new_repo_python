from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "A17", "+79537013455"))
catalog.append(Smartphone("Samsung", "A26", "+79537543897"))
catalog.append(Smartphone("Xiaomi", "Redmi 17", "+79675348002"))
catalog.append(Smartphone("Apple", "iPhone 17 Pro Max", "+79863467231"))
catalog.append(Smartphone("Honor", "400 Pro", "+79542390007"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.number}")
