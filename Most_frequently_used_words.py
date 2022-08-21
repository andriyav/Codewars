import re
import numpy as np
import pandas as pd
def top_3_words(text):
    text = text.lower()
    text_mod = []
    pattern = re.compile(r'(\'?[a-z0-9]*\'?[a-z0-9]+\'?)') #регулярний вираз для фільтрації непотрібних символів
    matches = pattern.finditer(text)
    for i in matches:
        text_mod.append(i[0])
    df = pd.value_counts(np.array(text_mod)) #пошук однакових слів та визначення їх кількості
    index = 0
    list_item = []
    item = []
    while len(df) > index:
        item.append(df.values[index])
        item.append(df.index[index])
        list_item.append(item)
        item = []
        index += 1
    list_item.sort(key=lambda k: (-k[0], k[1])) #сортування за кількістью та алфавітом
    list_first_three = list_item[:3] #зріз перших трьох елементів листа
    result = []
    for item in list_first_three:
        result.append(item[1]) #добавлення в результат найбільш повторювальних слів без їх кількості
    return result

text = """In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""

top_3_words(text)
