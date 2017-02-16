import json
import tmdb
import sys
filename='films.txt'
myfile=open(filename,mode='r')
films=json.load(myfile)
film=tmdb.search_film(films,sys.argv)#Ищем атрибуты фильма
dict1=tmdb.belongs_to_collection(film,films)
for i,j in enumerate(film['genres']): #Ищем основной жанр
    if i==0:
        film_gen=int(j['id'])
for i in range(3):
    dict1=tmdb.genres(films,dict1,film_gen,film['original_language']) #Добавляем еще 3 фильма в рекомендации
del dict1[film['title']]
for num in dict1:
    print(num)
myfile.close()
