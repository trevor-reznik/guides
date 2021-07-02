






# Postgres


<a name="new-db"/>

## New Database Setup

[Guide - Creating a psql DB](https://www.postgresql.org/docs/7.4/tutorial-createdb.html)

[createdb docs](https://www.postgresql.org/docs/9.1/app-createdb.html)

1. install

```bash
apt-get update
apt-get install postgresql
```

2. create user (optional)

```bash
sudo -u postgres createuser --interactive -P $USERNAME
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) y
Shall the new role be allowed to create more new roles? (y/n) n
```

3. create db

```bash
sudo -u postgres createdb -O $USERNAME $DB_NAME
sudo -u postgres psql -U $USERNAME -h 127.0.0.1 $DB_NAME
```

4. monitor interactively
```bash
psql -u $USERNAME
```


<a name="credentials"/>

## Credentials

```bash
$ sudo -u postgres psql
\password postgres
\q
```

<a name="config-file"/>

## Config File


<a name="location"/>

###### Location 
pg_hba.conf file (/etc/postgresql/9.1/main/pg_hba.conf*).
```bash
locate pg_hba.conf
```
<a name="restarting-after-changes"/>

###### Restarting after Changes
After altering this file, don't forget to restart your PostgreSQL server. If you're on Linux, that would be sudo service postgresql restart.

These are brief descriptions of both options according to the official PostgreSQL docs on authentication methods.

<a name="peer-authentification"/>

###### Peer Authentification 

[official PostgreSQL docs on authentication methods](http://www.postgresql.org/docs/9.3/static/auth-methods.html)


This line:

```
local   all             postgres                                peer
```

Should be:

```
local   all             postgres                                md5
```



<a name="usage"/>

## Usage

<a name="createdb"/>

**createdb** -- create a new PostgreSQL database

```bash
createdb [connection-option...] [option...] [dbname] [description]
```
createdb creates a new PostgreSQL database.

Normally, the database user who executes this command becomes the owner of the new database. However, a different owner can be specified via the -O option, if the executing user has appropriate privileges.

createdb is a wrapper around the SQL command CREATE DATABASE. There is no effective difference between creating databases via this utility and via other methods for accessing the server.




-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>




-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>
