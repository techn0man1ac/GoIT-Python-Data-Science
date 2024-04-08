words = ["banana", "apple", "cherry"]
print(f"Unsorted: {words} ") 
wordsSort = words
wordsSort.sort(key=len)
print(f"words: {words} wordsSort: {wordsSort}") 