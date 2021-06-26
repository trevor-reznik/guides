

# Postgres

### Init

```bash
# install
apt-get update
apt-get install postgresql
psql -U postgres
# enter password -> nested shell
postgres-# createdb -O postgres $DB_NAME
postgres-# psql -U postgres -h 127.0.0.1 $DB_NAME
```


### Credentials

```bash
$ sudo -u postgres psql
```

Then:

```bash
\password postgres
```

Then to quit psql:

```bash
\q
```

### Config File


###### Location 
pg_hba.conf file (/etc/postgresql/9.1/main/pg_hba.conf*).
```bash
locate pg_hba.conf
```
###### Restarting after Changes
After altering this file, don't forget to restart your PostgreSQL server. If you're on Linux, that would be sudo service postgresql restart.

These are brief descriptions of both options according to the official PostgreSQL docs on authentication methods.


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



### createdb

createdb -- create a new PostgreSQL database

```bash
createdb [connection-option...] [option...] [dbname] [description]
```

###### Description
createdb creates a new PostgreSQL database.

Normally, the database user who executes this command becomes the owner of the new database. However, a different owner can be specified via the -O option, if the executing user has appropriate privileges.

createdb is a wrapper around the SQL command CREATE DATABASE. There is no effective difference between creating databases via this utility and via other methods for accessing the server.