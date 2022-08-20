from ast import For
from fastapi import Form
from pydantic import BaseModel


class BinanceConnections(BaseModel):
    key: str
    secret: str
    
    @classmethod
    def as_form(
        cls,
        binancekey: str = Form(...),
        binancesecret: str = Form(...)
    ):
        return cls(
            key=binancekey,
            secret=binancesecret
                   )