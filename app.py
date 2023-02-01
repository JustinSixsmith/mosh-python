import math


def increment(number, by):
    return number + by


print(increment(2, by=1))


# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Justin", "Sixsmith")


# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting("Justin")
# file = open("content.txt", "w")
# file.write(message)

# students_count = 1000
# rating = 4.9
# print(students_count)

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])

# first = "Justin"
# last = "Sixsmith"
# full = f"{first} {last}"
# print(full)

# course = "  python programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)

# x = 1
# x = 1.1
# x = 1 + 2j  # a + bi

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x += 3
# print(round(2.9))
# print(abs(-2.9))

# print(math.ceil(2.2))
# print(math.fabs(2.2))

# x = input("x: ")
# print(type(x))
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# temperature = 21
# if (temperature > 30):
#     print("It's warm")
#     print("Drink water")
# elif (temperature > 20):
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# age = 17
# if (age >= 18):
#     message = "Eligible"
# else:
#     message = "Not eligible"

# age = 17
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# high_income = False
# good_credit = True
# student = False

# if high_income or good_credit or not student:
#     print("Eligible")

# age should be between 18 and 65
# age = 22
# if 18 <= age <= 65:
#     print("Eligible")

# for number in range(1, 10, 2):
#     print("Attempt", number, (number + 1) * ".")

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# print(type(5))
# print(type(range(5)))

# for x in "Python":
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)

# for item in shopping_cart:
#     print(item)

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         print(number)
#         count += 1
# print(f"We have {count} even numbers")
