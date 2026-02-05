def power(base, exponent=2):
    return base ** exponent

print(power(5))      # uses default exponent
print(power(5, 3))   # overrides default

output
25
125

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Sara")
output
My name is Sara and I am 25 years old.

