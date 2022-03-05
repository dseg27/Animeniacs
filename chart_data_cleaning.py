import pandas as pd
from langdetect import detect
from sortedcontainers import SortedDict
from sentence_transformers import SentenceTransformer, util

def splitLiveActionDF(f_df):
    n_df = f_df.loc[f_df['source'] == 'Netflix']
    am_df = f_df.loc[f_df['source'] == 'Amazon']
    d_df = f_df.loc[f_df['source'] == 'Disney']
    h_df = f_df.loc[f_df['source'] == 'Hulu']

    return n_df,am_df,d_df,h_df

def genreList(genre_string):
        genre_string = genre_string.replace('[','')
        genre_string = genre_string.replace(']','')
        genre_string = genre_string.replace("'",'')
        genre_list = list(genre_string.split(', '))

        return genre_list

def formatGenreCount(df,source):
    genre_df_top = df[['Comedy','Action','Fantasy','Adventure','Drama']]
    genre_df_top = genre_df_top.count()
    genre_count_df = pd.DataFrame({'Genre': genre_df_top.index, source: genre_df_top.values})
    return genre_count_df

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

def reformatDisneyGenre(genre_df):
    for index, row in genre_df.iterrows():
        if row['Action & Adventure'] == '1':
            genre_df.loc[index,'Action'] = '1'
            genre_df.loc[index,'Adventure'] = '1'

    return genre_df 

def genreAnimeCount(df,id,genreCol):

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
    return genre_df

def genreLiveCount(df,id,genreCol):

    source = list(df.iat[0,0])
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
        genre_df = reformatDisneyGenre(genre_df)
    elif source[0] == 'n':
        genre_df = reformatNetflixGenre(genre_df)            
    return genre_df

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

def masterGenreTest(f_df):
    n_df,am_df,d_df,h_df = splitLiveActionDF(f_df)

    am_genre_df = genreLiveCountTest(am_df,'show_id','listed_in')
    d_genre_df = genreLiveCountTest(d_df,'show_id','listed_in')
    h_genre_df = genreLiveCountTest(h_df,'show_id','listed_in')

    am_genre_df.to_csv('coles_practice/csv/amazon_genres.csv', index=False)
    h_genre_df.to_csv('coles_practice/csv/disney_genres.csv', index=False)
    d_genre_df.to_csv('coles_practice/csv/hulu_genres.csv', index=False)

def masterGenre(a_df,f_df):
    n_df,am_df,d_df,h_df = splitLiveActionDF(f_df)

    n_genre_df = genreLiveCount(n_df,'show_id','listed_in')
    am_genre_df = genreAnimeCount(am_df,'show_id','listed_in')
    d_genre_df = genreLiveCount(d_df,'show_id','listed_in')
    h_genre_df = genreLiveCount(h_df,'show_id','listed_in')

    n_genre_counts = formatGenreCount(n_genre_df,'netflix')
    am_genre_counts = formatGenreCount(am_genre_df,'amazon')
    d_genre_counts = formatGenreCount(d_genre_df,'disney')
    h_genre_counts = formatGenreCount(h_genre_df,'hulu')

    a_genre_df = genreAnimeCount(a_df,'uid','genre')
    anime_genre_counts = formatGenreCount(a_genre_df,'Anime')

    merged_genre_counts = anime_genre_counts.merge(n_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.merge(am_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.merge(d_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.merge(h_genre_counts,how='inner',on='Genre')
    merged_genre_counts = merged_genre_counts.rename(columns={'Anime':'anime','Genre':'source'})
    merged_genre_counts = merged_genre_counts[['source','netflix','hulu','amazon','disney','anime']]

    merged_genre_counts.to_csv('Updated Website/chart_data/top5genres_stack.csv',index=False)

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

def movieVSshow(a_df,l_df):
    l_df['count'] = '1'

    for index, row in a_df.iterrows():
        a_df.loc[index,'source'] = 'Anime'
        if row['episodes'] == 1.0:
            a_df.loc[index,'type'] = 'Movie'
        else:
            a_df.loc[index,'type'] = 'TV Show'
        a_df.loc[index,'count'] = '1'
    
    a_df_short = a_df[['source','type','count']]
    l_df_short = l_df[['source','type','count']]

    frames = [a_df_short,l_df_short]
    c_df = pd.concat(frames)

    c_df_group = c_df.groupby(['source','type']).agg({'count': ['count']})
    c_df_group.columns = ['count']
    c_df_group = c_df_group.reset_index()

    c_df_pivot = c_df_group.pivot(index='source',columns='type')
    c_df_pivot = c_df_pivot.reset_index()
    c_df_pivot.columns = ['source','count_movie','count_show']
    c_df_pivot.to_csv('Updated Website/chart_data/movie_vs_show_count.csv', index=False)

def scatterCSV(a_df):
    a_df = a_df.loc[a_df['ranked'] < 51]
    a_df = a_df[['title','episodes','score']]
    a_df.to_csv('Updated Website/chart_data/chart_anime.csv', index=False)

def getTimeseries(a_df,l_df):
    l_df = l_df.loc[l_df['release_year'] > 1999]
    l_count = l_df.groupby('release_year').count()
    l_count = l_count.reset_index()
    l_count = l_count[['release_year','show_id']]
    l_count.columns = ['release_year','count_live_actions']

    a_df = a_df.loc[a_df['aired'] != 'Not available']

    for index,row in a_df.iterrows():
        date_list = list(row['aired'].split(' to '))
        a_df.loc[index,'release_date'] = date_list[0]

    for index, row in a_df.iterrows():
        a_df.loc[index,'date_is_str'] = row['release_date'][0]
        a_df.loc[index,'is_date_str'] = row['release_date'][0].isnumeric()

        if row['release_date'][0].isnumeric() == False:
            date_year = list(row['release_date'].split(', '))
            a_df.loc[index,'release_year'] = date_year[1]
        elif row['release_date'][0].isnumeric() == True and len(row['release_date']) == 4:
            a_df.loc[index,'release_year'] = row['release_date']
        else:
            date_year = list(row['release_date'].split('-'))
            a_df.loc[index,'release_year'] = '20'+ date_year[2]

    a_df['release_year'] = pd.to_numeric(a_df['release_year'])
    a_df = a_df.loc[a_df['release_year'] > 1999]
    a_df = a_df.loc[a_df['release_year'] < 2022]
    a_group_df = a_df.groupby('release_year').count()
    a_group_df = a_group_df.reset_index()
    a_group_df = a_group_df[['release_year','uid']]
    a_group_df.columns = ['release_year','count_animes']

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
            #print(mydict)
            # try:
            #     mydict[anime_df["title"][x],(('%' + str(round(float(cos_sim[i][x]*100)))))] = cos_sim[i][x]
            # except KeyError:
            #     continue  
            # print(mydict)    
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

    # Export new csv
    la_df.to_csv('Final Resources/live_actions_with_anime_recs.csv')