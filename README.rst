PythonSD website
================

This is the *OLD* homepage of the San Diego Python group.
The new (current as of archiving this repo) site is at:
https://www.sandiegopython.org/

The site deployed from the repository:
https://github.com/sandiegopython/pythonsd-django

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

