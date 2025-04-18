# Palindrome Checker

n = input("Sentence or Word: ")

ob = n.lower()
bo = "".join(reversed(ob))

if ob == bo:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")