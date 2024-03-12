## Bind to a port
### Your Task
In this stage, your task is to start a TCP server on port 4221.

How to pass this stage
Since this is your first stage in this challenge, we've included some starter code in your repository. To pass this stage, simply uncomment the code and git push.

Step 1: Uncomment the code in app/main.py.

Step 2: Commit and push your changes.

Run the following commands to submit your changes:

git add .
git commit -m "pass 1st stage" # any msg
git push origin master

<hr>
<hr>

## Respond with 200
### Task
In this stage, you'll respond to a HTTP request with a 200 OK response.

Your program will need to:

Accept a TCP connection
Read data from the connection (we'll get to parsing it in later stages)
Respond with HTTP/1.1 200 OK\r\n\r\n (there are two \r\ns at the end)
HTTP/1.1 200 OK is the HTTP Status Line.
\r\n, also known as CRLF, is the end-of-line marker that HTTP uses.
The first \r\n signifies the end of the status line.
The second \r\n signifies the end of the response headers section (which is empty in this case).
It's okay to ignore the data received from the connection for now. We'll get to parsing it in later stages.



## Respond with 404
In this stage, your program will need to extract the path from the HTTP request.

Here's what the contents of a HTTP request look like:

GET /index.html HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1
GET /index.html HTTP/1.1 is the start line.
GET is the HTTP method.
/index.html is the path.
HTTP/1.1 is the HTTP version.
Host: localhost:4221 and User-Agent: curl/7.64.1 are HTTP headers.
Note that all of these lines are separated by \r\n, not just \n.
In this stage, we'll only focus on extracting the path from the request.

If the path is /, you'll need to respond with a 200 OK response. Otherwise, you'll need to respond with a 404 Not Found response.



## Respond with content
In this stage, your program will need to respond with a body. In the previous stages we were only sending a status code, no body.

The task here is to parse the path from the HTTP request. We will send a random string in the url path you will need to parse that string and then respond with the parsed string (only) in the rsponse body.

The tester will send you a request of the form GET /echo/<a-random-string>.

Your program will need to respond with a 200 OK response. The response should have a content type of text/plain, and it should contain the random string as the body.

As an example, here's a request you might receive:

GET /echo/abc HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1
And here's the response you're expected to send back:

HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 3

abc
Remember, lines in the response are separated by \r\n, not just \n.



## Parse headers
In this stage, your program will need to parse HTTP request headers.

The tester will send you a request of the form GET /user-agent, and it'll include a User-Agent header.

Your program will need to respond with a 200 OK response. The response should have a content type of text/plain, and it should contain the user agent value as the body.

For example, here's a request you might receive:

GET /user-agent HTTP/1.1
Host: localhost:4221
User-Agent: curl/7.64.1
and here's the response you're expected to send back:

HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 11

curl/7.64.1


## Concurrent connections
Up until now, we've only tested your program against a single connection in each stage.

In this stage, your server will need to handle multiple concurrent connections.

The tester will send you multiple requests at the same time. Your server will need to respond to all of them.



## Get a file
In this stage, your server will need to return the contents of a file.

The tester will execute your program with a --directory flag like this:

./your_server.sh --directory <directory>
It'll then send you a request of the form GET /files/<filename>.

If <filename> exists in <directory>, you'll need to respond with a 200 OK response. The response should have a content type of application/octet-stream, and it should contain the contents of the file as the body.

If the file doesn't exist, return a 404.

We pass in absolute path to your program using the --directory flag.



## Post a file
In this stage, your server will need to accept the contents of a file in a POST request and save it to a directory.

Just like in the previous stage, the tester will execute your program with a --directory flag like this:

./your_server.sh --directory <directory>
It'll then send you a request of the form POST /files/<filename>. The request body will contain the contents of the file.

You'll need to fetch the contents of the file from the request body and save it to <directory>/<filename>. The response code returned should be 201.

We pass in absolute path to your program using the --directory flag.


## Final Tests => Test Logs
Running tests on your code. Logs should appear shortly...
remote:
remote: [stage-1] Running tests for Stage #1: Bind to a port
remote: [stage-1] Connecting to localhost:4221 using TCP
remote: [stage-1] Success! Closing connection
remote: [stage-1] Test passed.
remote:
remote: [stage-2] Running tests for Stage #2: Respond with 200
remote: [stage-2] You can use the following curl command to test this locally
remote: [stage-2] $ curl -v -X GET http://localhost:4221/
remote: [stage-2] Sending request (status line): GET / HTTP/1.1
remote: [stage-2] Test passed.
remote:
remote: [stage-3] Running tests for Stage #3: Respond with 404
remote: [stage-3] You can use the following curl command to test this locally
remote: [stage-3] $ curl -v -X GET http://localhost:4221/Monkey/donkey
remote: [stage-3] Sending request (status line): GET /Monkey/donkey HTTP/1.1
remote: [stage-3] Test passed.
remote:
remote: [stage-4] Running tests for Stage #4: Respond with content
remote: [stage-4] You can use the following curl command to test this locally
remote: [stage-4] $ curl -v -X GET http://localhost:4221/echo/dooby/Coo-Monkey
remote: [stage-4] Sending request (status line): GET /echo/dooby/Coo-Monkey HTTP/1.1
remote: [stage-4] Test passed.
remote:
remote: [stage-5] Running tests for Stage #5: Parse headers
remote: [stage-5] You can use the following curl command to test this locally
remote: [stage-5] $ curl -v -X GET http://localhost:4221/user-agent -H "User-Agent: 237/donkey-237"
remote: [stage-5] Sending request (status line): GET /user-agent HTTP/1.1
remote: [stage-5] Test passed.
remote:
remote: [stage-6] Running tests for Stage #6: Concurrent connections
remote: [stage-6] Creating 2 parallel connections
remote: [stage-6] Sending request on 2 (status line): GET / HTTP/1.1
remote: [stage-6] Sending request on 1 (status line): GET / HTTP/1.1
remote: [stage-6] Test passed.
remote:
remote: [stage-7] Running tests for Stage #7: Get a file
remote: [stage-7] Testing existing file
remote: [stage-7] You can use the following curl command to test this locally
remote: [stage-7] $ curl -v -X GET http://localhost:4221/files/237_humpty_Horsey_donkey
remote: [stage-7] Sending request (status line): GET /files/237_humpty_Horsey_donkey HTTP/1.1
remote: [stage-7] Testing non existent file returns 404
remote: [stage-7] You can use the following curl command to test this locally
remote: [stage-7] $ curl -v -X GET http://localhost:4221/files/non-existent237_237_237_scooby
remote: [stage-7] Sending request (status line): GET /files/non-existent237_237_237_scooby HTTP/1.1
remote: [stage-7] Test passed.
remote:
remote: [stage-8] Running tests for Stage #8: Post a file
remote: [stage-8] You can use the following curl command to test this locally
remote: [stage-8] $ curl -v -X POST http://localhost:4221/files/dumpty_scooby_dooby_Horsey -d 'Monkey dumpty 237 monkey dumpty vanilla monkey Coo'
remote: [stage-8] Sending request (status line): POST /files/dumpty_scooby_dooby_Horsey HTTP/1.1
remote: [stage-8] Test passed.
remote:
remote: All tests passed. Congrats!
remote:
remote: Want to try another language or approach? Visit the course page:
remote: https://app.codecrafters.io/courses/http-server
remote:
To https://git.codecrafters.io/0ca64239c94482a8
   a38d5f8..84600e0  master -> master