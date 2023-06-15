# Serverless Link Shortener (Network, Compute, Serverless)

You are approached by some desperate web developers, Alice & Bob. They created a url shortening service "shorty", which became very popular, however they build everything using a monolithic architecture on a single machine. He doesn't want to run into scaling issues anymore and asked you, if you could help him, redesigning his application to a serverless application.

The main part of the application is the website. Here you can enter a long url und you get a short url, that should be stored for 1 week. In this week, requests to this short URL should be redirected to the original long url. They are also interested in having some basic statistics.

Their website uses __only client side rendering__ and all backend requests should be made via the API.


Principle

```                                
    shorty.com/x1u2dTs   ──►  short url service  ──► HTTP 308 REDIRECT to aws.amazon.com/ec2
                ▲
                │
                └───────  "n"  Digits, Upper- or Lowercase characters

```


## Tasks
1. Whats a reasonable choice for the short url length `n`?
2. Serverless Architecture, that can scale up & down to demand.
3. Pick a database and outline how the tables should/could look like
4. Describe how the web application can be hosted effectively.


## Part 2:
He now also plans to add authentication to the project: A user should be able to log-in and only then be able to make modifications to the short urls. Every user should only be able to change his/her own short urls.

Please prepare a proposal for the API and the architecture that they might use. Do you know a tool/service to make user authentication easier?

Example: 

| PATH                            | METHOD | Description                                            |
| ------------------------------- | ------ | ------------------------------------------------------ |
| `/v1/shorturls/{short-url-id} ` | GET    | retrieves the current configuration for {short-url-id} |
| `/v1/shorturls/{short-url-id} ` | PUT    | creates a new short url entry  {short-url-id}          |
| `/v1/shorturls/{short-url-id} ` | DELETE | deletes the current configuration {short-url-id}       |
| `/v1/shorturls/{short-url-id} ` | POST   | updates the short url configuration {short-url-id}     |
| `/v1/users/{user-id}          ` | GET    | retrieves the data about the user                      |
| `/v1/users/{user-id}/shorturls` | GET    | retrieves all short urls of the user                   |

After the proposal, try to implement this in AWS.

_Hint_: Use an API Gateway and create an HTTP API. 