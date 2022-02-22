import string


# Returns a dict containing the largest pandigital and the sequence of values
# that result in the pandigital.
def pandigital(number: int) -> dict[string, string]:
    result: dict[string, string] = dict[string, string]({"pandigit": "", "sequence": ""})
    largest: int = 0
    largest_seq: list[int] = list()
    for i in range(1, number):
        temp_pandigit = ""
        temp_sequence = []
        digits: [bool] = [False, False, False, False, False, False, False, False, False]
        for j in range(1, i):
            skip = False
            product: string = str(number * j)
            for char in product:
                if char == "0":
                    skip = True
                    break
                elif not digits[int(char) - 1]:
                    digits[int(char) - 1] = True
                else:
                    skip = True
                    break
            if skip:
                continue
            temp_sequence.append(j)
            temp_pandigit += str(number * j)
            if len(temp_pandigit) >= 9:
                break
        if len(temp_pandigit) != 9:
            continue
        elif not digits.__contains__(False):
            if int(temp_pandigit) > largest:
                largest = int(temp_pandigit)
                largest_seq = temp_sequence.copy()

    result["pandigit"] = str(largest)
    result["sequence"] = largest_seq.__str__()
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_number = 0
    while user_number <= 0:
        user_number = int(input("Please enter your positive number to find the pandigital: "))
        if user_number <= 0:
            print("That is an invalid number! Please enter a number greater than zero.")

    pan_dict = pandigital(user_number)
    print(f"The largest pandigital for {user_number} is {pan_dict.get('pandigit')} with sequence "
          f"({pan_dict.get('sequence')}).")
