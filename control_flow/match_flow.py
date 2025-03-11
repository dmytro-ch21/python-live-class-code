# status codes
status_code = 600

match status_code:
    case 100 | 101 | 102:
        print("Info")
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:  # Default Case
        print("Uknown Status Code")


weather = "snowy"

match weather:
    case "sunny":
        activity = "Go for a walk."
    case "rainy":
        activity = "Read a book."
    case "snowy":
        activity = "Build a snowman."
    case _:
        activity = "Check the forecast."

print(f"Suggested Activity: {activity}")


# cases using guards (if conditions)

# 0 - 10
# 10 - 20
# 30 - 40
# 40 - 50


num = 49
match num:
    case n if 0 < n < 10:
        print("Between 0 and 10")
    case n if 10 <= n < 20:
        print("Between 10 and 20")
    case n if 20 <= n < 30:
        print("Between 20 and 30")
    case n if 30 <= n < 40:
        print("Between 30 and 40")
    case n if 40 <= n < 50:
        print("Between 40 and 50")
    case _:
        print("Not in the range")


num = 245
match num:
    case n if n < 0:
        print("Negative")
    case 0:
        print("Zero")
    case n if n % 2 == 0:
        print("Positive Even")
    case _:
        print("Positive Odd")


