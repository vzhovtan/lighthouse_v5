from pymongo import MongoClient
import json

clientv4 = MongoClient()
mydb4 = clientv4["task_lighthouse_v41_backend"]

#Getting all document from MongoDB collection and saving on disk as JSON file
redis_value = {}
redis_data = []
result_list = []
collection_list = []
restricted_item_admin = ["admin", "webexbot", "event", "commander"]

for collection_name in mydb4.collection_names():
        collection_list.append(collection_name.lower())
result_list = [collection for collection in collection_list if all(item not in collection \
                                                                   for item in restricted_item_admin)]

print(result_list)

for collection in result_list:
    current_collection = mydb4[collection]
    for doc in current_collection.find():
        current_redis_key = collection + "@" + doc.get("platform").replace(" ", "-") + "@" + \
                            doc.get("component").replace(" ", "-") + "@" + doc.get("release").replace(" ", "-")
        redis_value["commands"] = doc.get("commands")
        redis_value["links"] = doc.get("links")
        current_redis_value = json.dumps(redis_value)
        current_redis_data = [current_redis_key, current_redis_value]
        redis_data.append(current_redis_data)

with open("lhv4db.json", "w") as file:
    file.write(json.dumps(redis_data))
