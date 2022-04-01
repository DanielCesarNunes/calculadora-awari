from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from utils import transform_dict_to_pandas
from model_linear_regression import LinearRegression


app = FastAPI()


class Aluguel(BaseModel):
    Metros: float
    Quartos: int
    Banheiros: int


@app.get("/")
async def hello_world():
    return {'message': 'hello world'}


@app.post("/predict/")
async def predict_pipe(aluguel: Aluguel):
    aluguel_dict = aluguel.dict()
    df = transform_dict_to_pandas(aluguel_dict)
    lr = LinearRegression()
    predict_value = lr.predict(df)[0]
    response_body = {}
    response_body["Metros"] = aluguel.Metros
    response_body["Predict"] = round(predict_value, 2)
    return response_body
