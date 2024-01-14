import os

from dotenv import load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from vgmuse.models.ost import OSTCollection

load_dotenv()

app = FastAPI(
    title="VGMuse private API",
    summary="A private API for VGMuse",
)

client = AsyncIOMotorClient(os.environ["MONGO_URI"])
db = client.get_database("vgmuse")
ost_collection = db.get_collection("ost")

@app.get("/osts/", response_model=OSTCollection, response_model_by_alias=False)
async def get_osts():
    osts = await ost_collection.find().to_list(1000)
    return OSTCollection(osts=osts)
