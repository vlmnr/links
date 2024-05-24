# преобразование длинного URl в короткий
# модули requests, base

import multiprocessing
import concurrent.futures


from myrequests import *
from base import *
from clean_base import *

if __name__ == "__main__":
"""    web_server_process = multiprocessing.Process(target=start_web_server)
    cleanup_process = multiprocessing.Process(target=cleanning_base) # in myrequests
    web_server_process.start()
    cleanup_process.start()
    web_server_process.join()
    cleanup_process.join() """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(start_web_server)
        executor.submit(database_cleanup_loop)



