def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)
            
def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)

def main():
    choice = "y"
    while choice.lower() == "y":
        valid_number = get_float("Enter number: ", 0, 1000)
        print("Valid number = ", valid_number)
        print()
        valid_integer = get_int("Enter integer: ", 0, 50)      
        print("Valid integer = ", valid_integer)
        print()

        choice = input("Continue (y/n)?: ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
