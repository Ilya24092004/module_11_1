import requests
import numpy as x
import pandas as pd

#первая библиотека
a = requests.get('https://urban-university.ru')
print(a)

#вторая библиотека

b = x.array(135876)
c = x.array(5625)
d = x.array(b+c)
print(d)

#третья библиотека

school = {'person' : ['Ivan','Dima','Vitalya','Ibragim'],
          'age' : [13,15,12,18],
          'mark' : [2,3,5,4]}
tb = pd.DataFrame(school)
tb