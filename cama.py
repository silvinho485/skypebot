import random
from time import sleep


def main(send_message):
    def joke():
        jokes = [
            "(clap) (clap) (clap)",
            "(victory)",
            "(like)",
            "(champagne)",
            "(cool)",
            "(fistbump)"
        ]
        return random.choice(jokes)

    sleep(3)
    send_message("#approve")

    sleep(5)
    send_message("#merge")

    sleep(5)
    send_message("#abrass")

    sleep(5)
    send_message("C.A.M.A Method succesfull\n{}".format(joke()))
