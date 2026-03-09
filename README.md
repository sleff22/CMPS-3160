# Kaggle Steam Games Data Sets

Our Colab notebook can be found [here](https://colab.research.google.com/drive/1tx-s_51ZsaE76XxECL3M3WFzYNSwJpXq?usp=sharing)

I uploaded the parser, two cleaned data sets, and the overall full data set in JSON format.
Both Kaggle_Cleaned_Sets are CSV files with the following labels:

`[appID, name, release_date, price, supported_languages, developers, publishers, categories, genres, tags, metacriticScore]`

## Data Filtering Process

I filtered out all the games that didn't support English since their entries weren't interpreted well in unicode and became gibberish.
The first set involves all games as long as they support English, have a price that is not 0, and have a metacritic score.
The second data set is the set of all games with price 0, but still support English and have a metacritic score.

I chose these metrics as a simple way to filter out entries that weren't real games, didn't use characters that unicode could interpret, or were otherwise unuseful datapoints.

The full games.csv file was too large to load into Colab and GitHub, so it is currently being hosted on GIT's large file system and will not display the raw values on this repository.
