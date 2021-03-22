This file will contain snippets that are no longer applicable, but things I found noteworthy anyway.

# On mysqlclient python package

It looks like for Ubuntu, additional apt packages are required for the mysqlclient package:


* `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

[Link to Pypi](https://pypi.org/project/mysqlclient/)

I'll have to look into a friendlier mysql driver for python that also plays nicely with flask-sqlalchemy and make the switch.