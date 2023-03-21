from Twitter_keeper import PullTweetsData
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from dotenv import load_dotenv
import os
import re
import emoji
import numpy as np
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import pandas as pd
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


class FindTopWord(PullTweetsData):

    def tokenize(self, d):
        result = d.split("/")
        result = list(filter(None, result))
        return result

    def prepared_Text(self, text_list):
        new_text = []
        for text in text_list:
            new_text.append(self.preprocessText(text['text']))
        return new_text

    def MostWordFinder(self, tweets_list):
        vectorizer = CountVectorizer(tokenizer=self.tokenize)
        transformed_data = vectorizer.fit_transform(self.prepared_Text(tweets_list))
        keyword_df1 = pd.DataFrame(columns=['word', 'count'])
        keyword_df1['word'] = vectorizer.get_feature_names_out()
        # print(vectorizer.get_feature_names_out())
        keyword_df1['count'] = np.ravel(transformed_data.sum(axis=0))
        newdf = keyword_df1.sort_values(by=['count'], ascending=False).head(10)
        return keyword_df1
    
    def Most10WordFinder(self, tweets_list):
        vectorizer = CountVectorizer(tokenizer=self.tokenize)
        transformed_data = vectorizer.fit_transform(self.prepared_Text(tweets_list))
        keyword_df1 = pd.DataFrame(columns=['word', 'count'])
        keyword_df1['word'] = vectorizer.get_feature_names_out()
        # print(vectorizer.get_feature_names_out())
        keyword_df1['count'] = np.ravel(transformed_data.sum(axis=0))
        newdf = keyword_df1.sort_values(by=['count'], ascending=False).head(10)
        return newdf
    
    def WordCloudPlot(self,df):
        word_dict = {}
        for i in range(0,len(df)):
            word_dict[df.word[i]]= df['count'][i]
        wordcloud = WordCloud(width=1280,height=720,font_path='./SukhumvitSet-Medium.ttf',mode="RGBA",background_color ="rgba(255, 255, 255, 0)",max_words=70).fit_words(word_dict)
        #  # Create a new subplot with Plotly
        # fig = make_subplots(rows=1, cols=1)

        # # Add the wordcloud as an image trace to the plot
        # fig.add_trace(
        #     go.Image(z=wordcloud.to_array()),
        #     row=1, col=1
        # )

        # # Configure the plot layout
        # fig.update_layout(
        #     title='Word Cloud',
        #     width=1280,
        #     height=720,
        #     margin=dict(l=10, r=10, t=80, b=10),
        #     template='plotly_white'
        # )
        # fig.show()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig('../GUI/wordcloud.png', dpi=300, bbox_inches='tight')
        plt.close()
        


class SentimentAnalyze(PullTweetsData):

    def __init__(self):
        self.__df_train = pd.read_csv('general-amy.csv')
        self.__vectorizer = CountVectorizer()
        self.__model = MultinomialNB()

    def preprocess_train_text(self, text):
        text = self.removeLink(text)
        text = self.removeEmoji(text)
        text = self.removeSpecialChar(text)
        final = "".join(u for u in text if u not in (
            "?", ".", ";", ":", "!", '"', "ๆ", "ฯ"))
        final = word_tokenize(final, engine="newmm")
        final = " ".join(word for word in final)
        # final = " ".join(word for word in final.split() if word.lower not in thai_stopwords())
        return final
        # tokens = word_tokenize(text, engine="newmm")
        # result = [word for word in tokens if word not in list(
        #         thai_stopwords()) and " " not in word]
        # return " ".join(result).rstrip()

    def run_prep_train(self):
        self.__df_train['text'] = self.__df_train['text'].apply(
            self.preprocess_train_text)

    def split_training(self):
        self.X = self.__vectorizer.fit_transform(self.__df_train['text'])
        self.y = self.__df_train['sentiment']
        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2)

    def training_model(self):
        self.run_prep_train()
        self.split_training()
        # Train the model
        self.__model.fit(self.X_train, self.y_train)

    def evaluating_model(self):
        # Evaluate the model on the test data
        y_pred = self.__model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        return accuracy

    def sentiment_analyzer(self, text):
        # Use the model to make predictions on new data
        new_text = self.__vectorizer.transform([text])
        new_bag_of_word = self.__vectorizer.transform(
            pd.Series([self.preprocess_train_text(text)]))
        # print(new_bag_of_word)
        new_pred = self.__model.predict(new_bag_of_word)
        return new_pred[0]


class main():
    def __init__(self):
        TH_Bangkok = 1225448
        TH = 23424960
        JP_Tokyo = 1118370
        self.WOEID = TH
        api_key = os.getenv('API_KEY')
        api_key_secret = os.getenv('API_KEY_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        self.database = "twitter_keeper"
        self.collection = "tweets"
        self.find_top_word = FindTopWord()
        self.pull_tweets = PullTweetsData()
        self.pull_tweets.getAccessToAPI(api_key, api_key_secret)
        self.pull_tweets.setUserAuthentication(
            access_token, access_token_secret)
        self.pull_tweets.getTwitterAPI()
        self.pull_tweets.connectToDB("twitter_keeper", "tweets")

    def load_sample_tweets(self, author="", keyword="", hashtag="", location="", text="", fromTime="", toTime=""):
        print(f"You called load_sample_tweets with {author, keyword, hashtag, location, text, fromTime, toTime}")
        results = self.pull_tweets.find_multi(author, keyword, hashtag, location, text, fromTime, toTime)
        # sorted_list = sorted(results, key=lambda x: x['tweet_create_at'],reverse=False)
        # try:
        #     recentTime = self.pull_tweets.utc_to_local(sorted_list[0]['tweet_create_at'])
        # except:
        #     recentTime = "No data, Pulling new tweets."
        # startTime = self.pull_tweets.utc_to_local(self.pull_tweets.local_to_utc(fromTime))
        # try:
        #     isStartTimeNotReached = recentTime > startTime
        # except:
        #     isStartTimeNotReached = False
        # if isStartTimeNotReached:
        #     self.pull_tweets.pullTweets(query=hashtag,amount=20000)

        return results

    def tweets_find_top_word(self, author="", keyword="", hashtag="", location="", text="", fromTime="", toTime=""):
        tweets_list = self.pull_tweets.prepared_Text(self.load_sample_tweets(
            author, keyword, hashtag, location, text, fromTime, toTime))
        return self.find_top_word.MostWordFinder(tweets_list)

    def tweets_sentiment_analyzer(self, tweets_list):
        self.sentiment_analyze = SentimentAnalyze()
        self.sentiment_analyze.training_model()
        acc = self.sentiment_analyze.evaluating_model()
        df = pd.DataFrame({'text': [], 'sentiment': []})
        for tweet in tqdm(tweets_list):
            sentiment = self.sentiment_analyze.sentiment_analyzer(tweet['text'])
            df = pd.concat([df, pd.DataFrame(
                pd.Series([tweet['text'], sentiment], index=df.columns)).T], ignore_index=True)
        return df
    
    def SentimentPiePlot(self,df):
        # Count the number of occurrences of each sentiment
        sentiment_counts = df['sentiment'].value_counts()

        print(sentiment_counts)
        # Calculate the percentage of each sentiment
        sentiment_percentages = sentiment_counts / len(df) * 100
        print(sentiment_percentages)
        # Create the pie chart
        fig = px.pie(sentiment_percentages, values=sentiment_percentages.values, 
                    names=sentiment_percentages.index, title='Sentiment Percentage')
        # fig.show()
        #Show the chart
        return fig

    def topTrends(self):
        trends = self.pull_tweets._PullTweetsData__api.get_place_trends(
            self.WOEID)
        top50 = trends[0]['trends']
        new_list = [d for d in top50 if d.get('tweet_volume') != None]
        sorted_list = sorted(
            new_list, key=lambda x: x['tweet_volume'], reverse=True)
        if len(top50) >= 20:
            top10 = sorted_list[0:20]
            print(len(top10))
        else:
            top10 = sorted_list[0:len(top50)]
        return top10

    def spatialPloting(self, tw_list):
        countries_dict = {
            "country": {}
        }
        c_data = pd.read_csv('country.csv')
        for i in tw_list:
            if i['tweet_location'].lower() in [str(element).lower() for element in c_data['name'].to_list()]:
                try:
                    countries_dict["country"][i['tweet_location'].lower()] += 1
                except:
                    countries_dict["country"][i['tweet_location'].lower()] = 1

        data = pd.DataFrame({
            'country': list(countries_dict['country'].keys()),
            'value': list(countries_dict['country'].values())
        })

        # Define the scattergeo trace
        def clip_value(value):
            if value <= 50:
                return value
            else:
                return 50
        
        data_value = data['value'].apply(clip_value)
        trace = go.Scattergeo(
            locationmode='country names',
            locations=data['country'],
            mode='markers',
            marker={
                'size': data_value,
                'color': "#000000",
                'colorscale': 'Viridis',
                'opacity': 0.7,
                # 'colorbar': {'title': 'Value'},
                'sizemin': 5
            },
            text = data['country'] + ': ' + data['value'].astype(str)
        )

        # Define the layout
        layout = go.Layout(
            title="Spatial Plot",
            geo=dict(
                projection_type='natural earth',
                showland=True,
                landcolor='rgb(243, 243, 243)',
                showcountries=True,
                countrycolor='rgb(204, 204, 204)',
                countrywidth=0.5,
                showocean=True,
                oceancolor='rgb(157, 214, 255)',
                showlakes=True,
                lakecolor='rgb(157, 214, 255)',
                showrivers=True,
                rivercolor='rgb(157, 214, 255)',
                riverwidth=1,
                showcoastlines=True,
                coastlinecolor='rgb(204, 204, 204)',
                coastlinewidth=1,
                showframe=False
            )
        )

        # Create the figure
        fig = go.Figure(data=[trace], layout=layout)
        # Update the layout to display the map in full screen
        fig.update_layout(
            autosize=True,
            margin=dict(l=0, r=0, t=0, b=0),
        )
        
        # Show the figure
        return fig
  

    # def OneAnalyzer(self):
    #     top10 = self.topTrends()
    #     for i in range(len(top10)):
    #         print("Number", i, "=>", top10[i]["name"])
    #     selectNumber = int(
    #         input("Please select Number to pull and analyze : "))
    #     selectOne = top10[selectNumber]
    #     # print(selectOne)
    #     objectSelectName = selectOne["name"]
    #     # print(objectSelectName)
    #     self.pull_tweets.pullTweets(objectSelectName, 100)
    #     df = self.tweets_sentiment_analyzer(keyword=objectSelectName)
    #     print(df)

    # def top10Analyzer(self):
    #     top10 = self.topTrends()
    #     names = [d['name'] for d in top10]
    #     for i in tqdm(names):
    #         self.pull_tweets.pullTweets(i, 10)
    #     resultSenti = pd.DataFrame({'text': [], 'sentiment': []})
    #     for i in tqdm(names):
    #         df = self.tweets_sentiment_analyzer(text="", keyword=i)
    #         # dfTitle(i)
    #         # resultSenti = pd.concat([resultSenti, dfTitle(i)])
    #         resultSenti = pd.concat([resultSenti, df])
    #     print(resultSenti)


if __name__ == "__main__":
    # print(main().topTrends())
    # main().OneAnalyzer()
    # x = main().load_sample_tweets(hashtag="dek66")
    # dfMostWord = main().find_top_word.MostWordFinder(x)
    # print(dfMostWord)
    # main().find_top_word.WordCloudPlot(dfMostWord)
    # df = main().tweets_sentiment_analyzer(x)
    # main().SentimentPiePlot(df)
    # # for i in x:
    # #     print(i['tweet_location'].lower())
    # main().spatialPloting(x).show()
    # print(main().spatialPloting(x))
    pass
