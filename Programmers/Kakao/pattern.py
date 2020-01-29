import re

# m = re.match('^(.+?)(?=\1*$)', "ababcdcdababcdcd")
# print(m.group())
# print(bool(m))


# import re
#
# def ReplaceThreeOrMore(s):
#     # pattern to look for three or more repetitions of any character, including
#     # newlines.
#     pattern = re.compile(r"(.)\1{2,}", re.DOTALL)
#     return pattern.sub(r"\1\1", s)
#
# ReplaceThreeOrMore




pattern = re.compile(r"(\w)\1+")

# a function to perform the substitution we need:
def repl(matchObj):
   char = matchObj.group(1)
   return "%s%s" % (char, char)

print(pattern.sub(repl, "ababcdcdababcdcd"))

