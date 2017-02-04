#!/usr/bin/python

import os
from guessit import guessit
from imdbpie import Imdb

#Read all movie names in current directory and their immediate directories (upto one level down)
raw_movie_names = []
immediate_directories = [name for name in os.listdir(".") if os.path.isdir(name)]
raw_movie_names.extend(immediate_directories)
for each_directory in immediate_directories:
	raw_movie_names.extend([name for name in os.listdir(each_directory) if os.path.isdir(os.path.join(each_directory, name))])

#Remove duplicates (if any)
raw_movie_names = list(set(raw_movie_names))

clean_movie_names = []

for name in raw_movie_names:
	clean_movie_names.append(str((guessit(name)).get('title')))

#Remove duplicates (if any)
clean_movie_names = list(set(clean_movie_names))

#Get IMDB ratings for each movie
imdb = Imdb(anonymize=True)

for name in clean_movie_names:
	imdb_search = imdb.search_for_title(name)
	if len(imdb_search)>0:
		imdb_movie_id =  (imdb_search)[0].get('imdb_id')
		movie = imdb.get_title_by_id(imdb_movie_id)
		print str(movie.title) +"\t" + str(movie.rating)
