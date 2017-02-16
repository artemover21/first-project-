import urllib.request
import urllib.parse
import json
def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)
def belongs_to_collection(film,films): #Проверяем серию фильмов.К примеру Пила 1 и Пила 2.
    result=dict()
    for num in films:
        if (films[num].get('belongs_to_collection')!=None):
            if films[num]['belongs_to_collection']['id']==film['belongs_to_collection']['id']:
                result[num]=num
    return result
def genres(films,result,gen,lang):
    max1=0.1    
    for num in films:
        if films[num]['genres']!=[]: #Бывает,что жанров на сайте нет
            for i,j in enumerate(films[num]['genres']): #Ищем главный жанр(Всегда стоит первым в списке)Пила-Ужасы
                if i==0:
                   genre=int(j['id'])
        if (result.get(num)==None) and (float(films[num]['vote_average'])>max1) and (genre==gen) and (lang==films[num]['original_language']): #Ищем лучший фильм по рейтингу и языку
            max_vote_film=num
    result[max_vote_film]=max_vote_film
    return result
def search_film(films,argv):
    string1=argv[1]
    for i in range(2,len(argv)):
        string1=string1+' '+argv[i]
    for num in films:
        if num==string1:
            a=films[num]
    return a
