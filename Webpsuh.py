class  WebPush:
    def __init__(self,platform,optin,global_frequency,start_date, end_date, language, push_type):
        self.optin=optin
        self.platform=platform
        self.global_frequency=global_frequency
        self.start_date=start_date
        self.end_date=end_date
        self.language=language
        self.push_type=push_type
        optin: bool
    def send_push(self):
        print("Push gönderildi !")

class TriggerPush(WebPush):

    pass
class BulkPush(WebPush):
    pass
class SegmentPush(WebPush):
    pass
class PriceAlertPush(WebPush):
    pass
class InstockPush(WebPush):
    pass


