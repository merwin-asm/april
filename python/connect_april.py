"""
AprilAPI 1.0.0

Module to work with april

Author : Merwin
"""

import json
import sys


class April:
    def __init__():
        pass

    def recv_request():
        n = sys.argv[1]
        f = open("." + str(current_id) + ".input", "r")
        d = json.loads(f.read())
        f.close()

        return d

    def send_response(response):
        n = sys.argv[1]
        f = "." + str(n) + ".output"
        f = open(f, "w")
        f.write(json.dumps(response))
        f.close()


