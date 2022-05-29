#file config
class Config :
    TELEGRAM_TOKEN="5490985665:AAEU_lgKJsaxLn0c8EssQZ0bsWjTQz3dtdc"
    AWS_ACCESS_KEY = "nQCZlgvbvwuSr7C99Uxx"
    AWS_ACCESS_SECRET_KEY="lzW5cDdY6wgCs4DifJFhoAdZHrS7s_2eq6m-0TqJ"
    VOICE_RECOGNITION_KEY = "AQVNx28rPwUX-yoQAba-HBmnOpqj9dtqW1mKQ2A2"
    def telegram_token(self):
        return self.TELEGRAM_TOKEN
    def aws_access_key(self):
        return self.AWS_ACCESS_KEY
    def aws_access_secret_key(self):
        return self.AWS_ACCESS_SECRET_KEY
    def yandex_speech_key(self):
        return self.VOICE_RECOGNITION_KEY