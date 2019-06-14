import logging
import time
from logging.handlers import TimedRotatingFileHandler



mylogger = logging.getLogger("[YANG]")
mylogger.setLevel(logging.INFO)

# myhandler = TimedRotatingFileHandler(path, when="s", interval=3, backupCount=5)
myhandler = TimedRotatingFileHandler("test_logging_time2.log", when="s", interval=10, backupCount=99)
formatter = logging.Formatter('%(name)s [ %(levelname)s ] %(lineno)d - %(asctime)s - %(message)s')
myhandler.setFormatter(formatter)
mylogger.addHandler(myhandler)
stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
mylogger.addHandler(stream_hander)

for i in range(5):
    mylogger.info("This is a test1  {0} and {1}".format("AAA", "aaa"))
    time.sleep(2)
    mylogger.error("This is a test2  {0} and {1}".format("BBB", "bbb"))
    time.sleep(3)

