The class `simpleDbTest.SimpleDbTestCase` is a very simple utility class to automate database tests.

No optimisation was made, please use it as a learning tool.

It uses MySQL, but you can easily imagine how to use [SQLAlchemy][s] instead for instance.

Features:

- Reads connection info from a config file
- Config file path overrideable by an environment variable
- Private config file override values (ignored by Git, prevents credentials to
  be commited)
- Closes the connection in case of error
- Executes request and provide results as a list or single value
- Test requests can be executed on various schemas and various hosts, provided
  the corresponding connection info are provide in the config file. This
  enables you to compare values coming from different servers in your tests.

## Run the example

For the example to work, you will need to install `python-mysqldb` (for Debian users), and to fill in your credentials in the config file.

Copy the file `cfg/simpleDbTest.cfg` as `cfg/private.cfg` to create a private version of the config file. It will override everything from `cfg/simpleDbTest.cfg`, and will be ignored by Git.

In your brand new private file, fill your MySQL server name, server port, user name, and password.

Then you can run the example:

    $ python testExample.py

You can also use your favourite unit test runner.

Note : in your config file, you need to have one section for each schema you want to test. The name of the section is the name of the schema. In each section, provide the server name, port, user name and password. This allows to test and compare values coming from different schemas on different servers.


[s]: http://www.sqlalchemy.org/
