import random
import string

def generate(length):
    chars = string.ascii_letters + string.digits + string.punctuation

    passwd = ''.join(random.choice(chars) for _ in range(length))
    
    return passwd

def main():
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length must be greater than 0.")
            return
        
        passwd = generate(length)
        
        print("Generated Password:", passwd)
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
