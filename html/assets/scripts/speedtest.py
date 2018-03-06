from html import HTML
import cgi
from os import popen
from os.path import expanduser

def speedtest():
    return popen('/usr/bin/speedtest-cli --simple').read()

def make_html(text):
    h = HTML()
    p = h.p
    for line in text.splitlines():
        p += line
        p.br
    return p

def save_html(html):
    as_string = str(html)
    with open('speedtest_results.html', 'w') as f:
        f.write(as_string)

save_html(make_html(speedtest()))
