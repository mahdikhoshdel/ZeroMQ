import zmq
import json
import gevent
from gevent import subprocess

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    gevent.sleep(2)
    message = socket.recv()
    data = json.loads(message)

    command_type = data['command_type']
    expression = data["expression"]
    command_name = data["command_name"]


    def errors(self):
        error_description = self
        result_error = {
            "Server_response": "Error",
            "Description": error_description
        }
        error_json = json.dumps(result_error, indent=4)
        socket.send_json(error_json)


    def parameter():
        parameters = data['parameters']
        for i in range(0, len(parameters)):
            print(parameters[i] + " ", end='')

    def os_command():
        try:
            execute = subprocess.check_output(
                command_name,
                cwd=parameter(),
                shell=True,
            ).decode('utf-8')
            # using replace to isolate keys and values
            execute = execute.replace('\r', '')
            execute = execute.replace('\n', '')
            execute = execute.replace('          ', '')
            result_command = {
                "given_os_command": command_name,
                "result": execute
            }
            directory = json.dumps(result_command, indent=4)
            socket.send_json(directory)

        except FileNotFoundError:
            errors("invalid path for your os command")
        except any:
            errors("Executing OS command Error")

    def compute_command():
        math = str(eval(expression))

        result_expression = {"given_math_expression": expression,
                             "result": math}
        math_json = json.dumps(result_expression, indent=4)
        socket.send_json(math_json)

    if command_type == 'os':
        os_command()

    elif command_type == 'compute':
        compute_command()

    else:
        errors("Out of sort command type in your json file")
