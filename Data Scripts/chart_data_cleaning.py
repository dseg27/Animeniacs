import pandas as pd
from langdetect import detect
from sortedcontainers import SortedDict
from sentence_transformers import SentenceTransformer, util

# Function to split the live action dataframe and return 4 individual DFs. One for each platform
def splitLiveActionDF(f_df):
    n_df = f_df.loc[f_df['source'] == 'Netflix']
    am_df = f_df.loc[f_df['source'] == 'Amazon']
    d_df = f_df.loc[f_df['source'] == 'Disney']
    h_df = f_df.loc[f_df['source'] == 'Hulu']

    return n_df,am_df,d_df,h_df

# A function to clean up the genre string provided within the dataframe. Removes compromising characters.
def genreList(genre_string):
        genre_string = genre_string.replace('[','')
        genre_string = genre_string.replace(']','')
        genre_string = genre_string.replace("'",'')
        genre_list = list(genre_string.split(', '))

        return genre_list

# Produces a count of the top 5 anime genre categories for the df provided into the function. Picks out these specific genres for the non-anime DFs
def formatGenreCount(df,source):
    genre_df_top = df[['Comedy','Action','Fantasy','Adventure','Drama']]
    genre_df_top = genre_df_top.count()
    genre_count_df = pd.DataFrame({'Genre': genre_df_top.index, source: genre_df_top.values})
    return genre_count_df

# Reformats NetFlix genre categories since they have a couple genres combined and split based on TV vs Movie
def reformatNetflixGenre(genre_df):
    for index, row in genre_df.iterrows():
        if row['TV Action & Adventure'] == '1':
            genre_df.loc[index,'Action'] = '1'
            genre_df.loc[index,'Adventure'] = '1'
        elif row['Action & Adventure'] == '1':
            genre_df.loc[index,'Action'] = '1'
            genre_df.loc[index,'Adventure'] = '1'

        if row['TV Comedies'] == '1':
            genre_df.loc[index,'Comedy'] = '1'
        elif row['Comedies'] == '1':
            genre_df.loc[index,'Comedy'] = '1'

        if row['TV Sci-Fi & Fantasy'] == '1':
            genre_df.loc[index,'Fantasy'] = '1'
        elif row['Sci-Fi & Fantasy'] == '1':
            genre_df.loc[index,'Fantasy'] = '1'

        if row['TV Dramas'] == '1':
            genre_df.loc[index,'Drama'] = '1'
        elif row['Dramas'] == '1':
            genre_df.loc[index,'Drama'] = '1'
    return genre_df 

# Reformats Disney genre categories since they combine Action and Adventure into one genre
def reformatDisneyGenre(genre_df):
    for index, row in genre_df.iterrows():
        if row['Action & Adventure'] == '1':
            genre_df.loc[index,'Action'] = '1'
            genre_df.loc[index,'Adventure'] = '1'

    return genre_df 

# produces genre counts for the Anime df
def genreAnimeCount(df,id,genreCol):
    # create a subset df of just genre and anime ID
    genre_df = df[[id,genreCol]]
    # Create a blank list to be used to store unique genre values in genre string
    unique_list = []
    # Loop through genre df row by row to split genre string into list of unique values
    for index, row in genre_df.iterrows():
        genre_list = genreList(row[genreCol])
        # Populate list of unique values
        for x in genre_list:
            if x not in unique_list:
                unique_list.append(x)
        # Use list of unique values to create columns if they don't exist and populate a value of 1 if they do exist   
        for x in genre_list:
            if x in unique_list:
                genre_df.loc[index,x] = '1'
    return genre_df

def genreLiveCount(df,id,genreCol):
    # Store the source as a variable
    source = list(df.iat[0,0])
    # create a subset df of just genre and show ID
    genre_df = df[[id,genreCol]]
    # Create a blank list to be used to store unique genre values in genre string
    unique_list = []
    # Loop through genre df row by row to split genre string into list of unique values
    for index, row in genre_df.iterrows():
        genre_list = genreList(row[genreCol])
        # Populate list of unique values
        for x in genre_list:
            if x not in unique_list:
                unique_list.append(x)
        # Use list of unique values to create columns if they don't exist and populate a value of 1 if they do exist        
        for x in genre_list:
            if x in unique_list:
                genre_df.loc[index,x] = '1'
    # Change genre name of Science Fiction to Fantasy if Hulu since Hulu does not have a Fantasy category
    if source[0] == 'h':
        genre_df = genre_df.rename(columns={'Science Fiction': 'Fantasy'})
    # Reformat Disney genre. This is redundant and could be replaced by correcting function above
    if source[0] == 'd':
        genre_df = genre_df.rename(columns={'Action-Adventure': 'Action & Adventure'})
        genre_df = reformatDisneyGenre(genre_df)
    # Send Netflix df to be reformatted with function above
    elif source[0] == 'n':
        genre_df = reformatNetflixGenre(genre_df)  
    # Amazon DF does not require reformatting          
    return genre_df

# Test function used for troubleshooting genre counting issues across multiple platforms. See genreLiveCount() for explanation of process
def genreLiveCountTest(df,id,genreCol):

    source = list(df.iat[0,0])
    print(source[0])
    genre_df = df[[id,genreCol]]
    unique_list = []

    for index, row in genre_df.iterrows():
        genre_list = genreList(row[genreCol])

        for x in genre_list:
            if x not in unique_list:
                unique_list.append(x)
                
        for x in genre_list:
            if x in unique_list:
                genre_df.loc[index,x] = '1'

    if source[0] == 'h':
        genre_df = genre_df.rename(columns={'Science Fiction': 'Fantasy'})

    if source[0] == 'd':
        genre_df = genre_df.rename(columns={'Action-Adventure': 'Action & Adventure'})
        
    #genre_df = reformatLiveGenre(genre_df)            
    return genre_df

# Test function used for troubleshooting genre counting issues across multiple platforms. See masterGenre() for explanation of logic
def masterGenreTest(f_df):
    n_df,am_df,d_df,h_df = splitLiveActionDF(f_df)

    am_genre_df = genreLiveCountTest(am_df,'show_id','listed_in')
    d_genre_df = genreLiveCountTest(d_df,'show_id','listed_in')
    h_genre_df = genreLiveCountTest(h_df,'show_id','listed_in')

    am_genre_df.to_csv('coles_practice/csv/amazon_genres.csv', index=False)
    h_genre_df.to_csv('coles_practice/csv/disney_genres.csv', index=False)
    d_genre_df.to_csv('coles_practice/csv/hulu_genres.csv', index=False)

# The master function for genre count process. Sequentially kicks off all necessary functions for producing genre count csv used on site
def masterGenre(a_df,f_df):
    # Calls the split of live action function
    n_df,am_df,d_df,h_df = splitLiveActionDF(f_df)
    # Calls the count function for each live action df
    n_genre_df = genreLiveCount(n_df,'show_id','listed_in')
    am_genre_df = genreAnimeCount(am_df,'show_id','listed_in')
    d_genre_df = genreLiveCount(d_df,'show_id','listed_in')
    h_genre_df = genreLiveCount(h_df,'show_id','listed_in')
    # calls for the reformatting of the genre counts for each live action df
    n_genre_counts = formatGenreCount(n_genre_df,'netflix')
    am_genre_counts = formatGenreCount(am_genre_df,'amazon')
    d_genre_counts = formatGenreCount(d_genre_df,'disney')
    h_genre_counts = formatGenreCount(h_genre_df,'hulu')
    # Runs the genre count and formatting of the Anime df
    a_genre_df = genreAnimeCount(a_df,'uid','genre')
    anime_genre_counts = formatGenreCount(a_genre_df,'Anime')
    # Merge all formatted genre count DFs into one and reorder them into the necessary order
    merged_genre_counts = anime_genre_counts.merge(n_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.merge(am_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.merge(d_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.merge(h_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.rename(columns={'Anime':'anime','Genre':'source'})
    merged_genre_counts = merged_genre_counts[['source','netflix','hulu','amazon','disney','anime']]
    # Save the merged DF into necessary folder to display on site
    merged_genre_counts.to_csv('Updated Website/chart_data/top5genres_stack.csv',index=False)

# Attempt to implement a language detection to exclude non-english. Found that only amazon provided non-english descriptions for their non-english shows. 
# Other platform just used english making this unnecessary.
def langDetect(df):
    for index, row in df.iterrows():
        descr = row['description']

        try: 
            descr_lang = detect(descr)
        except:
            descr_lang = 'nd'
        
        df.loc[index,'lang'] = descr_lang

    df = df[df['lang'] == 'en']

    return df
# Produces csv of movie and show count for the site
def movieVSshow(a_df,l_df):
    # create a count column on live action df
    l_df['count'] = '1'
    # Use a for loop for Anime count since Anime df has no Type column 
    for index, row in a_df.iterrows():
        # Designate rows with only 1 episode as a movie
        a_df.loc[index,'source'] = 'Anime'
        if row['episodes'] == 1.0:
            a_df.loc[index,'type'] = 'Movie'
        # Designate rows with more than 1 episode as a show
        else:
            a_df.loc[index,'type'] = 'TV Show'
        # Assign row with a count of 1
        a_df.loc[index,'count'] = '1'
    # Create shortened anime and live action DFs with only necessary columns for csv
    a_df_short = a_df[['source','type','count']]
    l_df_short = l_df[['source','type','count']]
    # Concatenate shortened DFs into one
    frames = [a_df_short,l_df_short]
    c_df = pd.concat(frames)
    # Group by source and type, rename column to count and reset the index to create a flat df
    c_df_group = c_df.groupby(['source','type']).agg({'count': ['count']})
    c_df_group.columns = ['count']
    c_df_group = c_df_group.reset_index()
    # Pivot the group by df to make the rows into the columns and the columns into the rows
    c_df_pivot = c_df_group.pivot(index='source',columns='type')
    c_df_pivot = c_df_pivot.reset_index()
    c_df_pivot.columns = ['source','count_movie','count_show']
    # Export pivoted table to necessary file location for use on site
    c_df_pivot.to_csv('Updated Website/chart_data/movie_vs_show_count.csv', index=False)

# Create scatter csv of top 51 anime titles
def scatterCSV(a_df):
    a_df = a_df.loc[a_df['ranked'] < 51]
    a_df = a_df[['title','episodes','score']]
    a_df.to_csv('Updated Website/chart_data/chart_anime.csv', index=False)

# Create csv for the timeseries chart on site
def getTimeseries(a_df,l_df):
    # Exclude everything pre-1999 from live action df, group by year, reset index to create flat df, count number of shows in year, and rename columns to necessary names
    l_df = l_df.loc[l_df['release_year'] > 1999]
    l_count = l_df.groupby('release_year').count()
    l_count = l_count.reset_index()
    l_count = l_count[['release_year','show_id']]
    l_count.columns = ['release_year','count_live_actions']
    # Drop anime titles where release year is unknown
    a_df = a_df.loc[a_df['aired'] != 'Not available']
    # Split the anime release year string with date would read something like Oct 11, 2007 to Oct 11, 2017
    for index,row in a_df.iterrows():
        date_list = list(row['aired'].split(' to '))
        # Capture the release date prior to the 'to' in the string
        a_df.loc[index,'release_date'] = date_list[0]
    # Since release date has two different formatting styles for loop to address this row by row
    for index, row in a_df.iterrows():
        # Identify whether the release_date column has a value like Oct 11, 2007 or 11-Oct-2007
        a_df.loc[index,'date_is_str'] = row['release_date'][0]
        a_df.loc[index,'is_date_str'] = row['release_date'][0].isnumeric()
        # If the string is formatted like Oct 11,2007 split the string at the comma space and store the year in release_year column
        if row['release_date'][0].isnumeric() == False:
            date_year = list(row['release_date'].split(', '))
            a_df.loc[index,'release_year'] = date_year[1]
        # If the string is formatted like 2007 (just the year) store the year in release_year
        elif row['release_date'][0].isnumeric() == True and len(row['release_date']) == 4:
            a_df.loc[index,'release_year'] = row['release_date']
        # If the string is formatted like 11-Oct-2007 split at - and capture the year (3 value in list) store in release_year column
        else:
            date_year = list(row['release_date'].split('-'))
            a_df.loc[index,'release_year'] = '20'+ date_year[2]
    # Convert release_year to numeric value
    a_df['release_year'] = pd.to_numeric(a_df['release_year'])
    # Drop titles released before 2000. If string was 11-Oct-1999 the year got stored as 2099 so these are dropped being greater than 2022
    a_df = a_df.loc[a_df['release_year'] > 1999]
    a_df = a_df.loc[a_df['release_year'] < 2022]
    # Group anime df by year, count, and reset index to create flat DF
    a_group_df = a_df.groupby('release_year').count()
    a_group_df = a_group_df.reset_index()
    # Group by UID and change UID to count_animes for the yearly count
    a_group_df = a_group_df[['release_year','uid']]
    a_group_df.columns = ['release_year','count_animes']
    # Merge to yearly count DFs into one and export to csv for use on site
    merged_year_counts = l_count.merge(a_group_df,how='inner',on='release_year')
    merged_year_counts.to_csv('Updated Website/chart_data/mock_timeseries.csv',index=False)

def sentenceEmbedding(anime_df,la_df):
    # Uncomment for testing
    # anime_df = anime_df.head(50)
    # la_df = la_df.head(50)
    # anime_df = anime_df.reset_index()
    # la_df = la_df.reset_index()

    # Define model from sentence_transformers
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Make a list of anime descriptions from df
    anime_desc = anime_df['description_without_stopwords'].tolist()

    # Make a list of netflix, hulu, amazon prime, disney+ descriptions
    la_desc = la_df['description_without_stopwords'].tolist()

    # Encode anime descriptions 
    anime_embedding = model.encode(anime_desc) # Encoding the anime list

    # Encode live action descriptions 
    la_embedding = model.encode(la_desc) # Encoding the netflix list

    # Compute cosine similarities
    cos_sim = util.cos_sim(la_embedding, anime_embedding)
    #cos_sim

    la_df = la_df.reset_index()
    anime_df = anime_df.reset_index()

    # Build reccomendations column in la_df from cos_sim tensor
    recs = []
    # for each row in the cos_sim tensor
    for i in range(len(cos_sim)):
        mydict={}
        
        # for each col in the row
        for x in range(len(cos_sim[i])):
            #assign title to the column from anime_df["title"][col#]
            try:
                mydict[float(cos_sim[i][x]*-100)] = anime_df["title"][x] + ' (' + (str(round(float(cos_sim[i][x]*100))) +'% Match)')
            except KeyError:
                continue  
        # find the max value in all the columns
        #top2 = sorted(mydict,keys=mydict.get,reverse=True)[:5]
        s = SortedDict(mydict)
        la_df.loc[i,'rec1'] = s.values()[0]
        la_df.loc[i,'rec2'] = s.values()[1]
        la_df.loc[i,'rec3'] = s.values()[2]
        la_df.loc[i,'rec4'] = s.values()[3]
        la_df.loc[i,'rec5'] = s.values()[4]
        #recs.append(top2)

    la_df.head()

    # Export new csv and json
    la_df.to_csv('Final Resources/live_actions_with_anime_recs.csv')
    la_df = la_df[['title','rec1','rec2','rec3','rec4','rec5']]
    la_df.to_json('Updated Website/final_live_actions_with_anime_recs.json', orient='records')