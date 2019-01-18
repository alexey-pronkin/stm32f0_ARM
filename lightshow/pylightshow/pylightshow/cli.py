import argparse
import sys
from . import uart


def play(args):
    pass


def main():
    parser = argparse.ArgumentParser('pylightshow')
    subparsers = parser.add_subparsers()

    parser_play = subparsers.add_parser('play', help='play a file')
    parser_play.set_defaults(handler=play)
    parser_play.add_argument('input_file', type=lambda x: isinstance(x, str) and x.endswith('.wav'))

    args = parser.parse_args()
    if not hasattr(args, 'handler'):
        parser.print_help()
        sys.exit(1)
    args.handler(args)
