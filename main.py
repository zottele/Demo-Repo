#
#
# Licensed under the Apache License, Version 2.0 (the "License");
#
import math
import os
import sys

import requests


import numpy as np

# print(sys.version)
# print(sys.executable)


def main():

    test = "Test"
    r = requests.get("https://coreyms.com")
    # print(r.status_code)
    if r.status_code != 200:
        print("not ok")
    else:
        print("Got Site")
    print(r.content)


if __name__ == "__main__":
    main()
