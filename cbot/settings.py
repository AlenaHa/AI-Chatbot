"""cbot default settings."""


import os


# Miscellaneous.
ENCODING = "utf-8"
PROJECT = os.path.normpath(
    # Project directory (package parent).
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir
    )
)
# Relative paths only.
ETC = os.path.join("etc", "cbot")

# Crawler parsing and settings.
HTML_PARSER = "html5lib"
TIMEOUT = 10

# Server settings.
HOST = "0.0.0.0"
PORT = 8080
CONFIG = os.getenv("FLASK_CONFIG") or "default"
(SECRET_KEY_PATH,) = map(
    lambda name: os.path.join(ETC, name),
    [
        "secret.key",
    ]
)

# Logging & debug
LOGGING = True
LOGFILE = "cbot.log"
DEBUG = os.getenv("CBOT_DEBUG", "").lower() in ("1", "true")
