words = ["banana", "apple", "cherry"]
print(f"Unsorted: {words} ") 
wordsSort = sorted(words, key=len)
print(f"words: {words} wordsSort: {wordsSort}") 

chars = ["banana", "apple", "cherry"]
print(f"chars: {chars}") 
chars.reverse()
print(f"reverse: {chars}") 