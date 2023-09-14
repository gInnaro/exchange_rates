from fastapi import FastAPI
import requests
 
app = FastAPI()

@app.get("/api/rates")
def daily_rates(froms: str, to: str, value: float):
    r = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    if to == 'RUB':
        data = (1 / r['rates'][froms]) * value
        return {"result": data}
    elif froms == 'RUB':
        data = r['rates'][to] * value
        return {"result": data}
