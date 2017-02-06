# shopping-list-api
Api server for Shopping List App

# mongodb user

```
use evedemo
db.createUser(
  {
    user: "user",
   pwd: "user",
    roles: [ { role: "readWrite", db: "evedemo" } ]
  }
 )
```