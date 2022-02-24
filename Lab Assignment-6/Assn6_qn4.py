"""4. Write a program that reads a string from keyboard and prints the letters in
decreasing order of frequency. Your program should convert all the input to lower
case and only count the letters a-z. Your program should not count spaces, digits,
punctuation or anything other than the letters a-z  """

text = input('Enter a sentence: ')
text=text.lower()
wdict = {}
letters = list(text)
print(letters)
for letter in letters:
  if letter!=' ' and letter in wdict:
    wdict[letter] += 1
  elif letter!=' ' and letter not in wdict:
    wdict[letter] = 1
#printing the dictionary
for key in wdict:
  print(key, wdict[key])
