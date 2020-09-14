# Formatting

**Simber** allows you to format the output messages as you want.

## How to pass keywords

Simber allows the user to pass the special keywords just like it is passed to any Python string. For instance, if you want the levelname to be dynamically formatted during the runtime, then the string should be following

```python
message_string = "{levelname} Just another message"
```

If the above string is passed as the format for the logger, during the runtime, a call to `INFO` method will print the following.

```console
INFO Just another message
```

## Special Keywords

Simber allows a certain number of special keywords that are formatted just before the message is written.

Supported keywords are:

| Name | Keyword | Description |
| ---- | ------- | ----------- |
| Time | time    | Time as of printing the message. It will be of the form `%d/%m/%Y %H:%M:%S` |
| Filename | filename | Name of the file that is printing this message |
| Function Name | funcname | Name of the function that is printing this message |
| Line Number | lineno | Line number of the current call in the file |
| Level Name | levelname | Level at which the logger is printing this message |
| Level Number | levelno | Level number at which the logger is printing this message |
| Logger Name | logger | Name of the logger that is printing this message |
| Message | message | Message passed by the user |

## Passing custom formats

In **Simber**, formats are specific to [streams](/streams/). So the format for each stream can vary, thus there is a need to pass custom formats. By leveraging the above keywords, pretty useful custom formats can be passed.

One thing to note is that, whatever custom message is passed by the user will be **appended** to this formatted string.

### Default format

By default, Simber uses the following format for printing to `stdout`.

```[{levelname}] [{logger}]```

By using the above format with the `info` method as following

```python
# Considering logger is an instance of Logger with name `Test`
logger.info("Printing a test message to stdout")
```

The output will be

```console
[INFO] [Test] Printing a test message to stdout
```

### Custom Format

We can passing a proper custom format in the following way.

Let's say, we want the following things in our logger message

- Level of the logger
- Name of the logger
- Name of the calling file
- Line number of the calling file

We can create a custom format including all the above in the following way.

```python
from simber import Logger

custom_format = "[{levelname}] [{logger}] [{filename}] [{lineno}]"

# Now create an instance and pass the format
logger = Logger("Test", format=custome_format)

logger.info("Just a test statement")
```

Above will output the following

```console
[INFO] [Test] [test.py] [4] Just a test statement
```

## Advanced

**Simber** formatter module has a `Formatter` class that exposes a static method `sub`.

This method is used by the logger in order to format the code. The code of the method can be found [here](https://github.com/deepjyoti30/simber/blob/89b058de6b9819c9e8110292c830aaaeef0cc074/simber/formatter.py#L48)

If you want to override this method, a class can be made by inheriting the `Formatter` class and defining the `sub` method according to your wish, however, it is important to keep it a static method and preserving the paramaters that it accepts.
