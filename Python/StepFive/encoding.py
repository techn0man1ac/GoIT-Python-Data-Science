s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")
# UTF-8: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82!'
utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")
# UTF-16: b'\xff\xfe\x1f\x04@\x048\x042\x04V\x04B\x04!\x00'
cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")
# CP-1251: b'\xcf\xf0\xe8\xe2\xb3\xf2!'
s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s) # True