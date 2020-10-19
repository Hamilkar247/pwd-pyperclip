import os
import logging
import argparse 
import pyperclip as pc
#def def_parser():


def def_params():
    parser = argparse.ArgumentParser(
            description="Script to send pwd to clipboard"
    )
    parser.add_argument("-l", "--loghami", actin='store_true', help="set debug")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:" + str(args))
    return args


def main():
    args=def_params()
    bas_dir = os.path.dirname(os.path.realpath(__file__))
    logging.debug('pwd:'+ bas_dir)
    pc.copy(bas_dir)


if __name__ == "__main__":
    main()


