### Lighthouse V5

V5 has been created to improve the performance of V4. It doesn't use BDB anymore and utilize Redis as key-value store for the DB.

Main DB file is:

* `lhv4db.json` 

which is complete Lighthouse V4 DB taken from MongoDB, converted to redis-like format and saved in JSON format.

Python apps are starting Redis, taking the local file `lhv4db.json` and starting backend service for API. There is no front-end, all testing is done with Postman.

Future development is undefined.
