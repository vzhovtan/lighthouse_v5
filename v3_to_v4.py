from pymongo import MongoClient

clientv3 = MongoClient(
    'mongodb://lighthouse_v3_backend:cb0c237101941d9fc1c8229206af244047e42a17@bdb-dbaas-alln-1:27000/?authSource'
    '=task_lighthouse_v3_backend&authMechanism=MONGODB-CR')
mydb3 = clientv3["task_lighthouse_v3_backend"]

clientv4 = MongoClient(
    'mongodb://lighthouse_v41_backend:a958935c0a9a9d21709711cacf2374dfea743d5e@bdb-user-alln-2.cisco.com:27000/?authSource'
    '=task_lighthouse_v41_backend&authMechanism=MONGODB-CR')
mydb4 = clientv4["task_lighthouse_v41_backend"]
collection4 = mydb4["mobility"]

#Testing of V3 connection
platform_list = []
feature_list = []
xr_list = []
ios_list = []
cable_list = []
dc_list = []
other_list = []
rfa_list = []

collection3 = mydb3["lighthouse"]
for item in collection3.find():
    if "final" in item['_id']:
        xr_item = {}
        ios_item = {}
        cable_item = {}
        dc_item = {}
        new_item = {}

        platform = item['_id'].split('_')[0]
        if platform not in platform_list:
            platform_list.append(platform)
        feature = item['_id'].split('_')[1]
        if feature not in feature_list:
            feature_list.append(feature)
        commands = item['commands']
        links = item['links']
        if platform == 'ios-xr-pi' or platform == 'ncs5500' or platform == 'crs' or platform == 'asr9k' or platform == 'gsr12k' or platform == 'ncs6000' or platform == '8800':
            xr_item['platform'] = platform
            xr_item['component'] = feature
            xr_item['release'] = 'release independent'
            xr_item['submitter'] = "lighthousev3"
            xr_item['commands'] = commands
            xr_item['links'] = links
            xr_list.append(xr_item)
        elif platform == "7600" or platform == "asr-920":
            ios_item['platform'] = platform
            ios_item['component'] = feature
            ios_item['release'] = 'release independent'
            ios_item['submitter'] = "lighthousev3"
            ios_item['commands'] = commands
            ios_item['links'] = links
            ios_list.append(ios_item)
        elif platform == "ubr10k-cmts" or platform == "rfgw-10" or platform == "cbr-8":
            cable_item['platform'] = platform
            cable_item['component'] = feature
            cable_item['release'] = 'release independent'
            cable_item['submitter'] = "lighthousev3"
            cable_item['commands'] = commands
            cable_item['links'] = links
            cable_list.append(cable_item)
        elif platform == "aci":
            dc_item['platform'] = platform
            dc_item['component'] = feature
            dc_item['release'] = 'release independent'
            dc_item['submitter'] = "lighthousev3"
            dc_item['commands'] = commands
            dc_item['links'] = links
            dc_list.append(dc_item)
        else:
            new_item['platform'] = platform
            new_item['component'] = feature
            new_item['release'] = 'release independent'
            new_item['submitter'] = "lighthousev3"
            new_item['commands'] = commands
            new_item['links'] = links
            other_list.append(new_item)
    else:
        rfa_list.append(item)

# print("Platform list")
# print(platform_list)
# print("Feature list")
# print(feature_list)
# print("RfA list")
# print(rfa_to_approve)

# for item in xr_list:
#     print(item)
#     new_doc = collection4.insert_one(item)
#     print(new_doc.acknowledged)

# for item in ios_list:
#     print(item)
#     new_doc = collection4.insert_one(item)
#     print(new_doc.acknowledged)

# for item in cable_list:
#     print(item)
#     new_doc = collection4.insert_one(item)
#     print(new_doc.acknowledged)

# for item in dc_list:
#     print(item)
#     new_doc = collection4.insert_one(item)
#     print(new_doc.acknowledged)

# for item in other_list:
#     print(item)
#     new_doc = collection4.insert_one(item)
#     print(new_doc.acknowledged)


#Testing of V4 connection
# collection4 = mydb4["ios-xr-draft"]
# dbaas_dict = {"platform": "ios-xr-pi", "release": "release independent", "component": "vpls"}
# doc = collection4.find_one(dbaas_dict)
# print(doc)
# raw_content = []
# raw_content.append(doc.get("commands"))
# raw_content.append(doc.get("links"))
# for item in raw_content:
#     print(item)
