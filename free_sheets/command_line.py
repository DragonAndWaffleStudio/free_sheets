from . import free_sheets
import argparse

def main():
    parser = argparse.ArgumentParser(prog = 'free_sheets', description = 'Tries to get a musescore page and extract its music sheets')

    parser.add_argument('url', help = 'a musescore webpage')

    args = parser.parse_args()

    print(f'Trying to get sheets from {args.url} ...')
    free_sheets.main(args.url)
    print(f'Success!')
