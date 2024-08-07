def personalized_greeting(first_name, last_name):
    
    if len(first_name) > 10 or len(last_name) > 10:
        return "Error: First name and last name must each be 10 characters or less."
    
   
    return f"Hello, {first_name} {last_name}! Welcome to our platform."

first_name = "aarti"
last_name = "negi"
print(personalized_greeting(first_name, last_name))
