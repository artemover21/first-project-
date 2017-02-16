import tmdb
import sys
import urllib.request
import urllib.parse
import json
films=dict()
filename='films.txt'
myfile=open(filename, mode='w')
i=1
summary=0
films={}
while(summary<int(sys.argv[1])):#sys.argv[1]-количество фильмов
    try:
        dictionary=tmdb.make_tmdb_api_request(method='/movie/'+str(i),api_key=''+str(sys.argv[2]))
        films[dictionary['title']]=dictionary
        summary+=1
        i+=1
    except urllib.error.HTTPError or TimeoutError or urllib.error.URLError:
        i+=1
json.dump(films,myfile)
myfile.close()
        
