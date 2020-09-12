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
