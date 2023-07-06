"""
Logging levels

The Logger object allows you to create logs with different levels of logging that help you to distinguish between less important logs and those reporting a serious error. By default, the following logging levels are defined:
Level name 	Value
CRITICAL 	50
ERROR 	40
WARNING 	30
INFO 	20
DEBUG 	10
NOTSET 	0

Each level has a name and a numeric value. You can also define your own level, but those offered by the logging module are quite sufficient. The Logger object has methods that set the logging level for you. Take a look at the example in the editor.

Result:

CRITICAL:root:Your CRITICAL message
ERROR:root:Your ERROR message
WARNING:root:Your WARNING message

All of the above methods require you to provide a message that will be visible in the logs. The default log format includes the level, the logger name and the message you’ve defined. Note that all these values are separated by a colon. Later in this course, you'll learn how to change the default formatting.

You’re probably wondering why messages with INFO and DEBUG levels are not displayed. This is due to the default configuration, which we'll talk about in a moment.

NOTE: The basicConfig method will be discussed later in the course. For now, remember that it's responsible for the basic logging configuration.

"""
import logging

logging.basicConfig()

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')