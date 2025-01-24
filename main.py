def fizzbuzz(number):
    fizz = 3
    buzz = 5

    if number % (fizz * buzz) == 0:
        return "fizzbuzz"
    elif number % fizz == 0:
        return "fizz"
    elif number % buzz == 0:
        return "buzz"

    return number