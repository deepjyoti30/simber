# Simber

## Requirements

Simber tries to be a **minimal** logging library with a lot of functionality. Most of the requirements of Simber are internal except one.

Simber leverages [colorama](https://github.com/tartley/colorama) in order to show colors in the terminal
and keep it working across platforms.

## Installation

### PyPI

`Simber` is available in PyPI [here]()

It can be installed by the following command

```console
pip install simber --user
```

### Manual

`Simber` can be installed manually from GitHub. It can be found [here]()

It can be installed manually by the following steps.

- Clone the repo

```console
git clone git@github.com:deepjyoti30/simber
```

- Move to the directory and run the install script

```console
cd simber && python setup.py install
```

>NOTE: In the above command, you might need to pass `sudo` in order for it to install properly.

## Get Started

### Using it right away

**Simber** can be used right away after installing with a few imports.

Following is a sample code that uses **Simber** and prints some useful statements.

```Python
from simber import Logger

# Create a new instance
logger = Logger("test")

# Print an info statement
logger.info("Just printing an info message from the test logger")

# Print a debug statement.
logger.debug("Just a debug message")

# Above message is not printed because the min level set is INFO

# Print a warning message
logger.warning("A warning message from the test logger")
```
