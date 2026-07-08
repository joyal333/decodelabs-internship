
print("=" * 50)
print("        PASSWORD STRENGTH CHECKER")
print("=" * 50)

password = input("Enter your password: ")


length = len(password)

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# ------------------------------------------
# Score Calculation
# ------------------------------------------

score = 0

if length >= 8:
    score += 20

if length >= 12:
    score += 20

if has_upper:
    score += 20

if has_lower:
    score += 15

if has_digit:
    score += 15

if has_symbol:
    score += 10

if score >= 80:
    strength = "🟢 STRONG"

elif score >= 50:
    strength = "🟡 MEDIUM"

else:
    strength = "🔴 WEAK"


print("\n" + "=" * 50)
print("PASSWORD ANALYSIS")
print("=" * 50)

print(f"Password Length      : {length}")
print(f"Uppercase Letter     : {'✔ Yes' if has_upper else '✘ No'}")
print(f"Lowercase Letter     : {'✔ Yes' if has_lower else '✘ No'}")
print(f"Number               : {'✔ Yes' if has_digit else '✘ No'}")
print(f"Special Character    : {'✔ Yes' if has_symbol else '✘ No'}")

print("-" * 50)
print(f"Password Score       : {score}/100")
print(f"Password Strength    : {strength}")

# ------------------------------------------
# Suggestions
# ------------------------------------------

print("\nSuggestions:")

suggestion = False

if length < 12:
    print("- Use at least 12 characters.")
    suggestion = True

if not has_upper:
    print("- Add at least one uppercase letter (A-Z).")
    suggestion = True

if not has_lower:
    print("- Add at least one lowercase letter (a-z).")
    suggestion = True

if not has_digit:
    print("- Add at least one number (0-9).")
    suggestion = True

if not has_symbol:
    print("- Add at least one special character (!@#$%^&*).")
    suggestion = True

if not suggestion:
    print("- Excellent! Your password follows all recommended checks.")

print("=" * 50)
print("Thank you for using Password Strength Checker")
print("=" * 50)