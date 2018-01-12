# cbot

AI chatbot web app.


## Installation

For this project, we're gonna use Python 2 version.

#### Install Python interpreter and pip:

*Linux*

```bash
$ sudo apt update && sudo apt install --upgrade python python-dev python-setuptools
$ sudo -H easy_install -U pip
```

*Windows*
- download and install desired version from here: https://www.python.org/downloads/
- download and run get-pip script: https://pip.pypa.io/en/stable/installing/

Make sure that you're using the correct version of pip, by running
`pip --version`. It should use the Python 2 version, if not, try with *pip2*.

#### Clone repository and install package:

```bash
$ git clone https://github.com/AlenaHa/AI-Chatbot.git
$ cd AI-Chatbot
$ sudo -H ./setup.sh    # setup.bat on Windows
```


## Usage

#### Run CLI and explore the API commands:

*Linux*

```bash
$ cbot --help
```

If you have trouble with file permissions (cbot.log), don't forget to remove
them with `sudo` first.

*Windows*

```bat
> python bin\cbot --help
```

#### Within CLI:

*Windows*

Crawl the first 3 definitions for a given word using a specific crawler engine.

```bat
> python bin\cbot crawl -c dex -l 3 inteligenta
```

Or simply run the bot API server:

```bat
> python bin\cbot run
```

For the same process you can also execute the *run.bat* or *run-debug.bat* files.

Now the server is running. You can explore the API by executing cURL commands
like these:

```bat
> curl http://localhost:8080/api/profiles
{
    "message": "ok",
    "status": 200,
    "urls": [
        "not implemented yet"
    ]
}
```

Or even chat with the bot:

```bat
> curl -i http://localhost:8080/api/chat?message=ana+are+mere
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 73
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Thu, 11 Jan 2018 22:49:03 GMT

{
    "data": "erem era ana", 
    "message": "ok", 
    "status": 200
}
```

*Linux*

Same commands, just directly execute the `cbot` script without the need to
supply paths, like in the top example above. 

#### Within module:

You can also import **cbot** as a normal python module/library and use it
accordingly in your Python scripts/projects.

*\<details coming soon\>*

## Development

If you want to develop **cbot**, do the following:

#### Optionally install virtualenv:

*Linux*

```bash
$ sudo -H pip install -U virtualenv virtualenvwrapper
$ echo "export WORKON_HOME=~/Envs" >>~/.bashrc
$ source ~/.bashrc
$ mkdir -p $WORKON_HOME
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >>~/.bashrc
$ source ~/.bashrc
$ mkvirtualenv cbot
```

*Windows*

Make sure that you have added your Python *Scripts* path to the system
path already (https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/).
The path you need to add is usually: `C:\Python27\Scripts`.

Now install the necessary pip packages and create your first virtual environment.

```bat
> pip install -U virtualenv virtualenvwrapper virtualenvwrapper-win
> mkvirtualenv cbot
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
