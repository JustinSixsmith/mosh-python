import math
from collections import deque
from array import array


point = {"x": 1, "y": 2}
point = dict(x=1, y=1)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del (point["x"])
print(point)
for key, value in point.items():
    print(key, value)


# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print("yes")


# numbers = array("i", [1, 2, 3])

# x = 10
# y = 11

# x, y = y, x

# print("x", x)
# print("y", y)


# point = (1, 2, 3)
# print(point[0:2])
# x, y, z = point
# print(y)


# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.append(5)
# queue.popleft()
# print(queue)
# if not queue:
#     print("Empty")


# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# browsing_session.append(4)
# browsing_session.append(5)
# for number in range(len(browsing_session)):
#     browsing_session.pop()
#     if browsing_session:
#         print(browsing_session[-1])


# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip("abc", list1, list2)))


# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]


# prices = list(map(lambda item: item[1], items))
# print(prices)
# prices = [item[1] for item in items]


# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)
# filtered = [for item in items if item[1] >= 10 ]


# items.sort(key=lambda item: item[1])
# print(items)


# numbers = [3, 51, 2, 8, 6]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)


# letters = ["a", "b", "c"]
# print(letters.count("d"))
# if "d" in letters:
#     print(letters.index("d"))


# letters.append("d")
# letters.insert(0, "-")
# print(letters)

# letters.pop(0)
# letters.remove("b")
# del letters[0:3]
# letters.clear()
# print(letters)


# for index, letter in enumerate(letters):
#     print(index, letter)


# numbers = [1, 2, 3, 4, 4, 4, 4, 4]
# first, *other, last = numbers
# print(first, last)
# print(other)


# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-1])


# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0:3])
# print(letters[::2])


# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(len(chars))


# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input


# print(fizz_buzz(7))


# def greet():
#     message = "a"

# print(name)


# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="John", age=22)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#         return total


# print("Start")
# print(multiply(1, 2, 3))


# print(multiply(2, 3, 4, 5))


# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))


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
