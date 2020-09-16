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

Alternately, the logger will also initialize a file stream and add it to the stream set if the [log_path](http://localhost:8000/logger/#logger-class) param is passed and valid.

>NOTE: The file stream will be initialized even if `disable_file` is passed as True but it will be disabled while init. It can be enabled back by using the logger update methods.

## Adding custom streams

## Disabling writing to files