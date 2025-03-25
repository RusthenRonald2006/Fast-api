from pydantic import BaseModel

#Em resumo, o BaseModel do Pydantic define a estrutura dos dados e garante que as informações que você recebe estejam no formato certo.

class Product(BaseModel):
    name: str
    price: float