grid = []
stringscount = []

for _ in range(2):
    line = input("").strip().lower()
    row = [chars for chars in line]  # Convert characters to lowercase
    stringscount.append(len(row))  # Count the characters
    grid.append(line)  # Add to grid

# Validate lengths
stringlengthvalidation = (
    stringscount[0] >= 1 and stringscount[0] <= 100 and
    stringscount[1] >= 1 and stringscount[1] <= 100
)

# Validate string counts
stringcountvalidation = stringscount[0] == stringscount[1]

if stringlengthvalidation and stringcountvalidation:
    lexicstring1 = grid[0]
    lexicstring2 = grid[1]

    if lexicstring1 == lexicstring2:
        print("0")  
    elif lexicstring1 < lexicstring2:  
        print("-1")
    else:
        print("1")
