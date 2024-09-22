grid = []
onepositionindex = []
n = 5

# Input the grid
for _ in range(n):
    line = input("")  # Prompt for input
    row = list(map(int, line.split()))
    grid.append(row)

# Flatten the list and check counts
flattenlist = [item for row in grid for item in row]
zerocount = flattenlist.count(0)
onecount = flattenlist.count(1)

# Check for exactly one '1' in the grid
if onecount == 1:
    onepossition = flattenlist.index(1)
    
    if zerocount == 24:  # This means there should be 1 '1' and 24 '0's
        k = n
        rowindex = onepossition // n  # Calculate the row index
        colindex = onepossition % n    # Calculate the column index
        
        # Calculate rowcount and columncount
        rowcount = abs(rowindex - (n // 2))
        columncount = abs(colindex - (n // 2))
        
        print(rowcount + columncount)

