from time import time
from tenacity import retry, wait_exponential

t = time()


@retry(wait=wait_exponential(multiplier=1, min=0, max=50))
def wait_exponential_sample():
    c = time()
    print(int(c-t))
    print('retry')
    raise Exception


wait_exponential_sample()
