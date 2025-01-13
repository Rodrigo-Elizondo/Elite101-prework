print('Hi welcome you out chat room this is our chatbot ')

from datetime import datetime

birthday_YMD = input("Please enter your birthday (YYYY-MM-DD): ")

birthday = datetime.strptime(birthday_YMD, "%Y-%m-%d")

today = datetime.today()

age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

print(f"You are {age} years old.")
