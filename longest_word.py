slova = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']
nejdelsi_slovo = ('', 0)
while slova:
    slovo = slova.pop(0)
    if len(slovo) > nejdelsi_slovo[1]:
        nejdelsi_slovo = slovo ,len(slovo)
print(nejdelsi_slovo)