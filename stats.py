def get_num_words(arr):
  return len(arr)

def get_num_letter(arr):
  letter_map = {}
  for word in arr:
    for letter in word:
      if letter.lower() in letter_map:
        letter_map[letter.lower()] += 1
      else:
        letter_map[letter.lower()] = 1
  return letter_map

def sort_on(dict):
    return dict["num"]

def sort_count(letter_count):
  list = []
  for letter in letter_count:
    if letter.isalpha():
      dict = {"char": letter, "num": letter_count[letter]}
      list.append(dict)
  list.sort(reverse=True, key=sort_on)
  return list