from fastapi import FastAPI,Path,Form
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
    
@app.post("/post_plant_grade")
def PostPlantGrade(plant_grade : str = Form(...),plant_index : str = Form(...), moisture_adjustment : str = Form(...)):
    return {"grade" : plant_grade, "plant_index" : plant_index, "moisture_adjustment" : moisture_adjustment}
