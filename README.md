## Lighthouse V5

Lighthouse is internal project and uses data saved in MongoDB 
Lighthouse is developed by engineers to engineers providing common resource of useful commands and support links to help in troubleshooting.
V5 started to modify frontend and use React and modify backend to use Redis as cache, split function among containers and run the app on K8S infra.

* lhv4db.json
is complete Lighthouse V4 DB taken from MongoDB, converted to redis-like format and saved in JSON format

Python files are for starting Redis, taking the local file "lhv4db.json" and start backend service for API.
There is no front-end yet, all testing is done with Postman
