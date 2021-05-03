import json
import redis3
"""
Redis has to be started on the same localhost with command
docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest
db_to_redis.py file takes the data from local JSON file which contains the entire Lighthouse DB and update Redis
"""


def get_db_data(file_name):
    with open(file_name) as fd:
        data = json.load(fd)

    return data


def update_redis_cache(connection, data):
    for item in data:
        current_redis_key = item[0]
        current_redis_value = json.dumps(item[1])
        connection.set(current_redis_key, current_redis_value)


if __name__ == "__main__":
    db_file = "lhv4db.json"
    redis_connection = redis3.Redis(host='127.0.0.1', port=6379)
    update_redis_cache(redis_connection, get_db_data(db_file))
