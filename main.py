import robot
import io_csv

if __name__ == "__main__":

    new_user = robot.ReseptionRobot()
    new_user.greeting()
    restaurant_name = new_user.ask_restaurant()
    new_user.end_conversation()