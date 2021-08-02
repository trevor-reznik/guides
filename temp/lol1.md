
# Postgres


<a name="table-of-contents"/>

###### Table of Contents


- [**POSTGRES**](#Postgres)
- [**TABLE OF CONTENTS**](#Table-of-Contents)
- [**LOCATION**](#Location)
- [**RESTARTING AFTER CHANGES**](#Restarting-after-Changes)
- [**PEER AUTHENTIFICATION**](#Peer-Authentification)




# Postgres


<p>


<details>
<summary markdown="span">**Postgres**</summary>




<a name="table-of-contents-"/>


- [**POSTGRES**](#Postgres)

# Postgres

<a name="table-of-contents"/>





-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Very Top (目次)</a></div>






</details>

</p>




<a name="Table-of-Contents"/>

###### Table of Contents


<p>


<details>
<summary markdown="span">**Table of Contents**</summary>




<a name="table-of-contents-"/>


- [**TABLE OF CONTENTS**](#Table-of-Contents)
- [**NEW DATABASE SETUP**](#New-Database-Setup)
- [**CREDENTIALS**](#Credentials)
- [**CONFIG FILE**](#Config-File)

###### Table of Contents

- [**NEW DATABASE SETUP**](#new-db)
- [**CREDENTIALS**](#credentials)
- [**CONFIG FILE**](#config-file)
- [***Location***](#location)
- [***Restarting after changes***](#restarting-after-changes)
- [***Peer authentification***](#peer-authentification)
- [**USAGE**](#usage)



<a name="new-db"/>



<a name="New-Database-Setup"/>

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



<a name="Credentials"/>

## Credentials

```bash
$ sudo -u postgres psql
\password postgres
\q
```

<a name="config-file"/>



<a name="Config-File"/>

## Config File


<a name="location"/>





-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Very Top (目次)</a></div>






</details>

</p>




<a name="Location"/>

###### Location 


<p>


<details>
<summary markdown="span">**Location**</summary>




<a name="table-of-contents-"/>


- [**LOCATION**](#Location)

###### Location 
pg_hba.conf file (/etc/postgresql/9.1/main/pg_hba.conf*).
```bash
locate pg_hba.conf
```
<a name="restarting-after-changes"/>





-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Very Top (目次)</a></div>






</details>

</p>




<a name="Restarting-after-Changes"/>

###### Restarting after Changes


<p>


<details>
<summary markdown="span">**Restarting after Changes**</summary>




<a name="table-of-contents-"/>


- [**RESTARTING AFTER CHANGES**](#Restarting-after-Changes)

###### Restarting after Changes
After altering this file, don't forget to restart your PostgreSQL server. If you're on Linux, that would be sudo service postgresql restart.

These are brief descriptions of both options according to the official PostgreSQL docs on authentication methods.

<a name="peer-authentification"/>





-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Very Top (目次)</a></div>






</details>

</p>




<a name="Peer-Authentification"/>

###### Peer Authentification 


<p>


<details>
<summary markdown="span">**Peer Authentification**</summary>




<a name="table-of-contents-"/>


- [**PEER AUTHENTIFICATION**](#Peer-Authentification)
- [**USAGE**](#Usage)

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



<a name="Usage"/>

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

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Very Top (目次)</a></div>






</details>

</p>



<div align="center" style="text-align: center; font-family: monospace; allign: center">
Made with <g-emoji class="g-emoji" alias="heart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png">
   <img class="emoji" alt="heart" height="20" width="20" src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png"></g-emoji>
 <a href="https://www.bymyself.life">bymyself</a></div>

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"> <a href="#table-of-contents">Top (目次)</a>
</div>

