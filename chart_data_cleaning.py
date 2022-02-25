import pandas as pd
from langdetect import detect

def genreList(genre_string):
        genre_string = genre_string.replace('[','')
        genre_string = genre_string.replace(']','')
        genre_string = genre_string.replace("'",'')
        genre_list = list(genre_string.split(', '))

        return genre_list

def genreCount(anime_df, netflix_df, amazon_df, hulu_df, disney_df):
    genre_df = anime_df[['uid','genre']]
    # genre_df_head = genre_df.head(5)
    unique_list = []

    for index, row in genre_df.iterrows():
        genre_list = genreList(row['genre'])

        for x in genre_list:
            if x not in unique_list:
                unique_list.append(x)
                
        for x in genre_list:
            if x in unique_list:
                genre_df.loc[index,x] = 'T'

    genre_count_series = genre_df.count()
    genre_count_df = pd.DataFrame({'Genre': genre_count_series.index, 'Count': genre_count_series.values})
    genre_count_df = genre_count_df.drop(labels=[0])
    genre_count_df = genre_count_df.drop(labels=[1])
    genre_count_df = genre_count_df[genre_count_df['Genre'] != '']
    genre_count_df = genre_count_df.sort_values('Count',ascending=False)

    genre_count_df.to_csv('data/genre_count_list.csv')

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