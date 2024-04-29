text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print("text:", text)
print("song:", song)

'''
Коли інтерпретатор виявляє лапки, повторені 
тричі, він сприймає усі символи до наступних 
трьох лапок, які закривають рядок, як символи рядка.
'''

one_line_text0 = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print("one_line_text0:", one_line_text0) # однією стрічкою

one_line_text1 = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
print("one_line_text1:", one_line_text1) # однією стрічкою але з перенесенням в коді за допомогою "\"