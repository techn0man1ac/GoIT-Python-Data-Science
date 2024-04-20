'''
Це краще працює на певні символи, якщо треба замінити слова - краще "index" + "replace"
'''
map = {ord('т'): 't', ord('ю'): 'yu', ord('Т'): 'T', ord('Ю'): 'YU'}

translated = 'ТЮтютюфафафіадщщщьют.'.translate(map)
print(translated) # TYUtyutyuфафафіадщщщьyut.