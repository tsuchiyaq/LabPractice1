class ReseptionRobot():
    def __init__(self):
        self.user_name = None
        self.restaurant_name = None
    
    def greeting(self):
        user_name = input("こんにちは、私は受付ロボットです。あなたの名前は？")
        return user_name

    def ask_restaurant(self,user_name):
        restaurant_name = input(user_name + "さん。どこのレストランが好きですか？")
        return restaurant_name
    
    def end_conversation(self,user_name):
        print(user_name + "さん、良い一日を")