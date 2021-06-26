# New Project


```bash
mkdir $PROJECT
cd $PROJECT
git init
touch README.md
touch .gitignore
echo $STUFF > .gitignore
```
github.com/new

```bash
git remote add origin git@github.com:username/repo_name.git
git remote add origin https://github.com/username/new_repo

git add .
git commit -m "init"
git push -u origin master
```



## Python

```bash
python -m venv env
touch requirements.txt
pip3 install $DEPENDENCIES
echo "$DEPENDENCIES" >> requirements.txt
```


## Node

```bash
npm init -y
vim package.json
npm install $DEPENDENCIES
``` 

**Typescript**

```bash
npm install typescript
npm install --save @types/node   # type definitions for Node.js
npx tsconfig.json                # typescript config file somehow

# ts-node test
npm install ts-node
vim package.json
  "scripts": {
    "start": "ts-node src/index.ts"
  },

mkdir src
touch src/index.ts
npm start                        # runs src/index.ts

# watch mode
vim package.json
  "scripts": {
    "watch" : "tsc -w",
npm run watch                    # compiles src/index.ts to js -> create dist folder with index.js


# new terminal
node dist/index.js               # executes js code in index.js
vim package.json
  "scripts": {
    "watch" : "tsc -w",
    "start" : "node dist/index.js",
    "start2": "ts-node src/index.ts"
  },
# start2 runs ts-node on typscript file
# start runs node on js file
# watch compiles live

# nodemon
vim package.json 
  "scripts": {
    "dev" : "nodemon dist/index.js",
npm install nodemon              # listens for any changes to file and reruns file

# nodemon with ts
vim package.json 
  "scripts": {
    "dev2" : "nodemon --exec ts-node src/index.ts",   # live with ts instead

npm run dev                      # runs live-updating that re-executes on save file

# terminal 1 (npm run watch) -> live compiling changes to ts file to index.js
# terminal 2 (npm run dev) -> re-running index.js on changes
```
**Postgres**

```bash
# install
apt-get update
apt-get install postgresql
psql -U postgres
# enter password -> nested shell
postgres-# createdb -O postgres $DB_NAME
postgres-# psql -U postgres -h 127.0.0.1 $DB_NAME

# terminal 3 (psql) postgres database
```

**Mikro-orm**

```bash
npm install @mikro-orm/cli @mikro-orm/core @mikro-orm/migrations @mikro-orm/postgresql pg
```
```JavaScript
const main = async () => {
    const orm = await MikroORM.init({
        dbName: "binder",
        user : "postgres",
        password : "postgres",
        type: "postgresql",
        debug: !__prod__,
    });
};

main();
```

```bash
touch src/constants.ts
vim !:!
```

```javascript
export const __prod__ = process.env.NODE_ENV === "production"
```

```javascript
import { __prod__ } from "./constants";
```

[defining entities w/ mikrorm](https://mikro-orm.io/docs/defining-entities)

```bash
mkdir src/entities
touch !:!/Post.ts
```

```javascript
    const orm = await MikroORM.init({
        entities: "binder",
```




### Website

- filezilla -> bymyself.life 
  - help modal update
  - symlink update
- Github link to website + portfolio


### Github Pages

1. x

### Project Profile
  
###### Github UI
  - description
    - website
    - tags
  - link to live version
  - Pages site

###### README
- OBS of working -> save as gif/webp
- Code screenshots
  - codemirror, sparkup
- feature list
- badges

