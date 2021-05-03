text = input(" Enter the message ")
search_word = input (" Enter the word you're trying to find ")

if  (text.find(search_word) != -1):
  print("It is found")
else:
  print("It is not found")
