#!/usr/bin/env python

import vxi11

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Connects to a device via VXI-11 and prints its response to *IDN?.')
    parser.add_argument('host', help='Host to connect to via VXI-11')
    args = parser.parse_args()

    instr =  vxi11.Instrument(args.host)
    print("The response to an *IDN? query is:")
    print(instr.ask("*IDN?"))
    #print(instr.ask("SYSTem:BEEPer:STATe?"))
    #print(instr.ask("APPLy?"))

    try:
        while True:
            query = input("vxi11 > ")
            print(instr.ask(query.strip()))
    except KeyboardInterrupt:
        print("[Ctrl]-[c] pressed. Exiting...")

if __name__ == "__main__":
    main()

