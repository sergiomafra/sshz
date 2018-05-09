#!/usr/bin/env python3

import argparse
import re
import subprocess

class sshz():

    def _url_cleaner(self, url):
        ''' Cleans the url passed as an argument '''

        url_reg = re.compile(
            '(https?://)?(www.)?(([a-z0-9\-]*(\.){1})+[a-z]{2,3})'
        )

        return url_reg.search(url).group(3)

    def run(self):
        ''' Run, Forest. Run! '''

        parser = argparse.ArgumentParser(
            description = (
                'SSH that cleans up the specified  url, resolve it and to '
                'connect to a server'
            )
        )
        parser.add_argument(
            'url',
            help='url to resolve and connect to a cloud'
        )
        parser.add_argument(
            '-m', '--mosh',
            default = False,
            action = 'store_true',
            help = 'Uses MOSH instead of SSH'
        )
        parser.add_argument(
            '-u', '--user',
            default = 'root',
            help = 'Defines the login user'
        )
        args = parser.parse_args()

        url = self._url_cleaner(args.url)

        command = 'mosh' if args.mosh else 'ssh'

        subprocess.call(
            '{} root@{}'.format(command, url),
            shell=True
        )

if __name__ == '__main__':
    sshz().run()
