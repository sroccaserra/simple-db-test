The class `simpleDbTest.SimpleDbTestCase` is a very simple utility class to automate database tests.

No optimisation was made, please use it as a learning tool.

It uses MySQL, but you can easily imagine how to use [SQLAlchemy][s] instead for instance.

Features:

- Reads connection info from a config file
- Config file path overrideable by an environment variable
- Private config file override values (ignored by Git, prevents credentials to be commited)
- Closes the connection in case of error
- Executes request and provide results as a list or single value

## Use

For the example to work, you will need to install `python-mysqldb` (for Debian users).

Then, copy the file `cfg/simpleDbTest.cfg` as `cfg/private.cfg`. It will override everything from `cfg/simpleDbTest.cfg`, and will be ignored by Git.

In your private cfg file, fill your MySQL server name, server port, user name, and password.

Then you can run the example:

    $ python testExample.py

You can also use your favourite unit test runner.


[s]: http://www.sqlalchemy.org/
