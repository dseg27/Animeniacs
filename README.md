# Animeniacs
## Data Analytics and Visualization Bootcamp

## FINAL PROJECT

### PROPOSAL
Group Topic: Anime. We are pursuing this topic as we are subject-matter experts on Anime and have noticed increased popularity in Anime viewership recently. There is no well-known resource currently available to recommend new anime series or to quantify or forecast trends in anime, so we’re stepping in to fill this need.

### Data Source: Kaggle CSVs

https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews 

https://www.kaggle.com/shivamb/hulu-movies-and-tv-shows 

https://www.kaggle.com/shivamb/netflix-shows 

https://www.kaggle.com/shivamb/amazon-prime-movies-and-tv-shows 

https://www.kaggle.com/shivamb/disney-movies-and-tv-shows

### Hypothesis:

We can use sentence embedding on anime and movie/show synopses to recommend animes, given someone's top five movies/shows.

### Analysis Approach:

We will use the Similarity Function (an area of supervised machine learning) to measure how similar synopses are. Reference: https://towardsdatascience.com/calculating-document-similarities-using-bert-and-other-models-b2c1a29c9630

### TECHNOLOGIES

Data Wrangling: We will use Pandas to clean and explore data. We will use Python to perform further analysis.

Database Storage: We plan to use MongoDB as it can support relational and non-relational data. We may decide to integrate images at some point, so we need a database that can handle this.

Machine Learning: We will use SciKitLearn libraries to implement a cosine_similarity function to compare text.

Visualization: We will implement our dashboard using either Flask or Github pages--TBD. We will use JavaScript and HTML to customize our dashboard. 


