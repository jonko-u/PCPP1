"""
The Logger object

One application may have several loggers created both by us and by programmers of the modules. If your application is simple, as in the example below, you can use the root logger. To do this, call the getLogger function without providing a name. The root logger is at the highest point in the hierarchy. Its place in the hierarchy is assigned based on the names passed to the getLogger function.

Logger names are similar to the names of the Python modules in which the dot separator is used. Their format is as follows:

hello – creates a logger which is a child of the root logger;

hello.world – creates a logger which is a child of the hello logger.

If you want to make another nesting, just use the dot separator.

The getLogger function returns a Logger object. Let's look at the example code in the editor. We'll find there the ways to get the Logger object, both with and without a name.

We recommend calling the getLogger function with the __name__ argument, which is replaced by the current module name. This allows you to easily specify the source of the logged message.

NOTE: Several calls to the getLogger function with the same name will always return the same object.
"""
import logging

logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)