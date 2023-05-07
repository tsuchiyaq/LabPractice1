import robot
import io_csv

if __name__ == "__main__":
    # インスタンスの作成
    csv_file = io_csv.IoCsv()
    # csvファイルの作成
    csv_file.create_csv()
    # csvファイルをデータフレームに変換する
    df_restaurant, row_count = csv_file.csv_to_pandas()

    # インスタンスの作成
    new_user = robot.ReseptionRobot()
    # ユーザーの名前を聞く
    new_user.greeting()

    # csv(データフレーム)のに既にあるレストランが好きか聞く
    for i in range(row_count):
        existing_restaurant_name = df_restaurant['NAME'][i]
        new_user.recommend_restaurant(df_restaurant, existing_restaurant_name, i)

    # 好きなレストランを聞く
    new_restaurant_name = new_user.ask_restaurant()
    new_user.end_conversation()

    # 聞いた好きなレストランをデータフレームに追加する
    df_restaurant = csv_file.add_restaurant(df_restaurant, new_restaurant_name)
    # データフレームをcsvに変換する
    csv_file.pandas_to_csv(df_restaurant)