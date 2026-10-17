
from datetime import date


first_name = input("Enter your first name: ").strip().title()
last_name = input("Enter your last name: ").strip().title()

birth_date = date(
    int(input("Birth year: ")),
    int(input("Birth month: ")),
    int(input("Birth day: "))
)

today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

message = (
    f"Hello, my name is {first_name} {last_name}.\n"
    f"I was born on {birth_date}.\n"
    f"My current age is {age}."
)

print("\n" + message)
