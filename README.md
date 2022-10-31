
## How to run basic instructions

### Step 1 install dependencies
Firstly I install a http-server so we have an easy enough way to run our frontend code.
`npm install --global http-server`

This tells us where the dependancies are downloaded
`npm root -g`

Now for the python backend dependencies
`pip install flask flask-cors`

### Step 2 start the backend
After this run the python program which initiates the backend server on local port 6969 :D
`cd backend`
`python3 app.py`

After you run it you should see something like this:
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:6969
Press CTRL+C to quit
```




### Step 3 start the front end

First enter the front end directory
`cd frontend`

Within the directory http-server you will find a bin directory.
In the bin directory find a js executable called http-server
You want to run this on local host 8080
`node http-server -a localhost -p 8080 -c-1 --cors --t`

**NOTE: (You can set up a path for http-server)**

Your expected output should be something like this:
```bash
Starting up http-server, serving ./

http-server version: 14.1.1

http-server settings: 
CORS: true
Cache: -1 seconds
Connection Timeout: 120 seconds
Directory Listings: visible
AutoIndex: visible
Serve GZIP Files: false
Serve Brotli Files: false
Default File Extension: none

Available on:
  http://localhost:8080
Hit CTRL-C to stop the server
```

### Step 4 open index file at http://localhost:8080
To do this simply control click on the http://localhost:8080

Then click 'Get user data'

You final output should look something like this

https://prnt.sc/osAhnM-2zjwv




