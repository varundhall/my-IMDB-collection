#!/usr/bin/python

import os
import csv
import progressbar
from guessit import guessit
from imdbpie import Imdb

#Create CSV file for storing the movies data
if os.path.isfile("list.csv"):
    os.remove("list.csv")

#Read all movie names in current directory and their immediate directories (upto one level down) - only reading folder names right now

raw_movie_names = []

print "Reading your local directory for movies\n"

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

print "Found : " + str(len(clean_movie_names)) + " movies in your collection\n"

print "Please wait...we are fetching limited data from IMDB\n"

print "Sit back and relax...we are working on your collection\n"

#Use Progressbar to tell user about the progress

bar = progressbar.ProgressBar(maxval=len(clean_movie_names), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

bar.start()
i = 0

#Get IMDB ratings for each movie

imdb = Imdb(anonymize=True)

f = open('list.csv', 'wt')
writer = csv.writer(f)
writer.writerow( ('Movie Title','IMDB Ratings','No. of Votes','Genres','Release Date','Cast','Director','Writer','Plot Outline') )

for name in clean_movie_names:
	imdb_search = imdb.search_for_title(name)
	if len(imdb_search)>0:
		imdb_movie_id =  (imdb_search)[0].get('imdb_id')
		movie = imdb.get_title_by_id(imdb_movie_id)
		cast_summary = []
		for person in movie.cast_summary:
			cast_summary.append(person.name)
		directors_summary = []
		for person in movie.directors_summary:
			directors_summary.append(person.name)
		writers_summary = []
		for person in movie.writers_summary:
			writers_summary.append(person.name)
		writer.writerow( ( movie.title, movie.rating, movie.votes, (",".join(movie.genres)), movie.release_date, (",".join(cast_summary)), (",".join(directors_summary)), (",".join(writers_summary)), movie.plot_outline ) )
	i = i+1	
	bar.update(i)

f.close()
bar.finish()

print "We have consolidated the data.\nGo ahead and check list.csv"
