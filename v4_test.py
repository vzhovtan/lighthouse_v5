from pymongo import MongoClient

clientv4 = MongoClient(
    'mongodb://lighthouse_v41_backend:a958935c0a9a9d21709711cacf2374dfea743d5e@bdb-user-alln-2.cisco.com:27000/?authSource'
    '=task_lighthouse_v41_backend&authMechanism=MONGODB-CR')
mydb4 = clientv4["task_lighthouse_v41_backend"]

"""
dbass in BDB the same as mydb4 i this script
"""

"""
Getting collection list with exception for restricted items
"""

restricted_item = ["admin", "webexbot", "event", "commander"]
collection_list = []
result_list = []

for collection_name in mydb4.collection_names():
    collection_list.append(collection_name.lower())

result_list = [collection for collection in collection_list if all(item not in collection for item in restricted_item)]
result_list.sort()
print(result_list)

"""
Testing of V4 connection by taking one document
"""

# collection4 = mydb4["ios-xr"]
# dbaas_dict = {"platform": "asr9k", "release": "6.5", "component": "interfaces"}
# doc = collection4.find_one(dbaas_dict)
# raw_content = []
# raw_content.append(doc.get("commands"))
# raw_content.append(doc.get("links"))
# for item in raw_content:
#     print(item)

"""
Getting raw content for one combination collection/platform/component/release
"""

# command_db = []
# db_dict = {"platform": "ncs5500", "component": "interfaces", "release": "6.5"}
# doc = mydb4["ios-xr"].find_one(db_dict)
# if doc:
#     command_db = doc.get("commands", "")
# else:
#     command_db = ["no current data"]
#
# print(command_db)

"""
Searching document for "release independent" release in one collection
"""

# db_dict = {"release": "release indepedent"}
# doc = mydb4["ios-xr"].find(db_dict)
# for item in doc:
#     print(item)

"""
Getting all document from collection
"""

# raw_content = []
# platform_list = []
#
# collection4 = mydb4["ios-xr"]
# for doc in collection4.find():
#     item_dict = {}
#     item_dict["platform"] = doc.get("platform")
#     item_dict["component"] = doc.get("component")
#     item_dict["release"] = doc.get("release")
#     item_dict["commands"] = doc.get("commands")
#     item_dict["links"] = doc.get("links")
#     raw_content.append(item_dict)
#
# for item in raw_content:
#     if item["platform"].lower() not in platform_list:
#         platform_list.append(item["platform"].lower())
#
# for i in range(0,3):
#     print(raw_content[i])
# print(len(raw_content))
# print(platform_list)

"""
User status verification
"""

# user_name = "vzhovtan"
#
# user_admin_status = False
# admin_names = mydb4['admin_list'].find_one()["admin"]
# if user_name in admin_names:
#     user_admin_status = True
#
# print (user_admin_status)

"""
Deleting one document
"""

# mycol = mydb4["ios-xr"]
# dbaas_dict = {"platform": "ncs5500", "release": "test", "component": "test"}
# update = mycol.delete_one(dbaas_dict)
# print(update.deleted_count)


"""
Taking collection list with filtering
"""

# restricted_user_list = ["admin", "webexbot", "event", "commander"]
# restricted_admin_list = ["admin", "webexbot", "draft", "event", "commander"]
#
# admin_list = []
# user_list = []
# collection_list = []
#
# for collection_name in mydb4.collection_names():
#     collection_list.append(collection_name.lower())
#
# admin_list = [collection for collection in collection_list if all(item not in collection for item in restricted_admin_list)]
# admin_list.sort()
#
# user_list = [collection for collection in collection_list if all(item not in collection for item in restricted_user_list)]
# user_list.sort()
#
# print(admin_list)
# print(user_list)


"""
Submitting one document and getting it back
"""
# submitted_doc = {}
# commands = ["111", "222", "333", "444", "555"]
# links = ["111@222", "222@333", "333@444", "444@555", "555@666"]
# userid = "test_user"
#
# db_dict = {"platform": "ncs5500", "component": "test", "release": "test"}
#
# submitted_doc["platform"], submitted_doc["component"], submitted_doc["release"], submitted_doc["commands"], submitted_doc["links"], submitted_doc["submitter"] = \
#     "ncs5500", "test", "test", commands, links, userid
#
# result = mydb4["ios-xr-draft"].insert_one(submitted_doc)
# print(type(str(result.inserted_id)))
#
# doc = mydb4["ios-xr-draft"].find_one(db_dict)
# if doc:
#     print(doc.get("commands", ""))
#     print(type(doc.get("commands", "")))
#     print(doc.get("links", ""))
#     print(type(doc.get("links", "")))
#     print(doc.get("submitter", ""))






