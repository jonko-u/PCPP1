"""
Basic configuration (part 1)

As we mentioned before, the basic logging configuration is done using the basicConfig method. Calling the basicConfig method (without specifying any arguments) creates a StreamHandler object that processes the logs and then displays them in the console.

The StreamHandler object is created by the default Formatter object responsible for the log format. As a reminder, the default format consists of the level name, logger name, and defined message. Finally the newly created handler is added to the root logger. Later you'll learn how to create your own handler and formatter.

In the previous examples, we called the basicConfig method without any arguments. Using the basicConfig, method you can change the logging level (in the same way as using the setLevel method) and even the location of the logs. Take a look at the example in the editor.

Result in prod.log file:

CRITICAL:root:Your CRITICAL message

In the example, the basicConfig method takes three arguments. The first one is the logging level equal to CRITICAL, which means that only messages with this level will be processed.

Passing a filename to the second argument creates a FileHandler object (instead of a StreamHandler object). As you’ve probably noticed, the logs no longer appear in the console. After setting the filename argument, all logs will be directed to the specified file.

In addition, passing the last filemode argument with the value 'a' (this is the default mode) means that new logs will be appended to this file. If you'd like to change this mode, you can use other modes that are analogous to those used in the built-in open function.

These aren't all the arguments that the basicConfig method can take. Are you ready for another dose of knowledge? Let's move on!

NOTE: ThebasicConfig method changes the configuration of the root logger and its children who don't have their own handler defined.
"""
import logging

# Part1
# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')
#
# logger = logging.getLogger()
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')
# Part2
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')