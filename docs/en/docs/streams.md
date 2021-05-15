# Streams

## What is it

Anything where **Simber** writes to is considered a stream. Simber allows users to add multiple streams to the logger. By default one stream is used when the logger is initiated. This is the `<stdout>` stream, that is, it will write to your console.

Streams are basically a set of `OutputStream` classes that are shared by all the instances running. This means, if a package is creating a `Logger` instance in various modules, it will still share the same streams as all the others.

This functionality gives full access to the user, as to where the logs should be written.

## Properties

A `Stream` is defined by an `OutputStream` class. This class takes a few arguments while initializing.

### Params

Following are the paramaters of the `OutputStream` class

| Name | Description | Default Value |
| ---- | ----------- | ------------- |
| `stream` | The stream itself. Should be of type `TextIOWrapper`. | No default value, required param |
| `level` | The minimum level that the stream will log in | INFO |
| `format` | The format of the output string | Default file format is considered |
| `disabled` | If the stream is disabled from writing. If this is `True`, it will not write anything, until it is changed to `False` | `False` |
| `time_format` | Time format to be passed to the formatter for the `time` value. | `%d/%m/%Y %H:%M:%S` |

### Attributes

Following are the attributes of the `OutputStream` class

- **level**: The minimum level that the stream will log in. Can be **get** and **set** by the `level` attribute.
- **format**: The format that the stream will output in. Can be **get** and **set** by the `format` attribute.
- **disabled**: If the stream is disabled or not. Can be **get** and **set** by the `disabled` attribute.
- **stream_name**: Name of the stream as returned by the `TextIOWrapper` stream. This is a readonly attribute.

### Methods

The `OutputStream` class has only one public method, i:e `write()`. This method allows the user to write to the stream. This need not be called manually, it will be handled by the logger.

Source of the `write()` method can be checked in the [stream](https://github.com/deepjyoti30/simber/blob/master/simber/stream.py) module.

## Default Stream

Simber adds a default stream to the stream set when a new instance is initialized.

>NOTE: Since the streams are shared among all the instances, so only unique streams are contained in the stream set. This means, even if the `Logger` class is initialized multiple times, it will have just one `stdout` stream.

This default stream is `stdout` and is of type `TextIOWrapper`.

This is extracted using the `sys` module.

Additionally, the logger will also initialize a file stream and add it to the stream set if the [log_path](http://localhost:8000/logger/#logger-class) param is passed and valid.

>NOTE: The file stream will be initialized even if `disable_file` is passed as True but it will be disabled while init. It can be enabled back by using the logger update methods.

## Adding custom streams

**Simber** allows you to add as many unique streams as you want and with call to any of the instances running, all the streams will write if they are not explicitly disabled.

In order to add a stream to the logger instance, the [add_stream](http://localhost:8000/logger/#utility-methods) method can be used.

This method takes an `OutputStream` object. If any other type is passed, it will raise an `InvalidOutputStream` exception.

The following code creates a new stream that writes to the file `nana.log` in the current directory.

```python
# Open the file stream
file_stream = open("nana.log", "a")  # Open in append mode

from simber.stream import OutputStream

# Create an Output Stream instance
stream = OutputStream(file_stream)
```

Once the `OutputStream` instance is ready, we can add it to the list of streams.

```python
from simber import Logger

# Create a logger instance
logger = Logger("main")

# Add the stream to the logger instance
logger.add_stream(stream)

logger.info("Just a test info log")  # This will log to console and `nana.log`
```

Now you can check the file `nana.log` and see that the test log was appended to it.

>NOTE: While creating custom file streams, make sure that the file exists before writing, else you won't
be able to open it with `open()`.

## Disabling writing to files

### Disable all file streams using Logger

**Simber** allows the user to disable writing to all the file streams present in the set of streams. The file streams are filtered out by using the `stream_name` attribute of the `TextIOWrapper` class.

Writing to files can be disabled in the following way throught the logger.

```python
from simber import Logger

logger = Logger("main")

# Disable writing to files
logger.update_disable_file(True)

logger.info("Test message that will log to only non file streams")
```

Above is usefule in case the app is being debugged and you don't want to fill up your log files with the same content over and over again.

### Disable while creating the OutputStream

The stream can also be disable while creating it.

As mentioned above, the `OutputStream` class accepts a `disabled` parameter.

So the stream can be disabled while the instance is created

```python
from simber.stream import OutputStream
from simber import Logger

stream = OutputStream(open("nana.log", "a"), disabled=True)

# Add the stream to logger and try to write
logger = Logger("main")
logger.add_stream(stream)

logger.info("Test log")  # Will not be written to the `nana.log` file
```

It can also be enabled/disabled further by directly updating the attribute

```python
print("Stream disabled: {}".format(stream.disabled))

# Enable the stream
stream.disabled = False
```
