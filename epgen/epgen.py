#!/usr/bin/env python3
"""
Usage: {0} <logo>
Usage: {0} nologo

Generate error pages given a logo. The second command gives no logo.
"""
from sys import argv, exit
from os.path import dirname
from os.path import realpath
from os.path import join
import jinja2
from base64 import b64encode
from mimetypes import guess_type

__version__ = '0.1'
SCRIPT_DIR = dirname(realpath(__file__))


def main():
    if len(argv) < 2:
        print(__doc__.format(argv[0]))
        exit(1)

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(SCRIPT_DIR, 'templates')),
    )

    logo_file = argv[1]

    if logo_file != 'nologo':
        with open(logo_file, 'rb') as f:
            env.globals['logo_data_uri'] = 'data:{mimetype};base64,{data}'.format(
                mimetype=guess_type(logo_file)[0],
                data=b64encode(f.read()),
            )

    template = env.get_template('error.html')

    template.stream(
        title="Permission denied",
        message="Access from the VPN or internal network only"
    ).dump('denied.html')

    template.stream(
        title="Internal server error",
        message="Please try again later or contact us"
    ).dump('error.html')

    template.stream(
        auto_retry=True,
        title="System offline",
        message="Essential maintenance in progress<br>Your session will resume when complete"
    ).dump('offline.html')

    template.stream(
        title="404 Not Found",
        message="The resource you are trying to access does not exist"
    ).dump('notfound.html')

    template.stream(
        title="429 Too Many Requests",
        message="Rate limit exceeded. Please wait and try again.",
    ).dump('ratelimit.html')


if __name__ == "__main__":
    main()
