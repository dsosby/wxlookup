#!/usr/bin/python
"""A quick script that opens a webpage to my local weather"""

import urllib

def main():
    wund_site = urllib.urlopen("http://wxunderground.com")
    wund_text = wund_site.read()
    wund_site.close()

    print wund_text

if __name__ == "__main__":
    main()
