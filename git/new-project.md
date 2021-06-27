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

[Guide - Creating a psql DB](https://www.postgresql.org/docs/7.4/tutorial-createdb.html)

[createdb docs](https://www.postgresql.org/docs/9.1/app-createdb.html)


```bash
# install
apt-get update
apt-get install postgresql

# create user
sudo -u postgres createuser --interactive -P $USERNAME
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) y
Shall the new role be allowed to create more new roles? (y/n) n

#create db
sudo -u postgres createdb -O $USERNAME $DB_NAME
sudo -u postgres psql -U $USERNAME -h 127.0.0.1 $DB_NAME
# terminal 3 (psql -u $USERNAME) postgres database
```



**Mikro-orm**

```bash
npm install @mikro-orm/cli @mikro-orm/core @mikro-orm/migrations @mikro-orm/postgresql pg
```
```JavaScript
const main = async () => {
    const orm = await MikroORM.init({
        dbName: "binder",
        user : "${USERNAME}",
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
import { Post } from "./entities/Post";

    const orm = await MikroORM.init({
        entities: "[POST]",
```

./entities/Post

```javascript
import { Entity, PrimaryKey, Property } from "@mikro-orm/core";

/*
 * Entity decorator : db table
 * Property decorator : column in table
 *  if you delete the property decorator, it would just a normal field in the object.
 * 
 * createAt, updatedAt and title! are good fields to always include. 
 */

@Entity()
export class Post {
    @PrimaryKey()
    id!: number;

    @Property({type: "date"})
    createdAt = new Date();

    @Property({ type: "date", onUpdate: () => new Date() })
    updatedAt = new Date();

    @Property({ type: "text" })
    title!: string;
}
```

**Creating Posts**

./index.ts

```javascript
// em = entitiy manager
// create(EntityName, Data-Obj)
const post = orm.em.create(Post, {})
```
**Insert Posts into DB**

```javascript
// Persists your entity immediately, flushing all not yet persisted changes to 
// the database too. Equivalent to em.persist(e).flush().
orm.em.persistAndFlush(post);
```

[**setting up the mikrorm cli**](https://mikro-orm.io/docs/installation/#setting-up-the-commandline-tool)

```bash
npx mikro-orm
```
```javascript
// ./package.json
// indicate locatino of config for ts
{
  "dependencies": { ... },
  "mikro-orm": {
    "useTsNode": true,
    "configPaths": [
      "./src/mikro-orm.config.ts",
      "./dist/mikro-orm.config.js"
    ]
  }
}
```

```bash
touch ./src/mikro-orm.config.ts
vim !:1
```

```javascript
import { __prod__ } from "./constants";
import { Post } from "./entities/Post";
import { MikroORM } from "@mikro-orm/core";

export default {
    entities : [Post],
    dbName: "binder",
    user : "postgres",
    password : "postgres",
    type: "postgresql",
    debug: !__prod__,        
} as Parameters<typeof MikroORM.init>[0];
```

```javascript
// ./index.ts
import microConfig from "./mikro-orm.config";

    const orm = await MikroORM.init(microConfig);
```

**Migrations**

[mikro-orm migrations configuration](https://mikro-orm.io/docs/migrations/#configuration)

```javascript
// ./mikro-orm.config.ts
import path from "path";

export default {
  migrations: {
    path: path.join(__dirname, "./migrations"), // path to the folder with migrations
    pattern: /^[\w-]+\d+\.[tj]s$/, // regex pattern for the js or ts migration files
  },
```

```bash
npx mikro-orm migration:create        # creates migrations folder -> 
                                      # the sql used to create the table is in that folder
```

```javascript
// ./index.ts
// Run migrations before doing anything else.
const main = async () => {
    const orm = await MikroORM.init(microConfig);
    await orm.getMigrator().up();
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

