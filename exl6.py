print "Exercise 6: Strings and Text"
print #
# Define variable x as a string that takes in a value for the type of people.
x = "There are %d types of people." % 10
# Define variable binary as string binary
binary = "binary"
# Define variable do_not as don't
do_not = "don't"
# Define variable y as a string that takes in two different strings
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Print string with string from variable x directly WITHOUT the need for additional quotes.
print "I said: %r." % x
# Print string with string from variable y directly WITH the need for additional quotes.
print "I also said: '%s'." % y

# Define variable hilarious as a boolean.
hilarious = False
# Define variable joke_evaluation as string that will take in a string at the end of the sentence.
joke_evaluation = "Isn't that joke so funny? %r"
# Print joke_evaluation taking in input hilarious.
print joke_evaluation % hilarious

# Define variables w and e as a string
w = "This is the left side of ..."
e = "a string with a right side."

# Add strings w and e together to form a sentence. This is possible because both variables are the same type.
print w + e
