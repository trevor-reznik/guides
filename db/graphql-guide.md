# GraphQL

 https://graphql.org/

 https://www.howtographql.com/


GraphQL the query language doesn't know about resolvers, it's just a query language. You write GraphQL queries, you ask for fields, all is well.

When you come to write a GraphQL server, you need to respond to queries. That means, you need to fetch your data from somewhere, and prepare it to be sent back in the response from the GraphQL server. This is what the resolvers are for. You make a resolver for each data type, and make resolver functions to resolve the fields on that type. Typically you only need to write resolver functions for fields that need to be computed (e.g. if you need to calculate a value, or go fetch some data from an API / database). That might not make sense just yet, but come back to that after you've read the rest of this.

I'm not sure, but your confusion here might be coming from you expecting GraphQL to be just one thing, like MySQL or Postgres or something - it's not. You make a GraphQL server, and you choose how to implement the data-fetching logic.

Let's say you have a basic blog, and you're writing a GraphQL server that you'll call to fetch the data. Let's keep it simple and say there are 2 data types, Post and Person. A Post has an author, which is a Person.

For that, your schema might look something like this:

```
graphql type Query { post(id: ID!): Post }

type Post { id: ID! title: String! author: Person! content: String! }

type Person { id: ID! name: String! }
```

So you can fetch a specific Post using the root Query type. And on a Post you can fetch the author (a Person).

Resolver functions are what you use to say "when someone asks for this field, on this type, this is the data that will be returned". So you'll have a resolver for your root query type, and you'll have a resolver function for that post field (post(id: ID!): Post above). That resolver function will return a Post. So maybe it'll go off to some API or your database and go and fetch that post by ID.

Now, when the GraphQL server gets that Post back, it's data might not look like your schema above. The author might just be an ID in your database, so you'd also make a resolver for your Post type, and add a resolver function for the author field. This can then use the post data you got back from the database and go fetch the author by ID. (This links back to what I was saying earlier, you shouldn't need to write resolver functions for the other fields if they're returned as-is and the field names are the same as in your schema).

Resolver functions are only executed if needed too. So if someone executed a query and they wanted the post but didn't ask for the author, then the author resolver wouldn't be executed.

If you still don't get it, you should just try to make a GraphQL server. There are plenty of beginner tutorials. I'm pretty confident that if you just make a basic server and play around with i

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

1. `install`

```bash
npm install graphql type-graphql
npm install apollo-server-express
npm install reflect-metadata
```

2. `import`

```typescript
import "reflect-metadata";
import { ApolloServer } from "apollo-server-express";
import { buildSchema } from "type-graphql";
```

<a name="build-schema"/>

3. build schema

```typescript
const apolloServer = new ApolloServer({
  schema: await buildSchema(),
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
    return "hello world";
  }
}
```

5. add options arg to `buildSchema()` and pass Resolver

```typescript
import { HelloResolver } from "./resolvers/hello";

const app = express();
const apolloServer = new ApolloServer({
  schema: await buildSchema({
    resolvers: [HelloResolver],
    validate: false,
  }),
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

10. assign resolver name to `ApolloServer` instance's `resolvers` property
11. use `context` obj of `ApolloServer` instance to make orm accessible to resolvers so they can access db

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
  em: EntityManager<IDatabaseDriver<Connection>>;
};
```

14. Import context type

```typescript
// resolvers/post.ts
import { MyContext } from "./types";
```

15. access `em` (entity manager obj of mikro-orm) in query method through `ctx`
16. use `em` access `Post`s and return `Promise` of posts

```typescript
@Resolver()
export class PostResolver {
  @Query(() => [Post])
  posts(@Ctx() ctx: MyContext) {
    return ctx.em.find(Post, {});
  }
}
```

17. Destructure ctx
18. Explicitly set type of posts return obj so resolver also has type checking

```typescript
@Resolver()
export class PostResolver {
  @Query(() => [Post])
  posts(@Ctx() { em }: MyContext): Promise<Post[]> {
    return em.find(Post, {});
  }
}
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
2. decorate with `@InputType()`
3. decoreate fields with `@Field()`

```typescript
@InputType()
class UsernamePasswordInput {
  @Field()
  username: string;
  @Field()
  password: string;
}
```

4. pass class to `@Arg` decorate in mutation method

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

<a name="credentials"/>

## Credentials

.

.

<a name="hashed-passwords"/>

#### Password Hashing

https://youtu.be/I6ypD7qv3Z8?t=4765

<a name="resolver-error-handling"/>

## Resolver Error Handling Options

#### using mikro-orm entity manager `em`

```typescript
(em.findOrFail(Entity, { data }) > false) | object;
```

#### creating custom `Error` classes

1. decorate Error class with grapql's `ObjectType()`

```typescript
// can return ObjectType() in mutations/queries, use InputType() for inputs
  @ObjectType()
  class FieldError {
```

2. decorate fields
2. include property which indicates which field caused the error
2. include property that relays error msg in human-readable

```typescript
    @Field
    field: string;
    @Field
    message: string;
  }
```

5. Update mutation return type

```typescript
  @Mutation(() => mutationNameResponse || ErrorName )
```

6. return `FieldError` on error condition

```typescript
  async fname(
    @Ctx() { em }: MyContext
  ) {
    if (!condition) {
      return {
        errors: [{
          field: "fieldName",
          message: "error message to user"
        }]
      }
    };
  }
```

#### creating dynamic return object

1. use `@Field` decorator for kv
2. use `?` after variable for optional params

```typescript
@ObjectType()
class mutationNameResponse {
  @Field()
  errors?: ErrorName[];

  @Field()
  video?: EntityNameClass;
}
```

3. set graphql type
3. [obj] and obj[] for array types
3. nullable is true for optional param

```typescript
  ... {
    @Field(() => [ErrorName], { nullable: true })
    errors?: ErrorName[];

    @Field(() => EntityNameclass, { nullable: true })
    video?: EntityNameClass;
  }
```

6. update query's return type

```typescript
  @Mutation(() => mutationNameResponse)
```

7. return `ErrorName`, `null` on error condition
8. (return `null`, `resObject` on success)

```typescript
  async fname(
    @Ctx() { em }: MyContext
  ) {
    if (!condition) {
      return {
        errors: [{
          field: "fieldName",
          message: "error message to user"
          },
        ],
        // null
      };
    }
```

8. create other error types


```typescript
    if (!secondCondition) {
      return {
        errors: [{
          field: "field",
          message: "$MESSAGE"
          },
        ],
      };
    }
```

9. return `null`, `mutationNameResponse` on success

```typescript
    if (!secondCondition) {
      return {
        errors: [{
          field: "field",
          message: "$MESSAGE"
          },
        ],
      };
    }
    else {
      return {
        // null,
        mutationNameResponse,
      };
    };
```
###### Example

```typescript
@ObjectType()
class FieldError {
  @Field()
  field: string;
  @Field()
  message: string;
}

@ObjectType()
class UpdateTagRes {
  @Field(() => [FieldError], { nullable: true })
  errors?: FieldError[];
  @Field(() => Video, { nullable: true })
  video?: Video;
}

@Resolver()
export class VideoResolver {
  @Mutation(() => UpdateTagRes)
  async updateCategory(
    @Arg("id", () => Int) id: number,
    @Arg("creator", () => String) creator: string,
    @Ctx() { em }: MyContext
  ) {
    const video = await em.findOne(Video, { id });
    if (!video) {
      return {
        errors: [
          {
            field: "creator",
            message: "creator name invalid",
          },
        ],
      };
    }
    video.creator = creator;
    em.persistAndFlush(video);
    return {
      video,
    };
  }
}
```

#### try catch

```typescript
try {
  foo(bar)
}
catch (err) {
  console.log(err.message)
  return {
    errors [
      {
      field: "field",
      message: "field invalid",
      },
    ]
  }
}
```


```typescript
try {
  foo(bar)
}
catch (err) {
  if ( err.code == "2305" || err.detail.includes("already exists") {
    return {
      errors [
        {
        field: "field",
        message: "field invalid",
        },
      ]
    }
  }
}
```


-----------------

