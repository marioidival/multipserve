Multi Pserve
=

Little script for you use in many pservers Pyramid


##How to
Install

    pip install multipserve

First, you can use the python script in your root directory application

    multipserver.py app1 app2 app3 app4

##To do
Multi Pserve works but not how I think ... There are 2 things I need to do to make it actually becomes good enough. Today, it starts the servers (pserve) in daemon mode, the pserve the Pyramid offers and place the script that was used, it creates files pid's and log's with the name of each app that was passed to the multi_pserve.py. I want it to run servers in reload mode, and has a web page or even at the terminal(which I think unlikely/not functional) show the logs of active servers.


Look [issues](https://github.com/marioidival/multi_pserve/issues) for more details.
