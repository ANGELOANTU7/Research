from fastapi import FastAPI,Path,Form
from fastapi.responses import StreamingResponse
import io
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import FetchBucketData


app = FastAPI()


origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/plant_data")

def PlantData():
    data = FetchBucketData.FetchPlantData()
    print("plant data : ",data)
    # return data
    response = data
    headers = {
        "Access-Control-Allow-Origin": "*",
    }
    return JSONResponse(content=response, headers=headers)

@app.get("/plant_feed/{index}")

def PlantFeed(index: int = Path(..., gt=0, le=50)):
    print("index",index)
    IndexNumber = int(index)

    image_contents = FetchBucketData.FetchPlantFeed(IndexNumber)
    headers = {
        "Access-Control-Allow-Origin": "*",
    }
    return StreamingResponse(content = io.BytesIO(image_contents), media_type='image/jpeg',headers=headers)
    
@app.post("/post_plant_grade")
def PostPlantGrade(plant_grade : str = Form(...),plant_index : str = Form(...), moisture_adjustment : str = Form(...)):
    return {"grade" : plant_grade, "plant_index" : plant_index, "moisture_adjustment" : moisture_adjustment}
