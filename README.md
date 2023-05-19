# ZeroMQ
## Client / Server using ZMQ
### Summary
This is a Request/Reply method the most basic pattern `client/server` model, where client sends a request and server replies to the request.
---

### Instruction
First of all after running Client, you have to give a JSON file to the Client script in right format;
client going to validation given file and if that was correct then going to send that file to the Server using ZMQ.
if you ran server before, Server listening and reading your `Spcific Command` in the json file
then in server, command going to be run and return result as a json format and will send it to the Cilent
In the end Client will show result to user.

- If in Server there was a error, Server return error as same json format but spcific for error to the Client
- If in Client error happend, error will return to user as a string
- Client after took your json file and sent it to Server will wait 10 sec (using gevent) for the hole new request


### JSON file
There is 2 type of command you can use in your json :


### 1) `OS commands`
like :
```json
{
    "command_type": "os",
    "command_name": "ls",
    "parameters":
    [
    "/home/me",
        "-h",
        "-l",
    ]
}

```

---
### 2) `Compute commands`
like:
```json
{
    "command_type": "compute",
    "expression": "((30+10)*5+1+1)"
}
```
---
Ps : It's necessary to use exact field name and command type like you see in 2 example in the top
