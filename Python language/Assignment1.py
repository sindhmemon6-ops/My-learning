# Assignment no 1: Python String Methods
# Three variables, all taken from user input
print("=" * 50)
print("        PYTHON STRING METHODS PRACTICE")
print("=" * 50)
 
# ---------- Step 1: Take input for 3 variables ----------
name = input("Enter your name (try extra spaces, e.g. '  saeed ahmed  '): ")
sentence = input("Enter a sentence (e.g. 'python is fun and python is easy'): ")
code = input("Enter a code or number (e.g. 12345 or abc123): ")
 
print("\nYou entered:")
print("name     =", repr(name))
print("sentence =", repr(sentence))
print("code     =", repr(code))
 
# ---------- Step 2: Case methods ----------
print("\n--- CASE METHODS ---")
print("upper():     ", name.upper())
print("lower():     ", name.lower())
print("title():     ", sentence.title())
print("capitalize():", sentence.capitalize())
print("swapcase():  ", name.swapcase())
print("casefold():  ", name.casefold())
 
# ---------- Step 3: Whitespace removal ----------
print("\n--- STRIP METHODS ---")
print("strip():  ", repr(name.strip()))
print("lstrip(): ", repr(name.lstrip()))
print("rstrip(): ", repr(name.rstrip()))
 
# ---------- Step 4: Replace, split, join ----------
print("\n--- REPLACE / SPLIT / JOIN ---")
print("replace():", sentence.replace("python", "Java"))
words = sentence.split()
print("split():  ", words)
print("join():   ", "-".join(words))
print("join() on code characters:", ",".join(code))
 
# ---------- Step 5: Searching ----------
print("\n--- SEARCH METHODS ---")
search_word = sentence.split()[0] if sentence.split() else ""
print("Searching for:", repr(search_word))
print("find():       ", sentence.find(search_word))
print("find() missing word 'xyz':", sentence.find("xyz"))  # returns -1
 
# index() raises an error if not found, so we check first
if search_word in sentence:
    print("index():      ", sentence.index(search_word))
else:
    print("index():       word not found")
 
print("count():      ", sentence.count(search_word))
print("startswith('p'):", sentence.startswith("p"))
print("endswith('y'):  ", sentence.endswith("y"))
 
# ---------- Step 6: Checking methods ----------
print("\n--- CHECK METHODS ---")
clean_name = name.strip()
print("name.isalpha():    ", clean_name.replace(" ", "").isalpha())
print("code.isdigit():    ", code.isdigit())
print("code.isalnum():    ", code.isalnum())
print("name.isspace():    ", name.isspace())
print("name.islower():    ", name.islower())
print("name.isupper():    ", name.isupper())
print("sentence.istitle():", sentence.istitle())
 
# ---------- Step 7: Alignment and padding ----------
print("\n--- ALIGNMENT METHODS ---")
print("center():", clean_name.center(30, "*"))
print("ljust(): ", clean_name.ljust(30, "-") + "|")
print("rjust(): ", clean_name.rjust(30, "-"))
print("zfill(): ", code.zfill(10))
 
# ---------- Step 8: Partition ----------
print("\n--- PARTITION METHODS ---")
print("partition(' '):  ", sentence.partition(" "))
print("rpartition(' '): ", sentence.rpartition(" "))
 
print("\n" + "=" * 50)
print("               END OF PROGRAM")
print("=" * 50)
