# Read the two strings
string1 = "ttXjenUAlfixytHEOrPkgXmkKTSGYuyVXGIHYmWWYGlBYpHkujueqBSgjLguSgiMGJWATIGEUjjAjKXdMiVbHozZUmqQtFrT"
string2 = "JziDBFBDmDJCcGqFsQwDFBYdOidLxxhBCtScznnDgnsiStlWFnEXQrJxqTXKPxZyIGfLIToETKWZBPUIBmLeImrlSBWCkTNo"

# Convert both strings to lowercase for case-insensitive comparison
lower_string1 = string1.lower()
lower_string2 = string2.lower()

# Compare the two strings
if lower_string1 < lower_string2:
    print("-1")
elif lower_string1 > lower_string2:
    print("1")
else:
    print("0")

