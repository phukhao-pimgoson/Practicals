COLOUR_CODES = {"000000": "Black", "FFFFFF": "White", "7F7F7F": "Gray50", "FF0000": "Red1", "00FF00": "Green1",
                "0000FF": "Blue1", "FFFF00": "Yellow1", "FF00FF": "Magenta1", "00FFFF": "Cyan1", "A020F0": "purple1"}


def main():
    print(COLOUR_CODES)
    user_code = (input("Enter colour code: ")).upper()
    while user_code != "":
        if user_code in COLOUR_CODES:
            print(user_code, "is", COLOUR_CODES[user_code])
        else:
            print("Code does not exist in dictionary")
        user_code = input("Enter colour code: ")


main()
