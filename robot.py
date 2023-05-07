class ReseptionRobot():
    """ロボットの受け答えなどに関するクラス
    """
    def __init__(self):
        self.user_name = None
        self.restaurant_name = None
    
    def greeting(self):
        self.user_name = input("こんにちは、私は受付ロボットです。あなたの名前は？")

    def ask_restaurant(self):
        self.restaurant_name = input(self.user_name + "さん。どこのレストランが好きですか？")
        return self.restaurant_name
    
    def end_conversation(self):
        print(self.user_name + "さん、良い一日を")