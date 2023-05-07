import csv
import os
import pandas as pd

class IoCsv:
    """csvの作成や入出力などを行うクラス
    """
    def __init__(self):
        self.file_path = "./restaurant.csv"

    def create_csv(self):
        if not os.path.isfile(self.file_path):
            # ファイルが存在しない場合、新しいファイルを作成する
            with open(self.file_path, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["NAME", "COUNT"])
        else:
            # ファイルが存在する場合、何もしない
            pass

    def csv_to_pandas(self):
        # csvをデータフレームに変換する
        df_restaurant = pd.read_csv(self.file_path)
        # データフレームの行数を数える
        row_count = len(df_restaurant)

        return df_restaurant, row_count

    def pandas_to_csv(self, df_restaurant):
        # データフレームをcsvに変換する
        df_restaurant.to_csv(self.file_path, index=False)
    
    def add_restaurant(self, df_restaurant, restaurant_name):
        # データフレームにレストランを追加する
        new_data = {'NAME': restaurant_name, 'COUNT': 1}
        df_restaurant = pd.concat([df_restaurant, pd.DataFrame(new_data, index=[0])])
        # インデックスのリセット
        df_restaurant = df_restaurant.reset_index(drop=True)

        return df_restaurant
    
    def count_up(self, df_restaurant, restaurant_name):
        # データフレームのカウントを更新する
        df_restaurant.loc[df_restaurant['NAME'] == restaurant_name, 'COUNT'] += 1