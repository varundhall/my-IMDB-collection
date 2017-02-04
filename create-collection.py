#!/usr/bin/python

import os
from guessit import guessit

#Read all movie names in current directory and their immediate directories (upto one level down)
raw_movie_names = []
immediate_directories = [name for name in os.listdir(".") if os.path.isdir(name)]
raw_movie_names.extend(immediate_directories)
for each_directory in immediate_directories:
	raw_movie_names.extend([name for name in os.listdir(each_directory) if os.path.isdir(os.path.join(each_directory, name))])

#Remove duplicates (if any)
raw_movie_names = list(set(raw_movie_names))

for name in raw_movie_names:
	print (guessit(name)).get('title')

