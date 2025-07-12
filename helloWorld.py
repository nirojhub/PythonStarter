print("Hello World")

'''import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0)}")
print(f"GPU: {torch.cuda.get_device_properties(0)}")
print(f"GPU: {torch.cuda.get_device_capability(0)}")'''

name = "Alice"
age = 30

# Using the old format method
old_format = "Hello, my name is {} and I am {} years old.".format(name, age)
print("Using format method:", old_format)

print()

# Using f-strings
f_string = f"Hello, my name is {name} and I am {age} years old."
print("Using f-string:", f_string)

print()

name = "Alice"
name2 = "Bob"

print(f"{name:<10}")  # Left-align within 10 characters
print(f"{name2:<10}")
print("----------")

print(f"{name:>10}")  # Right-align within 10 characters
print(f"{name2:>10}")
print("----------")

print(f"{name:^10}")  # Center-align within 10 characters
print(f"{name2:^10}")
print("----------")

print()

data = [
    {"Name": "Alice", "Age": 30, "Occupation": "Engineer"},
    {"Name": "Bob", "Age": 24, "Occupation": "Designer"},
    {"Name": "Charlie", "Age": 29, "Occupation": "Doctor"},
    {"Name": "David", "Age": 35, "Occupation": "Teacher"}
]

print(f"{'Name':<10} {'Age':<5} {'Occupation':<15}")
print("-" * 30)

for person in data:
    print(f"{person['Name']:<10} {person['Age']:<5} {person['Occupation']:<15}")

print()

x = 10
y = 5

print(f"x={x}, y={y}, x + y={x + y}") # old method

print(f"x={x}, y={y}, x + y={x + y}")

print()

number = 255
print(f"{number:b} | Binary")
print(f"{number:c} | Character")
print(f"{number:d} | Decimal")
print(f"{number:o} | Octal")
print(f"{number:x} | Hexadecimal (lowercase)")
print(f"{number:X} | Hexadecimal (uppercase)")
print(f"{number:#x} | Hexadecimal with prefix")

percentage = 0.876
print(f"{percentage:.2%} | Percentage format with 2 decimal places")

number = 12345.6789
print(f"{number:.0f} | Decimal")
print(f"{number:.2f} | Two decimal places")
print(f"{number:,.2f} | Comma as thousands separator")
print(f"{number:010.2f} | Zero-padded width 10") 
print(f"{number:+.2f} | Show sign")
print(f"{number:-.2f} | Show sign only for negative")