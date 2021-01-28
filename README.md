# ZeroMQ
## Server Client using ZMQ


First of all after run Client, you have to give to the cilent app a json file in the correct format
client going to validation given file and if that was correct then going to sendthe file to Server using ZMQ
if you ran server before, Server listening and reading your spcific command in the json file
then in server, command going to be run and return result as a json format and will send it to the Cilent
In the end Client will show result to user

- If in Server there was a error, Server return error as same json format but spcific for error to the Client
- If in Client error happend, error will return to user as a string
- Client after took your json file and sent it to Server will wait 10 sec (using gevent) for the hole new request
