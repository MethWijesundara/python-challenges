import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

all_chars = lowercase + uppercase + digits + special_chars

password_length = 12
password = ''.join(random.choice(all_chars)for x in range(password_length))
print("Your password is:",password)

#Pick one character from each category
password_chars = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special_chars)
]

# Fill the rest randomly
for x in range(password_length - 4):
    password_chars.append(random.choice(all_chars))

# shuffle the result so it's not predictable
random.shuffle(password_chars)

#convert list to string
password = ''.join(password_chars)
print("Strong password: ",password)