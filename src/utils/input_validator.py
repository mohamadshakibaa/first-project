def get_valid_input(start , end):
    """Get a valid integer input from the user between start and end (inclusive)."""
    
    print(" === The game starts with 100 points. You lose 5 points for each missed chance. ===")
    while True:
        try:    
            guess = int(input("Please enter your number: "))
            if start <= guess <= end :
                return guess
            else :
                print (f'Invalid number, Your number should be between {start} and {end}')
                continue
        except ValueError:
            print(f'Invalid input, Enter number between {start} and {end}')
        