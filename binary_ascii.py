#!/usr/bin/python3

# decode from ascii to binary
def text():
    text = input(f"\nEnter a string to encode as binary >: ")
    t_bin = bin(int.from_bytes(f'{text}'.encode(), 'big'))
    print(f"\n{t_bin}\n")

# decode from binary to ascii
def binary():
    binary = input(f"\n Enter binary with no spaces to decode into ascii text >: ")
    n = int(f'{binary}', 2)
    n_bin = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(f"\n{n_bin}\n")

def execute():
    bin_or_text = input(f"\n Type 'b' to encode text to binary or 't' to decode binary to ascii text :> ")
    if bin_or_text == "b":
        text()
    else:
        binary()

execute()