import robot
import io_csv

if __name__ == "__main__":

    new_user = robot.ReseptionRobot()
    user_name = new_user.greeting()
    restaurant_name = new_user.ask_restaurant(user_name)
    new_user.end_conversation(user_name)