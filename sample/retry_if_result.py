from tenacity import retry, retry_if_result


def check_result(result):
    return result == 'Failed'


@retry(retry=retry_if_result(check_result))
def retry_if_result_sample(num):
    print('retry')
    if num < 10:
        return 'Failed'
    return 'Success'


print(retry_if_result_sample(5))
