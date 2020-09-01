from pymongo import MongoClient
import json
import redis3

#Connections definition
r = redis3.Redis(host='127.0.0.1', port=6379)

clientv4 = MongoClient(
    'mongodb://lighthouse_v41_backend:a958935c0a9a9d21709711cacf2374dfea743d5e@bdb-user-alln-2.cisco.com:27000/?authSource'
    '=task_lighthouse_v41_backend&authMechanism=MONGODB-CR')
mydb4 = clientv4["task_lighthouse_v41_backend"]

#Getting all document from MongoDB collection and creating redis DB
redis_value = {}
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
        r.set(current_redis_key, current_redis_value)
        value = r.get(current_redis_key)

#Test variables
# plat = "asr9k"
# comp = "dhcp-proxy"
# rel = "release-independent"

#Getting platform, component and release sets
# platform_list = []
# component_list = []
# release_list = []

#platform list
# for key in r.keys():
#     platform = key.decode("utf-8").split("@")[1]
#     platform_list.append(platform)
#
# platform_set = set(platform_list)
# print(platform_set)

#component list
# for key in r.keys():
#     platform = key.decode("utf-8").split("@")[1]
#     component = key.decode("utf-8").split("@")[2]
#     if platform == plat:
#         component_list.append(component)
#
# component_set = set(component_list)
# print(component_set)

#release list
# for key in r.keys():
#     platform = key.decode("utf-8").split("@")[1]
#     component = key.decode("utf-8").split("@")[2]
#     release = key.decode("utf-8").split("@")[3]
#     if platform == plat and component == comp:
#         release_list.append(release)
#
# release_set = set(release_list)
# print(release_set)

#Getting data entry for specific platform+component+release combination
# requested_key = "ios-xr@" +plat + "@" + comp + "@" + rel
# requested_value = r.get(requested_key)
# requested_data = json.loads(requested_value)
# print(requested_key)
# print(requested_data)
