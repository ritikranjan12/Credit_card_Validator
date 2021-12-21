def credit():
    card_no = input("YOUR CARD NUMBER: ")
    odd_sum = 0
    even_sum = 0
    double_value = []
    number = list(card_no)
    for (idx, val) in enumerate(number):
        if idx % 2 != 0:  # this is an odd number
            odd_sum += int(val)
        else:  # this is an even no.
            double_value.append(2 * int(val))

    # converting the list into string
    double_string = ""
    for x in double_value:
        double_string += str(x)

    # converting string into list
    double_value = list(double_string)
    for x in double_value:
        even_sum += int(x)

    # total sum
    sum = odd_sum + even_sum
    if sum % 10 == 0:
        print("This is a Valid Card NUMBER")
    else:
        print("Invalid Card NUMBER")

if __name__=='__main__':
    credit()