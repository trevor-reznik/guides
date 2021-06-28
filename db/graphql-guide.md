
# GraphQL

<a name="table-of-contents"/>


##### Table of Contents
- [**Setup**](#setup)
    - [Build Schema](#build-schema)
    - [Create Resolvers](#create-resolvers)
    - [Pass Middleware](#pass-middleware)
    - [Entity Type](#entity-type)
    - [Field Types](#field-types)
    - [Apollo Context](#apollo-context)
- [**Create**](#create)
- [**Read**](#read)
- [**Update**](#update)
- [**Delete**](#delete)



<a name="setup"/>


## Setup with ApolloServer

1. install

```bash
npm install graphql type-graphql
npm install apollo-server-express
npm install reflect-metadata
```

2. import

```typescript
import "reflect-metadata";
import { ApolloServer } from "apollo-server-express"
import { buildSchema } from "type-graphql"
```


<a name="build-schema"/>

3. build schema

```typescript
const apolloServer = new ApolloServer({
  schema: await buildSchema()
});
```

<a name="create-resolvers"/>

4. create resolvers folder & file

```bash
mkdir src/resolvers
touch !:1/$(RESOLVER_NAME).ts
```
5. create Resolver and Query

```typescript
// $RESOLVER_NAME.ts
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

5. add options arg to buildSchema() and pass Resolver

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


<a name="pass-middleware"/>

6. create graphql endpoint by passing express middleware

```typescript
apolloServer.applyMiddleware({ app });
```

7. Enter graphql playground to test queries and mutations

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

<a name="entity-type"/>

8. Set entity type with decorator

```typescript
// entities/entity.ts
import { ObjectType } from "type-graphql";

@ObjectType()
@Entity()
export class Post { ... }
```

<a name="field-types"/>

9. Set field types

```typescript
// entities/entity.ts
import { Field, Int } from "type-graphql";

@ObjectType()
@Entity()
export class Post {
    
    @Field(() => Int)
    @PrimaryKey()
    id!: number;

    @Field(() => String)
    @Property({ type: "date", onUpdate: () => new Date() })
    updatedAt = new Date();

    @Field(() => String)
    @Property({ type: "text" })
    title!: string;
}
```


<a name="apollo-context"/>


10. assign resolver name to ApolloServer instance's resolvers property
11. use context obj of ApolloServer instance to make orm accessible to resolvers so they can access db

```typescript
import { PostResolver } from "./resolvers/post";

// context: obj accessible by all resolvers, function that returns object for context. 
//          Can also get req and res from Express
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


12. access context in query

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

13. create and export a type for context in a types file

```bash
touch src/resolvers/types.ts
vim !:1
```

```typescript
export type MyContext {
  em: ...  
}
```

14. hover over the context's value/obj to see type and then export that as context type

```typescript
import { EntityManager, IDatabaseDriver, Connection } from "@mikro-orm/core";

export type MyContext = {
    em: EntityManager<IDatabaseDriver<Connection>>
}
```

14. Import context type

```typescript
// resolvers/post.ts
import { MyContext } from "./types";
```


15. access em (entity manager obj of mikro-orm) in query method through ctx
16. use em access posts and return promise of posts

```typescript
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
17. Destructure ctx
18. Explicitly set type of posts return obj so resolver also has type checking

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


19. test: open graphql playground

```bash
npm run dev
npm run watch
xdg-open http://localhost:4000/graphql
```

20. send query

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
  },
  ...
}
```






<a name="read"/>

## Read


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





<a name="create"/>

## Create


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




<a name="update"/>

## Update


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





<a name="delete"/>

## Delete



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


<a name="input-classes"/>


## Input Classes


1. create input class
2. decorate with @InputType()
3. decoreate fields with @Field()


```typescript
@InputType()
class UsernamePasswordInput {
  @Field()
  username: string
  @Field()
  password: string
}
```

4. pass class to @Arg decorate in mutation method

```typescript
@Resolver()
export class UserResolver {
  @Mutation(() => String)
  register(
    @Arg("options", () => UsernamePasswordInput ) options: UsernamePasswordInput
  ); {
    options.password = ...
    options.username = ...
  }
}
```



<a name="hashed-passwords"/>

https://youtu.be/I6ypD7qv3Z8?t=4765
