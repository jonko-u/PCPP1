"""
Your first handler

Each logger can save logs in different locations as well as in different formats. To do this, you must define your own handler and formatter.

In most cases, you'll want to save your logs to a file. The logging module has the FileHandler class, which facilitates this task. When creating a FileHandler object, you must pass a filename where the logs will be saved.

Additionally, you can pass a file mode with the mode argument, e.g., mode='a'. In the next step, you should set the logging level that will be processed by the handler. By default, the newly created handler is set to the NOTSET level. You can change this using the setLevel method. In the example in the editor, we've set the CRITICAL level.

Finally, you need to add the created handler to your logger using the addHandler method.

Result in the prod.log file:

Your CRITICAL message

If you check the prod.log file, you'll see that only the message is saved there. Do you know what we forgot? Your handler hasn't created a formatter. You'll learn how to do this in a moment.

NOTE: Each logger can have several handlers added. One handler can save logs to a file, while another can send them to an external service. In order to process messages with a level lower than WARNING by added handlers, it's necessary to set this level threshold in the root logger.
"""
import logging

logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')