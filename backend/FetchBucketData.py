import boto3


bucket_name = 'bucket_name_here'


# Replace with your AWS access key and secret access key
access_key = 'access_key_here'
secret_key = 'secret_key_here'

# Create an S3 client with your credentials
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)


def FetchPlantData():
    file_name = 'packet.csv'
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = response['Body'].read().decode('utf-8')

    moist1 = data[0] + data[1]
    moist2 = data[3] + data[4]
    moist3 = data[6] + data[7]
    moist4 = data[9] + data[10]

    temp1 = data[12] + data[13]
    temp2 = data[15] + data[16]
    
    temp1 = float(temp1)
    temp2 = float(temp2)
    temp = (temp1 + temp2) / 2

    hum1 = data[18] + data[19]
    hum2 = data[21] + data[22]

    hum1 = float(hum1)
    hum2 = float(hum2)
    hum = (hum1 + hum2) / 2

    plant_data = {
        "moisture1" : float(moist1),
        "moisture2" : float(moist2),
        "mositure3" : float(moist3),
        "moisture4" : float(moist4),
        "tempreature" : temp,
        "humidity" : hum
    }

    return plant_data

def FetchPlantFeed(IndexNumber):
    folder_name = 'image/'
    image_name = 'img{ind}.jpg'.format(ind = IndexNumber)

    response = s3.get_object(Bucket=bucket_name, Key=folder_name + image_name)


    image_contents = response['Body'].read()

    
    return image_contents
