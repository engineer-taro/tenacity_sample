from tenacity import retry, stop_after_delay


@retry(stop=stop_after_delay(10))
def stop_after_delay_test():
    print('retry')
    raise Exception


stop_after_delay_test()

"""
retry
retry
~~~~~
10秒後に止まる
"""
