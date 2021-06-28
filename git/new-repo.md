# New Empty Repo


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

```typescript
export const __prod__ = process.env.NODE_ENV === "production"
```

```typescript
import { __prod__ } from "./constants";
```

[defining entities w/ mikrorm](https://mikro-orm.io/docs/defining-entities)

```bash
mkdir src/entities
touch !:!/Post.ts
```

```typescript
import { Post } from "./entities/Post";

    const orm = await MikroORM.init({
        entities: "[POST]",
```

./entities/Post

```typescript
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

```typescript
// em = entitiy manager
// create(EntityName, Data-Obj)
const post = orm.em.create(Post, {})
```
**Insert Posts into DB**

```typescript
// Persists your entity immediately, flushing all not yet persisted changes to 
// the database too. Equivalent to em.persist(e).flush().
orm.em.persistAndFlush(post);
```

[**setting up the mikrorm cli**](https://mikro-orm.io/docs/installation/#setting-up-the-commandline-tool)

```bash
npx mikro-orm
```
```typescript
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

```typescript
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

```typescript
// ./index.ts
import microConfig from "./mikro-orm.config";

    const orm = await MikroORM.init(microConfig);
```

**Migrations**

[mikro-orm migrations configuration](https://mikro-orm.io/docs/migrations/#configuration)

```typescript
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

```typescript
// ./index.ts
// Run migrations before doing anything else.
const main = async () => {
    const orm = await MikroORM.init(microConfig);
    await orm.getMigrator().up();
```

**Express**

```bash
npm install express  
npm install @types/express
```

```typescript
import express from "express"

const app = express();
app.get("/", (req, res) => {

})

app.listen(4000, () => {

});
```

**Graphql Schemas & Apollo Server**

```bash
npm install graphql type-graphql
npm install apollo-server-express
npm install reflect-metadata
```

```typescript
import "reflect-metadata";
import { ApolloServer } from "apollo-server-express"
import { buildSchema } from "type-graphql"

const apolloServer = new ApolloServer({
  schema: await buildSchema()
});
```

```bash
mkdir src/resolvers
touch !:1/hello.ts
```
Add graphql Query

```typescript
// hello.ts
import { Resolver, Query } from "type-graphql";


// Add functions that will be either mutations or queries
@Resolver()
export class HelloResolver {
    // Declare what query returns
    @Query(() => String)
    hello() {
        return "hello world"
    }
};
```

Add options arg to buildSchema()

```typescript
import { HelloResolver } from "./resolvers/hello";

const app = express();
const apolloServer = new ApolloServer({
  schema: await buildSchema({
    resolvers : [HelloResolver],
    validate: false
  })
});
```

Create graphql endpoint by passing express middleware

```typescript
apolloServer.applyMiddleware({ app });
```

Enter graphql playground devtool to test queries and mutations

```bash
xdg-open http://localhost:4000/graphql
```

```sql
# query:
{
  hello
}

# res:
{
  "data": {
    "hello": "hello world"
  }
}
```

- Set entity type with decorators
- Set field types with decorators

```typescript
// entities/entity.ts
import { Entity, PrimaryKey, Property } from "@mikro-orm/core";
import { Field, Int, ObjectType } from "type-graphql";

@ObjectType()
@Entity()
export class Post {
    
    @Field(() => Int)
    @PrimaryKey()
    id!: number;

    @Field(() => String)
    @Property({type: "date"})
    createdAt = new Date();

    @Field(() => String)
    @Property({ type: "date", onUpdate: () => new Date() })
    updatedAt = new Date();

    @Field(() => String)
    @Property({ type: "text" })
    title!: string;
}
```

<a name="apollo-context"/>

*Context object* 
- Add the resolver to resolvers property in schema
- use context obj of ApolloServer obj to make orm accessible to resolvers so they can access db
  - context: obj accessible by all resolvers, function that returns object for context. Can also get req and res from Express


```typescript
import { PostResolver } from "./resolvers/post";

const main = async () => {
    const orm = await MikroORM.init(microConfig);
    await orm.getMigrator().up();
    
    const app = express();
    const apolloServer = new ApolloServer({
      schema: await buildSchema({
        resolvers : [HelloResolver, PostResolver],
        validate: false
      }),
      context: () => ({ em: orm.em })
    });
```

<a name="mikroorm-crud"/>

**CRUD with Mikro-orm:** *Create CRUD Resolvers*


```typescript
// resolvers/post.ts
import { Post } from "../entities/Post";
import { Resolver, Query, Ctx } from "type-graphql";


@Resolver()
export class PostResolver {
    @Query(() => [Post])
    posts(
        @Ctx() ctx: MyContext
    ) {
        return ...
    }
};
```
- Create what the context type will be
- Create a types file to export the type of the ApolloServer.context object

```bash
touch src/resolvers/types.ts
```

```typescript
export type MyContext {
  em: 
}
```

- Hover over the context's value/obj to see type and then export that as context type


```typescript
import { EntityManager, IDatabaseDriver, Connection } from "@mikro-orm/core";

export type MyContext = {
    em: EntityManager<IDatabaseDriver<Connection>>
}
```

<a name="crud-read"/>

*Add Query:* **Read**

- Import context type
- access em through ctx
- use em (entity mamanger) of mikro-orm to access posts and return promise of posts


```typescript
// resolvers/post.ts
import { MyContext } from "./types";

@Resolver()
export class PostResolver {
    @Query(() => [Post])
    posts(
        @Ctx() ctx: MyContext
    ) {
        return ctx.em.find(Post, {});
    }
};
```
- Destructure ctx
- Explicitly set type of posts return obj so resolver also has type checking

```typescript
@Resolver()
export class PostResolver {
    @Query(() => [Post])
    posts(
        @Ctx() { em }: MyContext): Promise<Post[]> {
        return em.find(Post, {});
    }
};
```

```bash
npm run dev
npm run watch
xdg-open http://localhost:4000/graphql
```

```sql
# query
{
  posts {
    id
    createdAt
    updatedAt
    title
  }
}

# res
{
  "data": {
    "posts": [
      {
        "id": 1,
        "createdAt": "1624754629000",
        "updatedAt": "1624754629000",
        "title": "my first post"
      }
  }
}
```

**Read**: *single param query*

- Add new query with an arg
- Update types

```javascript
  // Update return type. by passing positional options object and setting nullable property to true  
  // Post no longer iterable
  @Query(() => Post, { nullable: true })
  post(
    // @Arg         for typegraphql (name of arg, type)
    // Int          graphql type
    // id: number   set ts type
    @Arg("id", () => Int) id: number, 
    @Ctx() { em }: MyContext
    // Update Promise type to be Post or null   
  ): Promise<Post | null> {
    // findOne method to find single
    return em.findOne(Post, { id });
  }
```

```sql
# query 
{
  post(id:1) {
    title
    createdAt
  }
}

# res
{
  "data": {
    "post": {
      "title": "my first post",
      "createdAt": "1624754629000"
    }
  }
}
```



*Add Mutations:* **create**

```typescript
  // Can still return a post from creating a post
  // Never return null from creating a post so remove from type
  @Mutation(() => Post)

  // Name mutation obj, use async and await
  async createPost(

    // Create args
    //    First arg in Arg() determines key in graphql
    // Set type for the arg in graphql:
    //    () => String
    // Set the type for ts
    //    title: string,
    @Arg("title", () => String) title: string,
    // for optional arg:
    //    () => String, { nullable: true }

    @Ctx() { em }: MyContext

    // Update Promise type
  ): Promise<Post> {
    // Use same logic as before
    //    access entity manager object of mikro-orm obj
    //        declare post with create method
    //        persist and flush
    const post = em.create(Post, {title});
    await em.persistAndFlush(post);
    
    return post
  }
```

```sql
# mutation

# graphql splits queries and mutations
mutation {
  createPost(title: "hello world") {
    id
    createdAt
  }
}

# res
{
  "data": {
    "createPost": {
      "id": 15,
      "createdAt": "1624853371001"
    }
  }
}
```

*Add Mutations:* **update**

```typescript
  // May return null -> update type
  @Mutation(() => Post, { nullable: true })
  async updatePost(
    @Arg("id", () => Int) id: number,
    // in graphql type, pass options object with nullable property set to true 
    // (indicating that title is an optional param)
    @Arg("title", () => String, { nullable: true }) title: string,
    @Ctx() { em }: MyContext
  ): Promise<Post | null> {
    // Await post query from entity manager
    const post = await em.findOne(Post, { id });
    if (!post) {
        return null
    }
    // If title arg was passed, update title property of queried post  
    if (typeof title !== "undefined" ) {
        post.title = title;
        await em.persistAndFlush(post);
    }
    return post
  }
```

```sql
# mutation
mutation {
  updatePost(id:1, title:"hi"){
    id
    title
    createdAt
    updatedAt
  }
}

# res
{
  "data": {
    "updatePost": {
      "id": 1,
      "title": "hi",
      "createdAt": "1624754629000",
      "updatedAt": "1624854278123"
    }
  }
}
```

*Add Mutations:* **delete**


```typescript
  @Mutation(() => Boolean)
  async deletePost(
    @Arg("id", () => Int) id: number,
    @Ctx() { em }: MyContext
  ): Promise<boolean> {
    await em.nativeDelete(Post, { id });
    return true;
  }
```

```sql
# mutation
mutation {
  deletePost(id:1)
}

# res
{
  "data": {
    "deletePost": true
  }
}
```









--------------------------

<a name="website"/>

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

