def provide_hint(guess:int , actual_number:int) -> int:
    """Provide a hint based on the difference between guess and actual_number."""
    if guess < actual_number:
        return f"Your number is low, Try again"
    else :
        return f"Your number is high, Try again"