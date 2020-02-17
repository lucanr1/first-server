#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()

name = form.getvalue("name")

page = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>Webpage</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>

        <h1>Thank you """ + name + """</h1>

      </body>
    </html>
"""

print(page)
