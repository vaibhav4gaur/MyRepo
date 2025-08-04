#RegularExpression
#REGEX
#import re
#text validate
#match pattern

# match(pattern,string,flags)
import re
pattern = "banana"
if re.match(pattern,"banbananalereesard"):
    print("True")
else:
    print("False")


#findall(pattern, string, flags)

import re
pattern = "bornvita"
string = re.findall("bornvita",pattern)
print(string)


# search(pattern,string,flags)

import re
pattern = "apple"
if re.search(pattern,"bananaonioncarrotapple"):
    print("True")
else:
    print("False")

#match(pattern,string,flags)

import re
pattern = "carrot"
if re.match(pattern,"carrot",flags=0):
    print("true")
else:
    print("false")

#sub (pattern,repl,string,count,flags)

import re
string = "I am a dog"
pattern = "a"
print(re.sub(pattern,"batt",string,count=0,flags=0))

# CHARACTERS AND CHARACTER SEQUENCES

# ^ - Matches the beginning of a line
# $ - Matches the end of a line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non-digit
# \s - Matches whitespace
# \S - Matches any non-whitespace

import re
string = "I am a big foot 67"
pattern = "\S"
print(re.findall(pattern,string,flags=0))

# Characters and Character sequence

# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression 0 to 1 times

import re
string = "From bobby.stream@mailing.cop"
pattern = "^From (\S+@\S+)"
print(re.findall(pattern,string))

# Characters and Character sequence

# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character
# [a-z 0-9] - Set of characters can include a range
# {}

import re
string = "From aarav.mask@mail.com"
pattern = "([^ ]*)"
print(re.findall(pattern,string,flags=0))
























