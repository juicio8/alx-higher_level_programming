#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


if __name__ = "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        data = res.read()
        print("Body response:")
        print("\t - type: {}".format(type(data)))
        print("\t - content: {}".format(data))
        print("\t - utf-8 content: {}".format(the_page.decode("utf-8")))
