import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password with specified criteria.
    
    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_numbers (bool): Include numbers
        use_symbols (bool): Include symbols
    
    Returns:
        str: Generated password
    """
    # Build character set based on user preferences
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one character type is selected
    if not characters:
        print("Error: At least one character type must be selected!")
        return None
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    """Get user preferences for password generation."""
    print("=== PASSWORD GENERATOR ===")
    print()
    
    # Get password length
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length >= 4:
                break
            else:
                print("Password length must be at least 4 characters.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nCharacter types to include:")
    
    # Get character type preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower().startswith('y')
    use_lowercase = input("Include lowercase letters? (y/n): ").lower().startswith('y')
    use_numbers = input("Include numbers? (y/n): ").lower().startswith('y')
    use_symbols = input("Include symbols? (y/n): ").lower().startswith('y')
    
    return length, use_uppercase, use_lowercase, use_numbers, use_symbols

def check_password_strength(password):
    """
    Check the strength of the generated password.
    
    Args:
        password (str): The password to check
    
    Returns:
        str: Strength rating
    """
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    
    if score >= 5:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Medium"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    """Main function to run the password generator."""
    while True:
        # Get user input
        length, use_uppercase, use_lowercase, use_numbers, use_symbols = get_user_input()
        
        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
        
        if password:
            # Display results
            print("\n" + "="*50)
            print("GENERATED PASSWORD:")
            print("="*50)
            print(f"Password: {password}")
            print(f"Length: {len(password)} characters")
            print(f"Strength: {check_password_strength(password)}")
            print("="*50)
            
            # Character composition analysis
            print("\nPassword Analysis:")
            print(f"Uppercase letters: {sum(1 for c in password if c.isupper())}")
            print(f"Lowercase letters: {sum(1 for c in password if c.islower())}")
            print(f"Numbers: {sum(1 for c in password if c.isdigit())}")
            print(f"Symbols: {sum(1 for c in password if c in '!@#$%^&*()_+-=[]{}|;:,.<>?')}")
        
        # Ask if user wants to generate another password
        print("\nGenerate another password? (y/n): ", end="")
        if not input().lower().startswith('y'):
            print("Thank you for using the Password Generator!")
            break
        print()

if __name__ == "__main__":
    main()
