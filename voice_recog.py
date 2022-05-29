
import requests
import time
import boto3
import config

#Store voice file to yandex cloud storage
def store_voice_file():
    session = boto3.session.Session()
    #set up section
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id = str(config.Config().aws_access_key()),
        aws_secret_access_key = str(config.Config().aws_access_secret_key())

    )
    #create file
    s3.put_object(Bucket='voiceconvert', Key='voice.ogg', StorageClass='STANDARD')
    #upload 
    s3.upload_file('voice_store/voice.ogg', 'voiceconvert','voice.ogg')


#Calling Yandex Speech Kit Recognition
def yandex_voice_recognition():
    #setup key
    result=""
    key = str(config.Config().yandex_speech_key())
    #set up url
    #url file was uploaded
    filelink = 'https://storage.yandexcloud.net/voiceconvert/voice.ogg'
    #url calling
    POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"
    body ={
        "config": {
            "specification": {
                "languageCode": "ru-RU"
            }
        },
        "audio": {
            "uri": filelink
        }
    }
    #prepare header
    header = {'Authorization': 'Api-Key {}'.format(key)}
    #request
    req = requests.post(POST, headers=header, json=body)
    data = req.json()
    print(data)
    #take id of processs
    id = data['id']
    while True: 
        #"#от_заказчика\n"
        time.sleep(1)
        GET = "https://operation.api.cloud.yandex.net/operations/{id}"
        req = requests.get(GET.format(id=id), headers=header)
        req = req.json()
        if req['done']: break
        print("In translating")
    #prepare bind data returned
    print("Текст:")
    #read each sentence
    for chunk in req['response']['chunks']:
        result =result + chunk['alternatives'][0]['text'] + '. '
    print(result)
    
    return result


