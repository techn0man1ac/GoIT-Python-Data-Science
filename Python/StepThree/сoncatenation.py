'''
У Python, коли ви поміщаєте два рядкових літерали поруч, 
вони автоматично конкатенуються (об'єднуються в один рядок). 
Це відомо як неявна конкатенація рядків:
'''
print(("spam " "eggs") == "spam eggs") # True

one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")
print("one_line_text:", one_line_text)

'''
Неявна конкатенація рядків - це корисна особливість мови Python, 
яка дозволяє писати більш чистий і читабельний код, особливо коли 
працюєте з довгими рядками або рядками, що формуються на основі декількох частин.
'''
