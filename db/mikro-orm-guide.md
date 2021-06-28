
# Mikro-orm 

<a name="table-of-contents"/>

##### Table of Contents
- [**Setup Checklist**](#setup-checklist)
- [**Creating Posts**](#creating-posts)
- [**Insert Posts**](#insert-posts)
- [**CLI**](#cli)
- [**Migrations**](#migrations)


<a name="setup-checklist"/>

## Setup Checklist

1. install

```bash
npm install @mikro-orm/cli @mikro-orm/core @mikro-orm/migrations @mikro-orm/postgresql pg
```
```JavaScript
const main = async () => {
    const orm = await MikroORM.init({
        dbName: "${DB_NAME}",
        user : "${USERNAME}",
        password : "${PASSWORD}",
        type: "postgresql",
        debug: !__prod__,
    });
};

main();
```

2. create constants file

```bash
touch src/constants.ts
vim !:!
```

3. export const that is true if in production environment 

```typescript
export const __prod__ = process.env.NODE_ENV === "production"
```

4. import const and set debug property of MikrOrm instance as that reference  

```typescript
import { __prod__ } from "./constants";
```

5. define entities [(defining entities w/ mikrorm)](https://mikro-orm.io/docs/defining-entities)

6. make entities folder and file for Post entity

```bash
mkdir src/entities
touch !:!/Post.ts
```

7. entities property of MikroOrm instance


```typescript
import { Post } from "./entities/Post";

    const orm = await MikroORM.init({
        entities: "[POST]",
```

<a name="create-entity"/>

8. Declare entity in ./entities/Post.ts

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




<a name="creating-posts"/>

## Creating Posts

`./index.ts`

```typescript
// em = entitiy manager
// create(EntityName, Data-Obj)
const post = orm.em.create(Post, {})
```



<a name="insert-posts"/>


## Insert Posts into DB

```typescript
// Persists your entity immediately, flushing all not yet persisted changes to 
// the database too. Equivalent to em.persist(e).flush().
orm.em.persistAndFlush(post);
```


<a name="cli"/>


## Mikro-orm CLI



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


<a name="migrations"/>


## Migrations

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

###### Create script to automate migration creation

```json
    "create:migration" : "mikro-orm migration:create"
```