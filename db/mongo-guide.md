https://www.w3schools.com/nodejs/nodejs_mongodb.asp


https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/    const uid = req.session.userId;
    const user = await em.findOne(User, { id: uid });
    return user;
}
```