# 🐍 Python Name Formatter

A clean and efficient Python script to format a list of names using **Lambda** functions and **Map**.

## 🛠️ How it Works
The script takes a raw list of strings and applies a transformation to:
1. **Strip** any leading or trailing whitespace.
2. **Capitalize** the first letter of each name.
3. **Decorate** each entry with stylish dashes.

## 💻 The Code
```python
mytexts = ['abood', 'iyad', 'abd']

# Functional approach using map and lambda
for name in list(map((lambda text : f'- {text.strip().capitalize()} -'), mytexts)):
    print(name)
📊 Expected Output
Running the script will produce:

Plaintext
- Abood -
- Iyad -
- Abd -
🚀 Quick Start
Clone the repository.

Run the script: python main.py.

Created with ❤️ for clean Python code.
