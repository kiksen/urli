from urllib.parse import urlparse, urlunparse


def remove_password(url_str: str) -> str:
    parsed = urlparse(url_str)
    if parsed.password:
        netloc = parsed.netloc.replace(parsed.password, "****")
        return urlunparse(parsed._replace(netloc=netloc))
    return url_str
