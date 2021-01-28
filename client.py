import json
import zmq
from json_checker import Checker
import gevent


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def validate(self):
    current_data = self
    expected_schema = {
        "command_type": str,
        "expression": str,
        "command_name": str,
        "parameters": [
            str
        ]
    }

    try:
        checker = Checker(expected_schema)
        checker.validate(current_data)
        return True

    except not True:
        return False


try:
    for request in range(1, 10):

        file_name = input(Bcolors.BOLD + "Enter your file name :\n" + Bcolors.ENDC)

        open_file = open((file_name + ''))
        data = json.load(open_file)
        if validate(data) is False:
            print("Given JSON file is " + Bcolors.FAIL + "not Valid" + Bcolors.ENDC)
            break
        else:
            print("Given JSON file is " + Bcolors.OKGREEN + "Valid" + Bcolors.ENDC)
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://127.0.0.1:5555")
            print("Sending request " + Bcolors.OKBLUE + "%s" % request + Bcolors.ENDC + " …")

            socket.send_json(data)
            print(Bcolors.BOLD + "Response:" + Bcolors.ENDC)
            message1 = socket.recv_json()
            print(message1)
            print("After a few secends you can send another Request")
            gevent.sleep(10)

except FileNotFoundError and TypeError as error:
    print("There is a " + Bcolors.FAIL + "Error" + Bcolors.ENDC + " : %s" % error)
