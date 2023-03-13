from ui_main import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets ,QtWebEngineWidgets
import os
import sys
# Get the directory containing the current script (i.e. script.py)
this_dir = os.path.dirname(__file__)

# Add the parent directory to the path
parent_dir = os.path.abspath(os.path.join(this_dir, os.pardir))
sys.path.append(parent_dir)

# Now add the utils directory to the path
utils_dir = os.path.abspath(os.path.join(parent_dir, 'TwitterKeeper'))
sys.path.append(utils_dir)

from Twitter_Analyzer import main
from Twitter_keeper import PullTweetsData


class Connect_to_Function(Ui_MainWindow):

    def on_pull_tweets_button_clicked(self):
        # Get the values from the Keyword_Pull_Field and Keyword_Pull_Field2
        query = self.Keyword_Pull_Field.text()
        amount = self.Keyword_Pull_Field_2.text()

        # Call the pullTweets method with the values from Keyword_Pull_Field and Keyword_Pull_Field2 as arguments
        self.twitter_analyzer.pull_tweets.pullTweets(query,amount)
        self.progressBar.setVisible(True)
        self.progressBar.setProperty("value", 0)

    def on_search_clicked(self):

        hashtag = str(self.Hashtag_Search.text())
        author = str(self.Author_Search.text())
        location = str(self.Location_Search.text())
        text = str(self.Text_Search.text())
        stime = str(self.StartTime_Search.text())
        etime = str(self.EndTime_Search.text())
        
        print(isinstance(text,str))
        results = self.twitter_analyzer.load_sample_tweets(author,"", hashtag, location, text, stime, etime)
        print(results)
        self.listWidget_2.clear()
        for result in results:
            item = QtWidgets.QListWidgetItem()
            item.setText(f"====================\n{ result['tweet_author']}\n {self.twitter_analyzer.pull_tweets.utc_to_local(result['tweet_create_at'])}\n ---------------------\n\n {result['text']}\n ====================")
            self.listWidget_2.addItem(item)

    def on_analyze_clicked(self):
        hashtag = str(self.Hashtag_Search_2.text())
        author = str(self.Author_Search_2.text())
        location = str(self.Location_Search_2.text())
        text = str(self.Text_Search_2.text())
        stime = str(self.StartTime_Search_2.text())
        etime = str(self.EndTime_Search_2.text())

        results = self.twitter_analyzer.load_sample_tweets(author,"", hashtag, location, text, stime, etime)
        dfSentiment = self.twitter_analyzer.tweets_sentiment_analyzer(results)
        figPie = self.twitter_analyzer.SentimentPiePlot(dfSentiment)

        dfMostWord = self.twitter_analyzer.find_top_word.MostWordFinder(results)
        self.twitter_analyzer.find_top_word.WordCloudPlot(dfMostWord)
        # image = self.twitter_analyzer.find_top_word.WordCloudPlot(dfMostWord)
        figSpatial = self.twitter_analyzer.spatialPloting(results)

        plot_widget = QtWebEngineWidgets.QWebEngineView(self.Sentiment)
        plot_widget.setHtml(figPie.to_html(include_plotlyjs='cdn'))
        plot_widget.setGeometry(0, 0, self.Sentiment.width(), self.Sentiment.height())

        # pixmap = QtGui.QPixmap()
        # pixmap.fromImage(image)
        
        # pixmap = QtGui.QPixmap('wordcloud.png')
        # self.wordcloud_label.setPixmap(pixmap)
        # Create a QLabel to display the generated image
        # label = QtWidgets.QLabel(self.WordCloud)
        # label.setPixmap(pixmap)
        # label.setGeometry(0, 0, self.WordCloud.width(), self.WordCloud.height())
        # self.WordCloud.setStyleSheet(f"background-image: url({pixmap});")
        plot_widget2 = QtWebEngineWidgets.QWebEngineView(self.WordCloud)
        # plot_widget2.setHtml(f"<html><body><img src=\"wordcloud.png\" /></body></html>")
        plot_widget2.setGeometry(0, 0, self.WordCloud.width(), self.WordCloud.height())

        plot_widget2.load(QtCore.QUrl.fromLocalFile(f"{this_dir}/wordcloud.png"))

        plot_widget3 = QtWebEngineWidgets.QWebEngineView(self.frame_6)
        plot_widget3.setHtml(figSpatial.to_html(include_plotlyjs='cdn'))
        plot_widget3.setZoomFactor(0.75)
        plot_widget3.setGeometry(0, 0, self.frame_6.width(), self.frame_6.height())

        # self.WordCloudCanvas.figure = figWordCloud
        # self.WordCloudCanvas.draw()

        plot_widget2.show()
        plot_widget.show()
        plot_widget3.show()
        
    # def update_wordcloud_frame(self, df):
    #     # Call the WordCloudPlot function to get the image
    #     image = self.twitter_analyzer.find_top_word.WordCloudPlot(dfMostWord)
        
    #     # Create a QPixmap from the image bytes
    #     pixmap = QtGui.QPixmap()
    #     pixmap.loadFromData(image)
        
    #     # Set the pixmap as the background of the WordCloud frame
    #     self.WordCloud.setStyleSheet(f"background-image: url({pixmap.toImage()});")
    def on_trends_clicked(self):
        trends = self.twitter_analyzer.topTrends()
        self.listWidget.clear()
        print(trends)
        font = QtGui.QFont()
        font.setPointSize(14)
        
        for result in trends:
            item = QtWidgets.QListWidgetItem()
            tweet_volumn = result['tweet_volume']
            if (tweet_volumn>=1000):
                tweet_volumn = round(tweet_volumn/1000, 1)
                tweet_volumn_text = f"{tweet_volumn}K"
            else:
                tweet_volumn_text = str(tweet_volumn)
            item.setText(f"{result['name']}\n {tweet_volumn_text} tweets")
            item.setFont(font)
            self.listWidget.addItem(item)

        # Connect the item selection signal to a new function
        self.listWidget.itemSelectionChanged.connect(self.on_list_item_selected)

    def on_list_item_selected(self):
        # Get the selected items from the listWidget
        selected_items = self.listWidget.selectedItems()

        # Get the text of the selected items and pass it to another function
        selected_texts = selected_items[0].text().split("\n")[0]
        print(selected_texts)

    def on_analyze_selected_clicked(self):
        hashtag = self.listWidget.selectedItems()
        hashtag = hashtag[0].text().split("\n")[0]
        self.progressBar_2.setVisible(True)
        self.progressBar_2.setProperty("value", 0)
        # create a new thread for the pullTweets method
        # thread = QtCore.QThread()
        # thread.started.connect(lambda: self.twitter_analyzer.pull_tweets.pullTweets(hashtag,10000))
        # thread.finished.connect(lambda: self.analyze_tweets(hashtag))
        # thread.start()
        # self.twitter_analyzer.pull_tweets.pullTweets(hashtag,10000)
        # Wait until tweets have been pulled
        self.twitter_analyzer.pull_tweets.pullTweets(hashtag, 10000)

        # Wait until tweets have been pulled
        while self.progress < 100:
            QtWidgets.QApplication.processEvents()

        self.analyze_tweets(hashtag)

    def analyze_tweets(self, hashtag):
        # load the sample tweets and perform sentiment analysis
        results = self.twitter_analyzer.load_sample_tweets(hashtag=hashtag)
        dfSentiment = self.twitter_analyzer.tweets_sentiment_analyzer(results)
        figPie = self.twitter_analyzer.SentimentPiePlot(dfSentiment)

        # find the top words and create a word cloud
        dfMostWord = self.twitter_analyzer.find_top_word.MostWordFinder(results)
        self.twitter_analyzer.find_top_word.WordCloudPlot(dfMostWord)
        plot_widget2 = QtWebEngineWidgets.QWebEngineView(self.WordCloud)
        plot_widget2.setGeometry(0, 0, self.WordCloud.width(), self.WordCloud.height())
        plot_widget2.load(QtCore.QUrl.fromLocalFile(f"{this_dir}/wordcloud.png"))

        # create a spatial plot of the tweets
        figSpatial = self.twitter_analyzer.spatialPloting(results)
        plot_widget3 = QtWebEngineWidgets.QWebEngineView(self.frame_6)
        plot_widget3.setHtml(figSpatial.to_html(include_plotlyjs='cdn'))
        plot_widget3.setZoomFactor(0.75)
        plot_widget3.setGeometry(0, 0, self.frame_6.width(), self.frame_6.height())

        # display the sentiment pie chart
        plot_widget = QtWebEngineWidgets.QWebEngineView(self.Sentiment)
        plot_widget.setHtml(figPie.to_html(include_plotlyjs='cdn'))
        plot_widget.setGeometry(0, 0, self.Sentiment.width(), self.Sentiment.height())
        
        # show the plots
        plot_widget2.show()
        plot_widget.show()
        plot_widget3.show()
        
    def update_progress_bar(self, progress):
        self.progressBar.setValue(progress)
        self.progressBar_2.setValue(progress)
        if progress == 100:
            self.progressBar.setVisible(False)
            self.progressBar_2.setVisible(False)
    
    def get_progress(self,progress):
        self.progress = progress

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Connect_to_Function()
    ui.setupUi(MainWindow)
    ui.twitter_analyzer = main()
    ui.progress = 0
    ui.PullTweet_Field.clicked.connect(ui.on_pull_tweets_button_clicked) # connected to pullTweets
    ui.twitter_analyzer.pull_tweets.update_progress_bar.connect(ui.update_progress_bar) # connected to progress of pullTweets
    ui.twitter_analyzer.pull_tweets.update_progress_bar.connect(ui.get_progress)
    ui.Search.clicked.connect(ui.on_search_clicked)
    ui.Search_Trend.clicked.connect(ui.on_analyze_clicked)
    ui.PullTweet_Field_3.clicked.connect(ui.on_trends_clicked)
    ui.Analyze_Selected_List.clicked.connect(ui.on_analyze_selected_clicked)
    # PAGE 1
    ui.Home_Page.clicked.connect(
        lambda: ui.stackedWidget.setCurrentWidget(ui.page_1))

    # PAGE 2
    ui.Search_Page.clicked.connect(
        lambda: ui.stackedWidget.setCurrentWidget(ui.page_2))

    # PAGE 3
    ui.Analyze_Page.clicked.connect(
        lambda: ui.stackedWidget.setCurrentWidget(ui.page_3))
    MainWindow.show()
    sys.exit(app.exec())