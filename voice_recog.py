
import requests
import time
import boto3
import config


def store_voice_file():
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id = str(config.Config().aws_access_key()),
        aws_secret_access_key = str(config.Config().aws_access_secret_key())

    )
    s3.put_object(Bucket='voiceconvert', Key='voice.ogg', StorageClass='STANDARD')
    s3.upload_file('voice_store/voice.ogg', 'voiceconvert','voice.ogg')


def yandex_voice_recognition():
    result=""
    key = str(config.Config().yandex_speech_key())
    filelink = 'https://storage.yandexcloud.net/voiceconvert/voice.ogg'
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
    header = {'Authorization': 'Api-Key {}'.format(key)}
    req = requests.post(POST, headers=header, json=body)
    data = req.json()
    print(data)
    id = data['id']
    while True: 
        #"#от_заказчика\n"
        time.sleep(1)
        GET = "https://operation.api.cloud.yandex.net/operations/{id}"
        req = requests.get(GET.format(id=id), headers=header)
        req = req.json()
        if req['done']: break
        print("In translating")
    print("Текст:")
    for chunk in req['response']['chunks']:
        result =result + chunk['alternatives'][0]['text'] + '. '
    print(result)
    return result

store_voice_file()
yandex_voice_recognition()

