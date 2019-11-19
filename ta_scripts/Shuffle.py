#! /usr/bin/env python
from __future__ import unicode_literals

import django
from django.conf import settings
from django.db import transaction
settings.configure(DEBUG=True)
django.setup()
from resort.models import Deck

def main():
    pass

for i in range(1,16):
    if i > 9:
        e = 'training0{0}@greenphire.com'.format(i)
        u = 'training0{0}@greenphire.com'.format(i)
        print(e,u)
    else:
        e = 'training{0}@greenphire.com'.format(i)
        u = 'training{0}@greenphire.com'.format(i)
        print(e,u)












if __name__ == '__main__':
    import argparse
    from django import setup
    setup()
    parser = argparse.ArgumentParser(
        description='shuffles deck of cards'
    )
    parser.add_argument(
        '--commit', dest='COMMIT', default=False, action='store_true',
        help='Commit script changes to DB'
    )
    args = parser.parse_args()
    with transaction.atomic():
        main()
        if not args.COMMIT:
            raise ValueError("Dry Run. Changes not committed")