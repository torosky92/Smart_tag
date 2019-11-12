from models.product import Product

class Display:
    def __init__(self,
                 tag_id: int,
                 store: str = 'test_store',
                 location: dict = None,
                 product: Product = None
                 ):
        self._tag_id = tag_id
        self._store = store
        self._location = location if location else {'row': 0, 'column': 0, 'corridor': 'A'}
        self._product = product
