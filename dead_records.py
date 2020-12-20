#!/usr/bin/python3

# Dependencies
import sys
import subprocess
import argparse
import os
import re
import pathlib
from time import sleep
from termcolor import colored, cprint
from concurrent.futures import ThreadPoolExecutor

# Banner
def banner():
    print("\033[91m")

    print("              ------------------------                                             ______")
    print("             /  |\    |\    |  -----  \                         |\_______________ (_____\\______________")
    print("            /   | \   | \   | /        \                HH======#H###############H#######################")
    print('           /    |  \  |  \  | ------    \                       \' ~""""""""""""""`##(_))#H\"""""Y########')
    print('          /     |  /  |   \ |      /     \                                       ))    \#H\       `"Y###')
    print('         /      | /   |    \| ----/       \                                      "      }#H)')
    print('        /      _____       _____           \                                                _')
    print('       /       (  *  )     (  *  )          \                    _ __ ___  ___ ___  _ __ __| |___')
    print("      /                                      \                   | '__/ _ \/ __/ _ \| '__/ _` / __|")
    print('      \          ___________________          /                  | | |  __/ (_| (_) | | | (_| \__ \ ')
    print('       \        /___________________\        /                   |_|  \___|\___\___/|_|  \__,_|___/')
    print('        \                                   /                   ')
    print('         ----------------------------------- ')


    print("Press Control+C to stop anytime\033[0m\n")

# Check args
def args():
    global subdomains_file
    parser = argparse.ArgumentParser()
    print("Usage example: python3 dead_records.py -w subdomains.txt -o1 dead.txt -o2 cname.txt\n")
    parser.add_argument('-w', help='path to the list of subdomain file (required)', required=True)
    parser.add_argument('-o1', help='found dead records output (required)', required=True)
    parser.add_argument('-o2', help="found CNAME's from dead records output (required)", required=True)
    args = parser.parse_args()

    subdomains_file = open(sys.argv[2], "r").readlines()

# filter_dns
def filter_dns(wordz):
    filtration = str(wordz)
    filt = "b'|Host|not found:|3|NXDOMAIN|\\n"
    filt1 = re.sub(filt, '', filtration)
    filt2 = filt1.replace("()", "")
    filt3 = filt2.replace('[" ', '').replace('"]', "")
    filt4 = filt3.replace("\\n'", "")
    formatted  = filt4.replace("\\", "\n").replace(" ", "")

    return formatted

# Find dead dns
def dead_check(subz):
    global show_dead
    try:
        for s in subz:
            cmd = "host " + s
            p = p = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
            dead = p.stdout.read()

            if "not found" in str(dead):
                dead_temp = open("dead-temp.txt", "a+")
                dead_temp.write(str(dead))
            else:
                continue

        exist_check = pathlib.Path("dead-temp.txt")
        if exist_check.exists() == True:
            pass
        else:
            print("\033[91mNO DEAD RECORDS FOUND :(")
            sys.exit(1)

        cprint("\033[96m\033[4mFOUND DEAD RECORDS:\n\033[0m", attrs=['blink'])

        read_dead = open("dead-temp.txt", "r").readlines()
        show_dead = filter_dns(read_dead)
        print("\033[93m")

        return show_dead

    except KeyboardInterrupt:
        os.remove("dead-temp.txt")
        sys.exit(1)


# Make temp file
def CNAME_check(deadz):
    try:
        try:
            for d in deadz:
                cmd = "dig CNAME +short " + d
                p = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
                check = p.stdout.read()

                if len(check) == 0:
                    print("\033[91m" + str(d), " --> \033[0m")

                else:
                    print("\033[92m\033[4m" + str(d) + "\033[0m" +  " --> " + "\033[92m\033[4m" + check.decode() + "\033[0m")
                    write_cname = open("cname-temp.txt", "a+")
                    cnamez = str(d) + " --> " + check.decode() + "\n"
                    write_cname.write(cnamez)
        except KeyboardInterrupt:
            os.remove("cname-temp.txt")
            sys.exit(1)

    except KeyboardInterrupt:
        os.remove("cname-temp.txt")
        sys.exit(1)

def output():
    if len(sys.argv) > 4:
        o1 = sys.argv[4]
        found_dead = open(o1, "w")
        found_dead.write(str(multithread()))

    os.remove("dead-temp.txt")

    cprint("\033[96m\033[4mCHECKING FOR CNAME's: \n\033[0m", attrs=['blink'])

    dead = show_dead.split("\n")
    dead.pop()
    CNAME_check(dead)

# write to temp file
def writeTemp():
    if len(sys.argv) > 5:
        o2 = sys.argv[6]
        cname_temp = open("cname-temp.txt", "r").readlines()
        found_dead_cnames = open(o2, "w")
        found_dead_cnames.write(str(cname_temp))

    os.remove("cname-temp.txt")

def multithread():
    executor = ThreadPoolExecutor(5)
    future = executor.submit(dead_check, subdomains_file)
    print(future.result())

def output():
    if len(sys.argv) > 4:
        o1 = sys.argv[4]
        found_dead = open(o1, "w")
        found_dead.write(str(multithread()))

    os.remove("dead-temp.txt")

    cprint("\033[96m\033[4mCHECKING FOR CNAME's: \n\033[0m", attrs=['blink'])

    dead = show_dead.split("\n")
    dead.pop()
    CNAME_check(dead)

def info():
    print("\033[1m\033[95m\033[4mSEARCHING FOR DEAD DNS RECORDS: \033[00m\n")
    print("\033[93m[-_-] Please sit back and grab a caffe, this might take a bit depending on the file size.\033[00m\n")

def main():
    args()
    banner()
    info()
    output()
    writeTemp()

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\033[91mCtrl+C detected.\n Exiting..\033[0m")
    sys.exit(1)
