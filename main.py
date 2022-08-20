import os
import uvicorn
from fastapi import FastAPI, Request
from binance.cm_futures import CMFutures
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from uitils import *


app = FastAPI(
    title = "Ricardo Fuentes Testing Binance ....",
    description = "Ricardo Fuentes / Binance Futures",
    version = "v0.2",
)       
# script_dir = os.path.dirname(__file__)
# st_abs_file_path = os.path.join(script_dir, "/static")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/binance/test/connection/{key}/{secret}')
def auth_get_all_blog_users(key: str, secret: str):
    cm_futures_client = CMFutures(key=key, secret=secret)
    return cm_futures_client.account()

@app.get('/binance/account/{api_key}/{secret}')
async def binance_account(api_key: str, secret: str):
    client = RequestClient(api_key=api_key, secret_key=secret)
    result = client.get_account_information()
    capital, asset_1, asset_2 = Get_Capital(result, "USDT")
    return  capital, asset_1, asset_2

# @app.get('/binance/candle')
# async def binance_candle(request: Request):
#     client = RequestClient(api_key=api_key, secret=secret)
#     candels = client.get_candlestick_data(symbol="BTCUSDT", interval="1m", limit=10)
#     return candels

# @app.get('/binance/filter/market')
# async def binance_account():
#     client = RequestClient(api_key=api_key, secret_key=secret)
#     result = client.get_exchange_information()
#     minQty, stepSize, maxQtz = Get_Exchange_filters(r= Calculate_max_Decimal_Qty(stepSize)esult, "ADAUSDT")
#     maxDecimal 
#     return  maxDecimal

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    uvicorn.run("main:app", host = "0.0.0.0", port = port, debug=False)