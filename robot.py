class ReseptionRobot():
    def __init__(self):
        self.name = None
    
    def greeting(self):
        print("こんにちは、私は受付ロボットです。あなたの名前は？")

    def ask_restaurant(self):
        print(self.name + "さん。どこのレストランが好きですか？")

    def set_name(self, name):
        self.name = name
        print(self.name + "さん。どこのレストランが好きですか？")
    