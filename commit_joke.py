#!/bin/python3
import time
import random

def main(print):
    def joke():
        jokes = ["(clap) (clap) (clap)",
                 "(victory)",
                 "(like)",
                 "(champagne)",
                 "(cool)",
                 "(fistbump)"
        ]
        return random.choice(jokes)
    time.sleep(3)
    print("#Aprove")

    time.sleep(5)
    print("#Merge")

    time.sleep(5)
    print("#Abrass")

    time.sleep(5)
    print("C.A.M.A Method succesfull\n{}".format(joke()))
