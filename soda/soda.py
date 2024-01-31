# def your_name() :
#     print("aristde")
#     # name="clemantine"
#     # print(name)
# your_name()
def upper_lower_check():
    your_string="Aristide"

    upper_count = 0
    lower_count = 0

    for l in your_string:
        if l.isupper():
            upper_count += 1
        elif l.islower():
            lower_count += 1

    print(f"The UpperCase is: {upper_count}")
    print(f"The LowerCase is: {lower_count}")

upper_lower_check()