import sys
if len(sys.argv) == 2:
script_name = sys.argv[0]
string = sys.argv[1]
else:
script_name = sys.argv[0]
string = "madam"
print("Invalid input using default values")
if string == string[::-1]:
print(string, "is a palindrome")
else:
print(string, "is not a palindrome")
