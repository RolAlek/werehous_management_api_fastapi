from crud.base import CRUDBase
from models import Product


class CrudProduct(CRUDBase):
    pass


crud_manager = CrudProduct(Product)
