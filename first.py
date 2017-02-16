import tmdb
import sys
saw_budget=tmdb.make_tmdb_api_request(method='/movie/'+str(sys.argv[1]),api_key=''+str(sys.argv[2]))['budget']
print(saw_budget)
