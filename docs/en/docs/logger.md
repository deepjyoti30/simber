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