mytexts =['abood','iyad','abd']

for name in list(map((lambda text : f'- {text.strip().capitalize()} -'),mytexts)):
    print(name)git add .
