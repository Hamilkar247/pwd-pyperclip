import logging
import argparse 
import pyperclip as pc
import subprocess

def def_params():
    parser = argparse.ArgumentParser(
            description="Script to send pwd to clipboard"
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:" + str(args))
    return args


def main():
    args=def_params()
    pwd_var=subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output_pwd = pwd_var.stdout.read() #zawiera cos w stylu '\b\home\matball\projects\n' - 
    pc.copy(str(output_pwd)[3:-1]) #używam substr by nie przekazywać do clipboard zbędnych znaków


if __name__ == "__main__":
    main()
