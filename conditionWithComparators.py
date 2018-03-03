def personIdentification(age):
    if age < 2:
        return "The Person is a Baby"
    elif 2 <= age < 4:
        return "The Person is Teddler"
    elif 4 <= age < 13:
        return "The Person is Kid"
    elif 13 <= age < 20:
        return "The Person is Teenager"
    elif 20 <= age < 65:
        return "The Person is Adult"
    elif age >= 65:
        return "The Person is an Older"


print(personIdentification(10))


def salaryIncrementEligiblity(salary, age, maritalStatus):
    if age > 20 and age < 60 and salary < 20000*4 and maritalStatus == 'married':
        return True
    else:
        return False

print(salaryIncrementEligiblity(10000,25,"married"))


