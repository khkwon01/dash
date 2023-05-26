# list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits), max(digits), sum(digits))

# tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# if
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


# object nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# user input
message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# while
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# function..
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# classes
class Dog:   # inheritance   class PuddleDog(Dog):
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# file
from pathlib import Path
path = Path('pi_digits.txt')
#path = Path('/home/eric/data_files/text_files/filename.txt')
contents = path.read_text(encoding='utf-8')
contents = contents.rstrip()
print(contents)

from pathlib import Path
import json

try:

    numbers = [2, 3, 5, 7, 11, 13]

    path = Path('programming.txt')
    path.write_text("I love programming.")

    path = Path('numbers.json')
    contents = json.dumps(numbers)
    path.write_text(contents)

except Exception as e:
    print(f"error : {str(e)}")


# testing your code : pytest
