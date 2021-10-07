import time
from tenacity import retry, stop_after_attempt, stop_after_delay


@retry(stop=(stop_after_attempt(3) | stop_after_delay(10)))
def stop_after_attempt_delay_combine(sleep: int):
    time.sleep(sleep)
    print('retry')
    raise Exception('retry error')


stop_after_attempt_delay_combine(1)  # => 1秒ごとにリトライされるので試行回数の制限でリトライが終了する
stop_after_attempt_delay_combine(5)  # => 5秒ごとにリトライされるので時間制限でリトライが終了する
