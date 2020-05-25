from sys import argv


def salary(hours, rate, bonus):
    try:
        hours, rate, bonus = int(hours), int(rate), int(bonus)
    except ValueError:
        return "Parameters can only be numbers"
    return hours * rate + bonus


name_script, h, r, b = argv

print(salary(h, r, b))
