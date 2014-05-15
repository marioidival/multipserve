MultiPserve
===========

!https://travis-ci.org/marioidival/multipserve.svg?branch=master!:https://travis-ci.org/marioidival/multipserve

How To
------

First, you can use the python script in your root directory for start servers

    mpserve --apps app1 app2 app3 app4


*app's* are directory of applications


After, multipserve creates pid and log file with name of each application

    app1.pid app1.log


For killing, you can using this:

    mupserve (-k|--kill) app1 app2 app3


If app killed successfully

    kill app1 with pid 41235

Issues
------
Multi Pserve works but not how I think...  

I want it to has a web page or even at the terminal
(which I think unlikely/not functional) show the logs of active servers.

Look `issues <https://github.com/marioidival/multi_pserve/issues/>`_  for more details.


1. All application now are loaded in --reload mode
#. ``multipserve`` creates a .log and a .pid files for each application
#. multipserve works with arguments
#.  ``--apps`` or ``--kill``
