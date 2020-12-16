**************************
Getting Started with Creo
**************************

Creo is an open source deal and lead management platform that provides emerging VC funds and other organizations easy on-premise data management. Currently, features include:

* Create and manage users and permissions
* Add deals, contacts, and files to on-premise SQL database
* One-click installation with database initialization

Quick Start
============

Retrieve the latest code from GitHub source:
::

    $ git clone git@github.com:ShaolinZhang/creo.git
    $ cd creo

Assuming you have Python already, install all dependencies:
::

    $ pip install -r requirements.txt

Modify ``.env.dev`` to include database connection information:

.. code-block:: html

    HOSTNAME=<YOUR_HOSTNAME>
    USERNAME=<YOUR_USERNAME>
    PASSWORD=<YOUR_PASSWORD>
    DATABASE_NAME=<YOUR_DB_NAME>

Initialize your database by running the database initialization script:
::

    $ python scripts/init_db.py

If successful, you will see the following output from terminal:
::

    Connection to MySQL DB successful
    Query executed successfully
    Query executed successfully
    Query executed successfully
    Database initialization successful

Customizing Appearances
========================

All strings for customizing appearances are also in the ``.env.dev`` file such as company name.
