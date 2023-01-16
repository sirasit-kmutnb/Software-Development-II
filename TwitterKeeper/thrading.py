from threading import Thread
import time
from tqdm import tqdm


class threader:
    def test(self, number):
        time.sleep(2)
        print(number)

    def test1(self, number):
        time.sleep(5)
        print(number)

    def __init__(self):
        for i in tqdm(range(10)):
            self.test(i)
            self.test1(i)
            # t = Thread(target=self.test, args=(i, ))
            # t.start()
            # t1 = Thread(target=self.test1, args=(i, ))
            # t1.start()


threader()
