
"""Wordcount exercise

this has been taken from google's python class,
it is a word counter which counts the number of times each word appears in a text file and prints the results.

"""

import sys

def print_words(filename): #
  d = {}
  punctuations = r"""!()-[]{};:'"\,<>./?@#$%^&*_~"""
  with open(filename, 'r') as f:
    for line in f:
      words = line.split()

      for word in words:
        word = word.lower()
        word = word.strip(punctuations)
        for i in words:
          if i == word:
            d[word] = d.get(word, 0) + 1




  for word, count in sorted(d.items()):
    print(word, count)




def print_top(filename):
  d = {}
  punctuations = r"""!()-[]{};:'"\,<>./?@#$%^&*_~"""
  with open(filename, 'r') as f:
    for line in f:
      words = line.split()

      for word in words:
        word = word.lower()
        word = word.strip(punctuations)
        for i in words:
          if i == word:
            d[word] = d.get(word, 0) + 1

  for word, count in sorted(d.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(word, count)


def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
