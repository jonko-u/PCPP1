"""
The setLevel method

The root logger has the logging level set to WARNING. This means that messages at the INFO or DEBUG levels aren't processed.

Sometimes you may want to change this behavior, especially if you create your own logger. To do this, you need to pass a logging level to the setLevel method. See how we do this in the editor.

Result:

CRITICAL:root:Your CRITICAL message
ERROR:root:Your ERROR message
WARNING:root:Your WARNING message
INFO:root:Your INFO message
DEBUG:root:Your DEBUG message

Setting the DEBUG level causes messages with this or a higher level to be logged. It's worth mentioning that loggers created using the name argument have the NOTSET level set by default. In this case, their logging level is set based on the parent levels, starting from the closest parent to the root logger.

If the closest parent has a level set to NOTSET, the logger level is set based on the levels of subsequent parents in the hierarchy. Level setting ends if a parent has a level other than NOTSET. If none of the visited parents has a level other than NOTSET, then all messages will be processed regardless of their level.

"""
import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')