
import requests
import time
import boto3


def store_voice_file():
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id = 'nQCZlgvbvwuSr7C99Uxx',
        aws_secret_access_key = 'lzW5cDdY6wgCs4DifJFhoAdZHrS7s_2eq6m-0TqJ'

    )
    s3.put_object(Bucket='voiceconvert', Key='voice.ogg', StorageClass='STANDARD')
    s3.upload_file('voice.ogg', 'voiceconvert','voice.ogg')


def yandex_voice_recognition():
    result=""
    key = 'AQVNx28rPwUX-yoQAba-HBmnOpqj9dtqW1mKQ2A2'
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
    print('Header ' + str(header))
    req = requests.post(POST, headers=header, json=body)
    data = req.json()
    print(data)
    id = data['id']
    while True:
        time.sleep(1)
        GET = "https://operation.api.cloud.yandex.net/operations/{id}"
        req = requests.get(GET.format(id=id), headers=header)
        req = req.json()
        if req['done']: break
        print("In translating")
    print("Текст:")
    for chunk in req['response']['chunks']:
        result =result + chunk['alternatives'][0]['text']
    print(result)
    return result

store_voice_file()
yandex_voice_recognition()

