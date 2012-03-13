#!/usr/bin/python
"""A quick script that opens a webpage to my local weather"""

import re
import urllib
import webbrowser

def main():
    wund_site = urllib.urlopen("http://www.wunderground.com")
    wund_text = wund_site.read()
    wund_site.close()

    local_url_re = re.compile(r'href="(/cgi-bin/findweather/getForecast\?query=\d+)')
    local_url_m  = local_url_re.search(wund_text)
    if local_url_m:
        local_url = local_url_m.group(1)
        webbrowser.open(r'http://www.wunderground.com%s' % local_url)

if __name__ == "__main__":
    main()
