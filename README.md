# shopping-list-api [![Build Status](https://travis-ci.com/Rassilion/shopping-list-api.svg?token=m4KidMr2FheLLF9fF3q5&branch=master)](https://travis-ci.com/Rassilion/shopping-list-api)
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