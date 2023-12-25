#!/usr/bin/env python

import time
import socket
import subprocess
import sys

def wait_for_db():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('db', 3306))
            sock.close()
            return
        except:
            print('Waiting for the database to be up...')
            time.sleep(1)

if __name__ == '__main__':
    wait_for_db()
    subprocess.call(sys.argv[1:])
