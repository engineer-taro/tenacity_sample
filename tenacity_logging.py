from tenacity import retry, wait_fixed, before_log, after_log
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


@retry(wait=wait_fixed(2),
       before=before_log(logger, logging.DEBUG),
       after=after_log(logger, logging.DEBUG))
def wait_fixed_sample():
    print('retry')
    raise Exception


wait_fixed_sample()
