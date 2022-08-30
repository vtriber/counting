#import application.salary
import application.db.people
from application.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    application.db.people.get_employees()