def greeting(name, age=28,color ='red'):
    """ 
    Greets the user and calculates their age for their next birthday.

    Args: 
        name(str) : The user's name.
        age(int) : The user's current age. Defaults to 28
        color(str) : The user's favorite color. Defaults to 'red'
    """
    # % 5 & 6 format strings
    formatted_name = name.strip().capitalize()
    formatted_color = color.strip().lower()

    # 4. calcualte age for next birthday
    next_birthday = age + 1

    # 1 and 2. Ouput messages
    print(f"\nHello {formatted_name} , you will be  {next_birthday} years old next birthday!")
    print(f"We hear you like the color {formatted_color}!")
    
if __name__ == "__main__":
    # 3. Capture input
    try:
        user_name = input ("Enter your name: ")
        user_age = input("Enter your age: ")
        user_color = input("Enter your favorite color: ")

        # Convert age to int , using the default 28 if input is empty
        age_val = int(user_age) if user_age.strip() else 28

        greeting(user_name , age_val , user_color)
    except ValueError:
        print("Error: Please enter a valid number for age. ")