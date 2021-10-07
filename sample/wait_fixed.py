from tenacity import retry, wait_fixed


@retry(wait=wait_fixed(2))
def wait_fixed_sample():
    print('retry')
    raise Exception


wait_fixed_sample()
