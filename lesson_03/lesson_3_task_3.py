from address import Address
from mailing import Mailing

addr_from = Address("107007", "Москва", "ул. Пушкина", "д. 1", "кв. 1")
addr_to = Address("390000", "Тамбов", "ул.Рылеева", "д. 60", "кв. 77")


mailing = Mailing(
    to_address=addr_to,
    from_address=addr_from,
    cost=450.70,
    track="RU68098534"
)


print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} -"
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
