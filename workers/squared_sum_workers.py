import threading


class SquaredSumWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        super(SquaredSumWorker, self).__init__(**kwargs)
        # you can set Dameon to true liked this
        # self.dameon = True
        # The dameon parameter needs to be set, before you start the thread.
        self.start()

    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2
        print(sum_squares)

    def run(self):
        self._calculate_sum_squares()
