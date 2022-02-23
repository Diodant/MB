import requests
import json
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Вы пытаетесь перевести одинаковые валюты {base}')
        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена")

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[exchanges[base]]

        return total_base