# cbot

AI chatbot web app.

## Installation

#### Install Python interpreter and pip:

*Linux*

```bash
$ sudo apt update && sudo apt install --upgrade python python-dev python-setuptools
$ sudo -H easy_install -U pip
```

*Windows*
- download and install desired version from here: https://www.python.org/downloads/
- download and run get-pip script: https://pip.pypa.io/en/stable/installing/

#### Clone repository and install package:

```bash
$ git clone https://github.com/AlenaHa/AI-Chatbot.git
$ cd AI-Chatbot
$ sudo -H ./setup.sh    # setup.bat on Windows
```


## Usage

#### Run CLI and explore the API commands:

```bash
$ cbot --help
```

If you have trouble with file permissions (cbot.log), don't forget to remove
them with `sudo` first.

#### Within CLI:

#### Within module:

## Development

If you want to develop **cbot**, do the following:

#### Optionally install virtualenv:

```bash
$ sudo -H pip install -U virtualenv virtualenvwrapper
$ echo "export WORKON_HOME=~/Envs" >>~/.bashrc
$ source ~/.bashrc
$ mkdir -p $WORKON_HOME
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >>~/.bashrc
$ source ~/.bashrc
$ mkvirtualenv cbot
```

Use `workon cbot` command to activate the virtual environment every time you
want to work through it and `deactivate` for leaving it.

#### Install requirements and develop:

```bash
$ pip install -Ur requirements.txt
$ python setup.py develop
$ python setup.py test
```

Don't forget to run with `sudo -H` if you're working outside the virtualenv.

#### Run tests, create and serve documentation:

```bash
$ nosetests
$ cd doc && make html
$ cd _build/html && python -m SimpleHTTPServer
```

Enter http://localhost:8000 to view documentation.

----

* Source: https://github.com/AlenaHa/AI-Chatbot.git
* License: MIT
