# Redis

https://www.npmjs.com/package/redis



<a name="setup"/>

## Setup


1. `install`

```bash
sudo apt install redis-server
```

2. start server

```bash
redis-server
```

3. install client for node and express

```bash
npm i redis connect-redis express-session
npm i @types/redis @types/connect-redis
```

4. `import`

```typescript
import redis from "redis";
import session from "express-session";
import connectRedis from "connect-redis";
```

5. init

```typescript
const RedisStore = connectRedis(session);
const redisClient = redis.createClient()

// add to express
app.use(
    session({
        store: new RedisStore({ client: redisClient }),
        secret: "$SECRET",
        resave: false,
    })
)
```


6. put before other middleware that accesses it


```typescript
const app = express();

app.use(
    session({
        name: "$NAME",
        store: new RedisStore({ client: redisClient }),
        secret: "$SECRET",
        resave: false,
    })
)

applyMiddleware({ app });
```


7. add options

```typescript
    session({
      name: "qid",
      store: new RedisStore({ 
        client: redisClient,
        disableTouch: true|false,
        disableTTL: true|false
      }),
```

8. add cookie property and options

```typescript
    session({
      name: "qid",
      cookie: {
        domain:
        encode:
        httpOnly:
        maxAge:
        path:
        sameSite:
        secure:
        signed:
      }
```

9. access session from inside Resolvers by passing in Express' `req` and `res` objects into ApolloServer's context object

```typescript
  const apolloServer = new ApolloServer({
    schema: await buildSchema({
      resolvers: [ResolverName]
    }),
    // returns context of MyContext defined type
    context: ({req, res}): MyContext => ({ em: orm.em, req, res }), 
  });
```

10. update context's type

```typescript
// types.ts
import { Session, SessionData } from "express-session";
import { Request, Response } from "express";
export type MyContext = {
    em: EntityManager<IDatabaseDriver<Connection>>;
    // & sign to join types together
    // add type for a userId property
    req: Request & {session: Session & Partial<SessionData> & {userId?: number}};
    res: Response 
};
```

11. access `req` and `res` objects in Resolver(s)

```typescript
// resolverName.ts
  @Mutation(() => returnObjName)
  async func(
    @Ctx() { em, req }: MyContext
  ): Promise<returnObjName> {
      req.method()
  };
```

12. use `req` objects' `session` property to store kv data that you defined types for

```typescript
  ): Promise<returnObjName> {
      req.session.userId = user.id;
  };
```

13. test

`localhost:port/graphql` -> `Settings` -> `"request.credentials": "include"` ->

`browser IDE` -> `Application`-> `Cookies` -> `Clear` -> 

```sql
mutation {
    testMutation(options: option){
        res
    }
}
```

14. add `me()` query to test if logged in

```typescript
@Resolver()
export class UserResolver {
  @Query(() => User, { nullable: true })
  async me(@Ctx() { req, em }: MyContext) {
    if (!req.session.userId) {
      return null;
    }
    const uid = req.session.userId;
    const user = await em.findOne(User, { id: uid });
    return user;
}
```


15.