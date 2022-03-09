# Animeniacs
## Data Analytics and Visualization Bootcamp

## FINAL PROJECT

**https://dseg27.github.io/Animeniacs/**

### OVERVIEW
There is currently no well-known source available to recommend anime series for people to watch, so we’re stepping in to fill this need. We've hypothesized that we can use sentence embedding and scikitLearn's cosine similarity function on anime and live action show synopses to recommend animes for someone, given their favorite live-action title. 

#### **PIPELINE**

![data pipeline](https://user-images.githubusercontent.com/90593897/155247929-8042813b-66d4-485c-b34f-144b8cf215a9.png)

### Data Source: Kaggle CSVs

1. https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews 
2. https://www.kaggle.com/shivamb/hulu-movies-and-tv-shows 
3. https://www.kaggle.com/shivamb/netflix-shows 
4. https://www.kaggle.com/shivamb/amazon-prime-movies-and-tv-shows 
5. https://www.kaggle.com/shivamb/disney-movies-and-tv-shows



### TECHNOLOGIES AND FILES 

1. Data Wrangling: We used Python and Pandas to explore, clean, and analyze our data. 
**databases.ipynb**
In this file, you can see how we cleaned our data. Here are examples of how we removed titles that were missing synopses, and how we removed an innapropriate genre to make the website more family-friendly: 
![image](https://user-images.githubusercontent.com/90593897/156944928-2378f794-732c-4f36-a12a-7f0089ef6171.png)

Below, you can see how we removed titles in Spanish, removed stop words, and dropped duplicate titles: 
![image](https://user-images.githubusercontent.com/90593897/156945027-7ebfa85a-50ae-4859-a859-872c8e88ea82.png)



2. Machine Learning: We used SentenceTransformers (a Python framework) in order to implement sentence embedding on our live action and anime data. We also used this framework to implement the cosine similarity function in order to compare the live action and anime embeddings, in order to find synopses that were similar. 


**chart_data_cleaning.py**
This file contains several functions that transform our data so that it can be used to display data in the charts on our site. This file also holds the sentence embedding function which peforms sentence embedding on the live action and anime titles, and then applies the cosine similarity function to compare the live action sentence embedding and anime sentence embeddings. It then ultimately returns the five anime recommendations.

![image](https://user-images.githubusercontent.com/90593897/156944703-e65a0e56-931b-404f-abc8-4fa9093f715e.png)

![image](https://user-images.githubusercontent.com/90593897/156944746-86213352-43ec-4963-afc7-d16ab8be1ff8.png)

**model.ipynb** 
This file contains the isolated framework and implementation of the machine learning aspect of this project. Here is how recommendations were generated: 
![image](https://user-images.githubusercontent.com/90593897/156944856-46be8ace-527c-4d3a-b5e4-06e6f1f45aa0.png)




3. Data Storage: After cleaning the data and generating the necessary results from our machine learning model, we exported the final, cleaned data to CSVs and stored them in our **Final Resources** folder:
4. 
![image](https://user-images.githubusercontent.com/90593897/156945592-f9c10ccf-5334-4544-8427-6393b527f854.png)


The final CSV that holds our live action titles and the corresponding five anime recommendations (**live_actions_with_anime_recs.csv**) was then converted into a JSON file that we could use to pull data from and display on our website. This JSON file (**final.json**) was then used in our **Updated Website** folder for visualization. 


4. Visualization: 

![image](https://user-images.githubusercontent.com/90593897/156945266-65459c8f-c972-40e7-8959-ce41f6e09ef1.png)



We used HTML, JavaScript and CSS to create our own website. Our folder structure for these files lives in the **Updated Website** folder of the repo. On this site, a user can search for their favorite live action show using a drop-down menu that pulls live-action titles from our JSON file. 

![image](https://user-images.githubusercontent.com/90593897/156945288-31f7e416-f907-4103-a8b3-c557d5765903.png)

Once selected, a button is clicked that will display a list of 5 recommended animes, and the match percentage. 
![image](https://user-images.githubusercontent.com/90593897/156945306-65d3a6e7-e605-40f6-92aa-6b6be8b3858a.png)


The user can also view charts that display anime data including top ranked shows and their episode lengths, a comparison of anime and live action growth over the last two decades, as well as bar charts that compare anime and live action titles. These charts were generated using the JavaScript library, Chart.js. 

![image](https://user-images.githubusercontent.com/90593897/156945332-9e69eda1-5f27-40b8-b47e-a3edcd57f329.png)


5. Limitations & Future Improvements: 
While we had over 20,000 live action titles to work with, our website was not able to quickly load all the titles into our drop-down menu without crashing the page. Therefore, we were only able to display 1,000 live action titles for a user to choose from: 
![image](https://user-images.githubusercontent.com/90593897/156945459-fe2d224d-b8cb-4f89-9541-7d6be64a9fa5.png)


