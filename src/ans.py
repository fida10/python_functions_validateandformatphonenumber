""" 
Practice Question 3: Validate and Format Phone Number

Task:

Write a function format_phone_number that takes a string phone number (e.g., '1234567890') and returns a formatted version of the number (e.g., '(123) 456-7890'). If the input is not a valid phone number, the function should return None.
"""

def format_phone_number(candidate):
    if(len(candidate) == 10):
        return (f'({candidate[:3]}) {candidate[3:6]}-{candidate[6:]}')
    else:
        return None
    
    #better to have done this with regex but this will work for the requirements
