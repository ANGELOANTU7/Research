from fastapi import FastAPI,Path
from fastapi.responses import StreamingResponse
import io

import FetchBucketData

app = FastAPI()




@app.get("/plant_data")

def PlantData():
    data = FetchBucketData.FetchPlantData()
    print("plant data : ",data)
    return data

@app.get("/plant_feed/{index}")

def PlantFeed(index: int = Path(..., gt=0, le=50)):
    print(index)
    IndexNumber = int(index)

    image_contents = FetchBucketData.FetchPlantFeed(IndexNumber)
    return StreamingResponse(content = io.BytesIO(image_contents), media_type='image/jpeg')
    
    