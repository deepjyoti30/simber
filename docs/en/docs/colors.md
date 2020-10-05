
# Colors

**Simber** allows highlighting the output with colors.

## Usage

Using colors in the output format is pretty simple. All you need to do is use some special characters in order to let **Simber** know that that part needs to be formatted with a certain color.

For instance, if we want a format that uses the green color in the levelname, we pass the format string as follows

```python
from simber import Logger

custom_format = "%g{levelname}%"

# Create the logger and pass the custom format
logger = Logger("test", format=custom_format)

logger.info("Colorful log message")
```

Above will print the following output

<img src="/assets/logger_color.jpg">

## Format

The user has to **wrap** the string in `%` and make the **first character** of the string the color that the string will use.

The `ColorFormatter` extracts all the strings that follow the following format

```%<color>somestring%```

In the above string the `%` mark the start and end of the special colored string and the `<color>` will be a single character that will specify which color to be used for the message inside the string.

For example, if a string is passed as **`%ggreen colored string`** it will return a string that will be colored `green` with the message **`green colored string`**

## Color names

The single character map of the colors to the proper color is listed in the following table

| Color | character |
| ----- | --------- |
| Green | g         |
| Red   | r         |
| Yellow | y        |
| Blue | b          |
| Magenta | m       |
| Cyan | c |
| White | w |
| Black | n |

>NOTE: Black uses the character `n` because `b` is already used by `Blue`

Based on the above table, if we want a string to have red color we will do something like this

```%rThis string has red text%```

## Automatic color filling

**Simber** also allows the user to pass a special character that makes the color formatter fill the color based on the level that message needs to be logged in.

This can be established by passing the character **`a`** in place of the color name.

```python
# This will make the levelname color according to the log level
format = "%a{levelname}%"
```

The color is determined as following, based on the level that the message is being logged in.

| Level | Color used |
| ----- | ---------- |
| Debug | Blue |
| Info | Green |
| Warning | Yellow |
| Error | Red |
| Critical | Red |

## Examples

Let's say we want to make the logger automatically detect the color for the level but for the time, we 
want to keep the color red for all the prints.
That can be done in the following way.

```python
from simber import Logger

custom_format = "%a[{levelname}]% %r[{time}]%"
logger = Logger("test", format=custom_format)

logger.info("Just a test message")
logger.warning("A warning test message")
```

This will show the following output

<img src="/assets/logger_color_2.jpg">