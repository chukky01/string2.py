#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  if len(s) < 3:
    return s
  elif len(s) <= 3:
    return s + "ing"
  elif s.endswith("ing"):
    s = s.replace("ing", "ly")
    return s

  return

if __name__ == "__main__":
  s = input("give me a string: ")

  result = verbing(s)
  print(result)




# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  not_index = s.find('not')
  bad_index = s.find('bad')

  if not_index != -1 and bad_index != -1 and bad_index > not_index:
    s = s[:not_index] + 'good' + s[bad_index + 3:]


  return s

if __name__ == '__main__':
  s = input("Give a sentence with the words 'not' and 'bad' in it: ")

  result = not_bad(s)
  print(result)


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  a_mid = (len(a) + 1) // 2
  b_mid = (len(b) + 1) // 2

  a_front = a[:a_mid]
  a_back = a[a_mid:]

  b_front = b[:b_mid]
  b_back = b[b_mid:]

  return a_front + b_front + a_back + b_back




if __name__ == '__main__':
  a = input('give me a random string: ')
  b = input('give me another string: ')

  result = front_back(a, b)
  print(result)



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  return ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


if __name__ == '__main__':
  got = input("Enter any prefix of your choice: ")
  expected = input("Enter the expected prefix of the word: ")

  result = test(got, expected)
  print(result)




# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
