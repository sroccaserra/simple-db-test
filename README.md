The class `simpleDbTest.SimpleDbTestCase` is a very simple utility class to automate database tests.

No optimisation was made, please use it as a learning tool.

It uses MySQL, but you can easily imagine how to use SQLAlchemy instead for instance.

## Use

For the example to work, you will need to install `python-mysqldb` (for Debian users).

Then, copy the file `cfg/simpleDbTest.cfg` as `cfg/private.cfg`. It will override everything from `cfg/simpleDbTest.cfg`, and will be ignored by Git.

In your private cfg file, fill your MySQL server name, server port, user name, and password.

Then you can run the example:

    $ python testExample.py

You can also use your favourite unit test runner.

