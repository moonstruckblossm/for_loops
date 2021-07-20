# -------------------- Section 2 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   b. Prompt input from the user in the form of an integer. Save to a variable named size.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#   >> size... 4
#
#   $$$$
#    $$$
#     $$
#      $
#
# Write Code Below #
symbol = input("gimme symbol homie :) ")
size=int(input("gimme size homie :) "))

for i in range(size):
  print(" "*(i) + symbol*(size-i))


# 2 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#
#
# Write Code Below #
symbol = input("gimme symbol! ")
startStop = int(input("gimme number! "))
for i in range(-startStop, startStop+1):
    print(symbol*abs(i))


# 3 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#
#
# Write Code Below #
for i in range(startStop):
    print(symbol*i)

for i in range(startStop,0,-1):
  print(symbol*i)


# ---------- Part 2 | Mathematical Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 2\n'
)

# 1 - for Loop | Sum n
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate the sum of all numbers between 0 and n, and print the value.
#
#   sum = n + n - 1 + n - 2 + n - 3
#
#   EXAMPLE: 5 --> 5 + 4 + 3 + 2 + 1
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #
n = int(input("enter an integer: "))
sum = 0
for i in range(n):
  sum += n-i 

print("thee sum is:", sum)

# 1 - for Loop | n!
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate n! using loops.
#
#   n! or n factorial is equal to n * (n - 1) * (n - 2) * ... * 1
#
#   EXAMPLE: 5 --> 5 * 4 * 3 * 2 * 1
#
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #

n = int(input("enter an integer: "))
prod = 1
for i in range(n):
  prod *= n-i 

print("thee sum is:", prod)