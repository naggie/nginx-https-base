epgen.py
--------

Used to generate the minimal error pages used by this ansible role. Each page
has necessary assets embedded such that it is not necessary to serve additional
files to serve and route error pages.

Error pages can also be customised with a logo. The logo will be embedded with
a base64 encoded data URI.

Usage: ./epgen.py <logo>
Usage: ./epgen.py nologo

Generate error pages given a logo. The second command gives no logo.

