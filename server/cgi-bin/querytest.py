#!/usr/bin/env python3

html_body = """
<html><body>
foo = %s
</body></html>"""

import cgi

form = cgi.FieldStorage()    # (1)
print( "Content-type: text/html¥n")
print(html_body % foo)


