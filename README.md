Hit the hosted url (`https://inlinefragmentstrawberry-production.up.railway.app/graphql`) with a header: `{"User": "1"}` to return a user. Full query is:

```graphql
query UserInline {
  user {
    ...on User {
      id
      name
    }
    ...on Missing {
      message
    }
    __typename
  }
}
```

Headers
```json
{
  "User": "1"
}
```

Response
```json
{
  "data": {
    "user": {
      "id": "1",
      "name": "Patrick Star",
      "__typename": "User"
    }
  }
}
```

vs

```json
{
  "data": {
    "user": {
      "message": "User not found",
      "__typename": "Missing"
    }
  }
}
```