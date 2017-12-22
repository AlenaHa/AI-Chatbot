"""Find and extract information from web."""


import abc
import json
import urllib
import urlparse

import requests
import six
from bs4 import BeautifulSoup

from cbot import settings
from cbot.utils import Logger


@six.add_metaclass(abc.ABCMeta)
class BaseCrawler(Logger):

    """Base class for any crawler."""

    # Types of response returned by the `request` method.
    RESPONSE_OBJECT = 1
    RESPONSE_CONTENT = 2
    RESPONSE_JSON = 3
    RESPONSE_SOUP = 4

    # Common URL paths for building final URIs.
    URL_BASE = None

    # Default encoding for br encoded response and unicode search results.
    ENCODING = settings.ENCODING

    # Compressed HTML content depending on the accepted and received encoding.
    DECOMPRESS = {}

    _ACCEPT_ENCODING = [
        "gzip",
        "deflate"
    ]
    HEADERS = {
        "Pragma": "no-cache",
        "Accept-encoding": ", ".join(_ACCEPT_ENCODING),
        "Accept-language": "en-US,en;q=0.8",
        "Upgrade-insecure-requests": "1",
        "User-agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
            "Gecko) Chrome/60.0.3112.24 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/webp,image/apng,*/*;q=0.8"
        ),
        "Cache-control": "no-cache",
    }

    def __init__(self, *args, **kwargs):
        """Intialize with a crawler object."""
        super(BaseCrawler, self).__init__(*args, **kwargs)

        self._session = requests.Session()

    @classmethod
    def normalize_url(cls, url, query=None):
        """Create absolute path URL with normalized unified query."""
        # First, create and absolute URL from a relative one.
        url = urlparse.urljoin(cls.URL_BASE, url)
        # Now split it into chunks for parsing.
        split = list(urlparse.urlsplit(url))
        # Built a new final query based on the previous and the provided one.
        new_query = dict(urlparse.parse_qsl(split[3]))
        new_query.update(query or {})
        # Replace the old query with the newly created one.
        split[3] = urllib.urlencode(new_query)
        # Return the final processed in chunks as URL.
        return urlparse.urlunsplit(split)

    def _normalize_response(self, response, get):
        """Decompress the content before pre-process."""
        if get == self.RESPONSE_SOUP:
            content = response.text
        else:
            content = response.content

        encoding = response.headers.get("Content-Encoding")
        func = self.DECOMPRESS.get(encoding)
        if func:
            if isinstance(content, six.text_type):
                content = content.encode(self.ENCODING)
            content = func(content)

        if get == self.RESPONSE_CONTENT:
            if not isinstance(content, six.binary_type):
                content = content.encode(self.ENCODING)
        elif get == self.RESPONSE_SOUP:
            if not isinstance(content, six.text_type):
                content = content.decode(self.ENCODING)
            content = BeautifulSoup(content, settings.HTML_PARSER)
        elif get == self.RESPONSE_JSON:
            if six.PY3 and not isinstance(content, six.text_type):
                content = content.decode(self.ENCODING)
            content = json.loads(content, encoding=self.ENCODING)
        return content

    def _request(self, url, query=None, headers=None, data=None,
                 get=RESPONSE_OBJECT):
        """Make a full HTTP request and return a response.

        :returns: requested response after a successful call
        :rtype: Response, str, dict, BeautifulSoup
        :raises: `Exception` when connection fails
        """
        # Get the full url plus query value.
        url = self.normalize_url(url, query=query)
        # Prepare the action type depending on the given data.
        if data:
            verb = self._session.post
        else:
            verb = self._session.get
        # Make the request, check it and return a response.
        self.log.debug(
            "%s: %r | %s",
            "GET" if verb == self._session.get else "POST",
            url,
            data
        )
        response = verb(url, headers=headers, data=data,
                        timeout=settings.TIMEOUT)
        response.raise_for_status()

        # Return response depending on the requested type.
        if get == self.RESPONSE_OBJECT:
            return response
        elif get in (
                self.RESPONSE_CONTENT,
                self.RESPONSE_JSON,
                self.RESPONSE_SOUP):
            return self._normalize_response(response, get=get)

        raise Exception(
            "invalid response type {!r}".format(get)
        )

    @abc.abstractmethod
    def get_defs(self, word, limit=1):
        """Returns at most `limit` definitions for `word`."""


class DexCrawler(BaseCrawler):

    """Crawler for dexonline source."""

    URL_BASE = "https://dexonline.ro"

    def get_defs(self, word, limit=1):
        url = "/definitie/{}".format(word)
        soup = self._request(url, headers=self.HEADERS,
                             get=self.RESPONSE_SOUP)
        spans = soup.find_all("span", {"class": "def"})
        defs = []
        for span in spans[:limit]:
            defs.append(span.text.encode(settings.ENCODING).strip())
        return defs


CRAWLERS = {
    "dex": DexCrawler,
}
