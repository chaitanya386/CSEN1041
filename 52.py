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
OUTPUT
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 1, in <module>
NameError: name 'sample' is not defined
