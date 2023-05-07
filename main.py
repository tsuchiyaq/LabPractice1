import robot
import io_csv

if __name__ == "__main__":
    user_name = robot.ReseptionRobot.greeting()
    restaurant_name = robot.ReseptionRobot.ask_restaurant(user_name)
    robot.ReseptionRobot.end_conversation(user_name)