from tenacity import retry, TryAgain


@retry
def retry_if_exception_sample(num):
    if num > 10:
        print('retry')
        raise TryAgain
    else:
        return 'Success'


retry_if_exception_sample(11)
