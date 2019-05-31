# (u)LoopDesigner

uLoopDesigner is a web app for interacting with LoopDB, based on the original LoopDesigner written by Mihails Delhmans from https://github.com/HaseloffLab/LoopDB/tree/loopdesigner. The schema has been implemented for a simplified syntax so that there's less redundancy in (u)Loop libraries.

You can try a public version at [uloopdesigner.herokuapp.com](http://uloopdesigner.herokuapp.com)

# Installation

This section will explain how to install a local (u)LoopDesigner server.

## Gettting Started

### Installing LoopDB
There are several difficulties with the installation that will require basic coding and maybe (depending on the case) debugging. You need command-line skills and at this point I've been successful on running it in MacOS. Linux probably work but I'd suggest using the last version of Ubuntu/Debian.

LoopDB is available through PyPi, so you can just

``` bash
pip install loopdb
```

### Setting up a database

LoopDB is based on [SQLAlchemy] (http://www.sqlalchemy.org), which allows to use most of the
common database back-ends. We recommend using [PostgreSQL](https://www.postgresql.org). After you
have installed PostgreSQL, or any other database server, create a new database. With PostgreSQL it
can be done with

``` bash
createdb loopdb
```

You'll need credentials.

### Install LoopDesigner

Check out the `loopdesigner` branch:

``` bash
git clone https://github.com/HaseloffLab/LoopDB.git -b loopdesigner LoopDesigner
```

This will clone the files to LoopDesigner folder. Now install the requirements:

``` bash
cd LoopDesigner
pip install -r requirements.txt
```

### Starting the server

Now you should be ready to start the LoopDesigning server by running

```bash
python server.py
```

If you didn't get any errors you should be able to access the LoopDesigner by navigating to

http://127.0.0.1:8000

in your browser.

### Schema

The easiest way to define a schema is by using a JSON file. Have a look at the `schema.json` file for an example. The schema has already been included according to a simplified common syntax. Check out the file to see the logic.

### Config
The config file `schema.py` has some important details regarding the location of the databse and where to find the schema file.

```python
>> from loopDB import LoopDB # Importing the LoopDB module

>> loopDB = LoopDB( 'postgresql:///loopdb', clean = True) # Establishing the connection to the database
>> loopDB.initFromFile('schema.json') # Initialising from the schema file
```

### Initialisation
Initiate the database using

```bash
python initialise.py
```

### Loading sample sequences.
```bash
sh load.sh load/
```
