from datetime import datetime


class Product:
    def __init__(self,
                 product_id: int,
                 name: str,
                 price: float,
                 quantity: int = 1,
                 expiration: datetime = datetime.utcnow(),
                 discount: float = 0,
                 description: str = ''
                 ):
        self._name = name
        self._product_id = product_id
        self._price = price
        self._quantity = quantity
        self._expiration = expiration
        self._discount = discount
        self._description = description

    def to_dict(self):
        return {
            'name': self._name,
            'product_id': self._product_id,
            'price': self._price,
        }
