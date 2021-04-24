# Logger

**Simber**, since it's a logger, exposes a public class named `Logger`.

It can be used right away by creating an instance of this class and using the write methods.

## Levels

**Simber** allows the user to log the messages in 5 different levels. Each level has a number associated to them that let's the Logger determine which level is higher. These are:

| Number associated | Name | Description |
| ----------------- | ---- | ----------- |
| 0 | DEBUG | Level that is used for debugging, messages that are not supposed to be seen by the user. |
| 1 | INFO | Level used to show information to the user. |
| 2 | WARNING | Level used to show warning to the user. |
| 3 | ERROR | Level to show errors to the user. Errors are considered not fatal. Some error has occured but the program can continue working |
| 4 | CRITICAL | Level to show fatal errors to user. When message is printed through this level, the program exits execution just after printing the message. |

## Minimum Level

The logger takes into consideration the minimum level before printing anything. It checks if the level that is being called is higher or equal to the minimum level and only then it prints the message.

For Eg:

If the minimum level is set to `WARNING` which has the number `2` associated with it. This means any levels that have a number less than `2` associated with it will not print the message.

>NOTE: By default, the minimum level is set to `INFO` in **Simber**.

## Using in packages

One of the most powerful features of **Simber** is that it allows the user to handle all the logger instances by just one instance. This can also be seen in the [architecture](/architecture) page.

Let's say you have a large package base and there are a lot of modules where you need to log from. So, the trivial way would be to create an instance in every module and call the log methods accordingly. Now, let's say we want to make all the loggers run at `DEBUG` mode, which means we want to set the minimum level of all the loggers to `DEBUG`.

Usually, you'd have to go to each module and update the instance manually.

However, Simber takes care of that for you. All you have to do is use the `update_level` method of the `last` instance created (since the last instance is mostly created in the main module which is importing all the other ones.).

This method will update the level of all the other logger instances at once!

### How does it work?

**Simber** by default, keeps a list of all the instances initialized from the `Logger` class. This means that if you create two instances of the `Logger` class, both in different files. However, you import one to the other, Simber, will automatically pick it up and will have control over the other instances.

Eg:

Let's say you have a module named `second_module.py` with the following code.

```python
from Simber import Logger

logger = Logger("second")

def hello():
    logger.info("Printing hello from second module")
```

and a module named `first_module.py` with the following code.

```python
from Simber import Logger
from second_module import hello

logger = Logger("first")

# Update the minimum level of both instances
logger.update_all("WARNING")

logger.info("Printing from first module")  # Won't be printed
hello()  # Won't print
logger.warning("Just a warning")  # Will be printed
```

In the above code, the first module imports the second module. Only after the imports are done, the `logger` is init and so it is able to pick up the second module's instance automatically and even update it.

## Logger Class

The `Logger` class in **Simber**, takes a certain number of parameters. Only one of them is required, that is name of the logger. Others are optional.

It is defined as follows:

```python
def __init__(self, name, **kwargs)
```

Following are the params accepted by the `Logger` class:

| param | Description |
| ----- | ----------- |
| name | Name of the current instance of the logger. This should be something that describes the module that the logger is being called from |
| format | The format to be used by the logger for the messages. |
| file_format | The format to be used to write to files. If it is not passed, `format` will be used here. |
| log_path | File or directory where logs are supposed to be stored. If it is a directory, a new log file is created if not already present and accordingly written. If it is a file, the logs are written to this file. If not passed, this is skipped.|
| level | Minimum level that the logger will log in. By default set to `INFO` |
| file_level | Minimum level that the logger will log in for files. Set to minimum level by default |
| disable_file | Disable writing the logs to the files |
| update_all | Update all the instances that are created before this instance with the passed `format`, `level` and value of `disable_file`. |
| time_format | Format for the time to be printed. This should be a string as accepted by the [datetime's strftime](https://docs.python.org/3/library/datetime.html#datetime.date.strftime). |

## Methods

**Simber** exposes a number of methods in order to let the user have maximum control over the logger.

### Log methods

The methods to log are

- `debug(message, *args)`
- `info(message, *args)`
- `warning(message, *args)`
- `error(message, *args)`
- `critical(message, *args, exit_code=-1)`

### Update methods

The methods that can be used to update other instances

- `update_level(level)`               - Update the `level` for all instances
- `update_disable_file(disable_file)` - Update the `disable_file` attribute for all instances
- `update_format(format)`             - Update the `format` for all instances
- `update_format_console(format)`     - Update the console `format` for all the instances

### Utility methods

Other useful methods

- `add_stream(stream_to_be_added)` - Add streams to the stream container. More in the [streams](/streams/) page
- `list_available_levels()`        - List all available levels to stdout
- `hold()`                         - Hold the screen for user input. Useful if the logger needs to be haulted afer showing a certain output.
- `get_log_file()`                 - Get the current log file that is being written to.