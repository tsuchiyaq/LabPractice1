import io_csv

class ReseptionRobot():
    """ロボットの受け答えなどに関するクラス
    """
    def __init__(self):
        self.user_name = None
        self.new_restaurant_name = None
    
    def greeting(self):
        # 名前を聞く
        self.user_name = input("こんにちは、私は受付ロボットです。あなたの名前は？")

    def ask_restaurant(self):
        # 好きなレストランを聞く
        self.new_restaurant_name = input(self.user_name + "さん。どこのレストランが好きですか？")
        return self.new_restaurant_name
    
    def recommend_restaurant(self, df_restaurant ,existing_restaurant_name, i):
        # データフレームにあるレストランが好きか聞く
        print(self.user_name + "さん。" + existing_restaurant_name + "がおすすめです。")
        answer = input(self.user_name + "さんは好きですか？")
        if answer == "Yes":
            io_csv.IoCsv().count_up(df_restaurant, existing_restaurant_name)
    
    def end_conversation(self):
        print(self.user_name + "さん、良い一日を")