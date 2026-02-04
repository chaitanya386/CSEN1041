sample = "   hello python world   "
print("Original sample: '", sample, "'", sep="")

# strip: remove leading/trailing spaces
print("strip()       -> '", sample.strip(), "'", sep="")

# upper and lower
print("upper()       ->", sample.upper())
print("lower()       ->", sample.lower())

# replace
print("replace('python', 'Java') ->", sample.replace("python", "Java"))

# split (by whitespace)
words = sample.strip().split()
print("split() ->", words)

# join
joined = "-".join(words)
print("'-'.join(words) ->", joined)

# find
print("find('python') ->", sample.find("python"))

# count
print("count('l') ->", sample.count("l"))

# startswith / endswith
print("startswith('   he') ->", sample.startswith("   he"))
print("endswith('world   ') ->", sample.endswith("world   "))

# isalpha / isdigit (after stripping spaces)
only_letters = "HelloWorld"
only_digits = "12345"
print("'HelloWorld'.isalpha() ->", only_letters.isalpha())
print("'12345'.isdigit() ->", only_digits.isdigit())
output
Original sample: '   hello python world   '
strip()       -> 'hello python world'
upper()       ->    HELLO PYTHON WORLD   
lower()       ->    hello python world   
replace('python', 'Java') ->    hello Java world   
split() -> ['hello', 'python', 'world']
'-'.join(words) -> hello-python-world
find('python') -> 9
count('l') -> 3
startswith('   he') -> True
endswith('world   ') -> True
'HelloWorld'.isalpha() -> True
'12345'.isdigit() -> True
