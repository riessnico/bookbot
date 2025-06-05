from sys import argv, exit
from stats import get_num_words, get_num_letter, sort_count

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()


def main():
  if len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

  content = get_book_text(argv[1])
  num_letters = get_num_letter(content.split())
  sorted_count = sort_count(num_letters)
  print(f"============ BOOKBOT ============")
  print(f"Analyzing book found at {argv[1]}...")
  print(f"----------- Word Count ----------")
  print(f"Found {get_num_words(content.split())} total words")
  print(f"----------- Character Count ----------")
  for dict in sorted_count:
    print(f"{dict["char"]}: {dict["num"]}")
  print(f"============ END ============")

main()