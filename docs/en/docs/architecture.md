# Architecture

In order to get the best out of **Simber**, you should be aware of its architecture. The ideology behind creating Simber was that it needs to be simple enough that anyone can start using it right away
and powerfull enough that pro users can get everything they want from a Logger.

## Simber Architecure

Following image sums up how **Simber** actually works and why it is *powerful*

<div align="center" style="padding-top: 25px; padding-bottom: 25px;">
<img src="/assets/simber_arch.png">
</div>

## Explanation

The above image *literally* sums up a lot but still, I will explain each part of it.

Let's start from the bottom part of the diagram and accordingly move up to the top.

### Logger

The idea behind the logger is that one instance that would be the *main* instance, should be able to control all the other instances.

As seen at the very bottom, there are multiple logger instances. Above that we see that there is one logger instance that was initialized the last and so called the *final* instance.

It clearly shows that the final instance will be able to control all the other instances. This is very advantageous, especially for packages with a big source base. The main module, which will probably be importing all the other modules, will have the *main* Logger instance and this instance will automatically pick up all the instances initialized before. This also means, if we want to, let's say, change the minimum level of all the logger instances to `WARNING`, we can just call a method in the *main* instance and it will update the level of all the *child* instances.

### Stream

A *stream* is anything where the logger will write to. It can be Standard Output or it can be files.

However, the idea of streams is that, all the logger instances should share a set of streams. This is useful because any logger can write to all the streams this way and it avoids redundancy of the same streams.

>Note that it is a `set` of streams, which means duplicate streams are not allowed.

This is why, as seen in the image above, the final instance of the Logger will leverage the Streams.

So, let's say, you call a log method to log a `DEBUG` message, what actually happens is a write request is sent to all the available streams and these streams accordingly write.

### Formatter

*Formatter* is what handles the formatting of the output. As **Simber** allows the user to have the flexibility to specify format for all the different instances, it is necessary to have something that will dynamically change those passed format to output'able strings. This is done by the formatter.

Let's say the user provided the following format for any said instance

```"{levelname} {message}"```

Now, the above string has two special keywords that the user assumes the Logger will take care of. Thus the *formatter* will come in action here. We pass the above string to the formatter and we get the following output.

>NOTE: Assuming the logger is running in `INFO` and the message passed was `Just a test`

```console
INFO Just a test
```

### Color Formatter

Just like the *formatter*, the *Color Formatter* takes care of formatting the colors. Since **Simber** gives the user the flexibility to specify colors as well as automatically detect colors based on Level, this is necessary.

Let's say we have the following string as the format for any logger instance

```"%gJust a static message%"```

The above format should output the message in the color green. Check the [color docs](/colors) for referrence.

Thus the *Color Formatter* comes in action here and dynamically changes the color just before output. So the above format will output the following string.

<img src="/assets/color_arch.jpg">

## Conclusion

All of the above modules together make up Simber which is aimed at giving the user complete control of the Logger while being useful and powerful.