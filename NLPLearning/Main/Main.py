import threading
from Tweepy import PullTweetsData
import time


class main_threading:

    def setUp(self):

        self.__api_key = "b1AP2ULpybPSA4QJxwNcIkciB"
        self.__api_key_secret = "vUXGZ9ZJ8a0R4YphK9ZHAfwZduAs5v3iCnsxkOuXcZ9edJTqUM"
        self.__access_token = "1552621958780530688-rF7v3RU347dHhd00lKnGRExRI1vLB3"
        self.__access_token_secret = "2YTPWAIixuKT2LvaizWI8CstmF6ABdZOXYbMDo0DIvVcR"

        self.puller = PullTweetsData()
        self.puller.getAccessToAPI(self.__api_key, self.__api_key_secret)
        self.puller.setUserAuthentication(
            self.__access_token, self.__access_token_secret)
        self.puller.getTwitterAPI()
        self.puller.connectToDB("twitter", "tweets")

    def saveTwitter(self, q, amount):
        self.puller.pullTweets(q, amount)

    def __init__(self):
        self.setUp()
        t = threading.Thread(target=self.saveTwitter,
                             args=("#dek66", 15000, ))
        t.start()
        # self.paintwall()


main_threading()
