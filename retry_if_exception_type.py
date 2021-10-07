from tenacity import retry, retry_if_exception_type


@retry(retry=retry_if_exception_type((TypeError, IndexError)))
def retry_if_exception_sample():
    print('retry')
    raise KeyError


retry_if_exception_sample()
