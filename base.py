import random
from tenacity import retry


@retry
def retry_test():
    if random.randint(0, 10) > 1:
        print('retry')
        raise Exception
    else:
        return "Success!"


print(retry_test())
