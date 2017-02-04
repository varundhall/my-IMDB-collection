# my-IMDB-collection
Python Script to create IMDB database (.csv) for user's local movie collection

Create your local movies database without using any 3rd party IMDB API, this script fetches the data directly from IMDB.

The CSV(.csv) file can be used to sort the movies on the basis of IMDB ratings, votes, release year or filter on the basis of genres, cast, producer. CSV file can be opened in LibreOffice or MSFT Excel for better readibility.

## Features

    1. Detects Accurate Movie Names from raw folders
    2. Read folder names upto two level down from current directory
    3. Fetches accurate data directly from IMDB without using any 3rd party API
    4. Creates (.csv) file with all the consolidated data

## How to use
    1. Install the dependencies
    2. Copy create-collection.py to your movies folder
    3. Execute the script
    4. Check the movies folder for list.csv which contains all accurate IMDB data with latest ratings

## Dependencies required
To use, simply:
```bash
pip install imdbpie progressbar guessit
```

## Next
- [x] Add support for reading names upto 2 level down from current directory
- [ ] Add support for reading file names
- [ ] Add support for 2+ level down from current directory
- [ ] Option to rename folders - [MovieName MovieYear MovieRatings]

## Contributions
If you have a nice idea that can further improve this script, feel free to raise a pull request :)
