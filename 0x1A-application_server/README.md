# 0x1A. Application server

## Objective
While a **web server** can also serve **dynamic content**, this task is usually given to an **application server**. In this project I add this piece to my infrastructure, plugging it to my **Nginx** and making it serve the Airbnb clone project.

## Requirements
1. Nginx ==> `sudo apt-get install nginx`
2. Gunicorn ==> `pip install gunicorn`
3. Flask ==> `pip install flask`

## Featured Commands
* `sudo netstat -ntalp | grep 5000` ==> displays all the processes hooked to port 5000
* `python3 -m web_flask.0-hello_route` ==> starts the application server.
* `sudo systemctl stop datadog-agent` ==> This command stops datadog-agent which is using port 5000 from our previous project.

##
