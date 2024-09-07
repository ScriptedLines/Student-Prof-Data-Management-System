import random
import time

def key(characters):
    l = random.sample(characters, 15)
    pas = "".join(l)
    return pas

def get_today_date():
    return time.strftime("%Y-%m-%d", time.localtime())

def generate_password(characters):
    return key(characters)

def mainfx():
    characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
        '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
        '_', '`', '{', '|', '}', '~', ' ']

    today_date = get_today_date()
    random.seed(today_date)  
    password = generate_password(characters)

#     # After a day, generate a new password
#    # Sleep for 5 seconds for testing purposes (change to 86400 for one day)
#     next_day_date = get_today_date()
#     if next_day_date != today_date:
#         random.seed(next_day_date)  # Set the seed based on the next day's date
#         password = generate_password(characters)  # Generate a new password
    
    return password  # Return the password for today


print("Today's Password:", mainfx())
