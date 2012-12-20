PythonSD website
================

This is the homepage of the San Diego Python group.

Generating the website
----------------------

::

  % pip install -r requirements.txt
  % make html


Viewing the site locally
------------------------

Start the development server

::

  % ./develop_server.sh start
  
Stop the development server

::

  % ./develop_server.sh stop


Publishing to Github
--------------------

::

  % make github

