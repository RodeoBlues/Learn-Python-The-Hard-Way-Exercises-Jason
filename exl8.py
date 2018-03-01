print "Exercise 8: Printing, Printing"
print #
# Define variable formatter as a string that takes in four inputs from the user.
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

# Mix of double-quotes and single-quotes is printed in the output sometimes because it picks the most efficient way to do it.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
