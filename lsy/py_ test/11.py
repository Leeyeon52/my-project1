class MailSender:
    def send(self):
        print('메일 발송 준비 완료')
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class BlackBox:
    def __init__(self, name, price):   #b1. name, price/b2.name.price
        self.name = name
        self.price = price

    def hi(self):
        print('하이')
       
class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self, name, price,sd):
        super().__init__(name, price)
        self.sd = sd 
    
    def set_travel_mode(self,min):
        super().__hi()
        print(f'{self.name}{min} 분 동안 여행모드ON')

class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(f'{self.name}{min} 분 동안 여행모드ON')
        self.make()
        self.send()

b2 = TravelBlackBox('하양이',100000, 128)
b3 = AdvancedTravelBlackBox('까망이', 200000, 256)
b3.set_travel_mode(60)