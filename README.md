# Kaggle Steam Games Data Sets

I uploaded the parser, two cleaned data sets, and the overall full data set in JSON format.
Both Kaggle_Cleaned_Sets are CSV files with the following labels:

`[appID, name, release_date, price, supported_languages, developers, publishers, categories, genres, tags, metacriticScore]`

## Data Filtering Process

I filtered out all the games that didn't support English since their entries weren't interpreted well in unicode and became gibberish.
The first set involves all games as long as they support English, have a price that is not 0, and have a metacritic score.
The second data set is the set of all games with price 0, but still support English and have a metacritic score.

I chose these metrics as a simple way to filter out entries that weren't real games, didn't use characters that unicode could interpret, or were otherwise unuseful datapoints.
