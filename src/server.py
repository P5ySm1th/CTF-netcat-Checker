#!/usr/bin/env python3

from flag import FLAG
import sys
import verify

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[33m'
NORM = '\033[0m'

BANNER = f"""
{YELLOW} 

INSERT YOUR ASCII ART HERE

{NORM}

Welcome to XXXX Challenge!
"""

QUESTIONS = [
    "[1]. Your question here!",
    "[2]. ",
    "[3]. ",
    "[4]. ",
    "[5]. ",
    "[6]. ",
    "[7]. ",
    "[8]. ",
    "[9]. ",
    "[10]. "
]

ANSWERS = [
    "1",
    "2",
    "3",
    ["67C2B2E99EE18A4BFC42EFA407182207", "67C2B2E99EE18A4BFC42EFA407182207".lower()],
    ["ADS", "Alternate Data Streams", "Alternate Data Stream"],
    "4",
    "5",
    "6",
    "7",
    "8"
]

assert len(QUESTIONS) == len(ANSWERS), "Questions and Answers length mismatch!"

QnA = dict(zip(QUESTIONS, ANSWERS))

def getInputnValidate():
    for question, answers in QnA.items():
        print(f"{YELLOW}{question}{NORM}")
        while True:
            user_input = input("Answer: ")
            if user_input in answers:
                print(f"{GREEN}[+] Correct! {NORM}")
                break
            else:
                print(f"{RED}[-] Wrong answer! {NORM}")
                sys.exit(0)

def getFlag():
    print(f"{GREEN}[+] Congrats! Here is your flag: {FLAG}{NORM}")
    sys.exit(0)

def ver1fy():
    challenge = verify.get_challenge(31337)
    print("== proof-of-work: enabled ==")
    print("please solve a pow first")
    print(f"You can run the solver with:")
    print(f"    python3 <(curl -sSL {verify.SOLVER_URL}) solve {challenge}")
    print("===================")
    solution = input("Solution? ").strip()
    
    if verify.verify_challenge(challenge, solution):
        print(f"{GREEN}[+] Correct{NORM}")
    else:
        print(f"{RED}[-] Proof-of-work fail{NORM}")
        sys.exit(1)

def main():
    ver1fy()
    print(BANNER)
    getInputnValidate()
    getFlag()

if __name__ == "__main__":
    main()
