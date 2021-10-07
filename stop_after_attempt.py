from tenacity import retry, stop_after_attempt


@retry(stop=stop_after_attempt(3))
def stop_after_attempt():
    print('retry')
    raise Exception('retry error')


stop_after_attempt()

"""
retry
retry
retry
Exception: retry error
"""
