import json
import redis3
from bottle import *
"""
Redis has to be started on the same localhost with command
docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest
v4_redis.py file takes the data from production mongoDB and update Redis
"""
r = redis3.Redis(host='127.0.0.1', port=6379)

@get('/')    # http://localhost:<port>
def welcome():
    response.set_header('Vary', 'Accept')
    response.content_type = 'application/json'
    return 'REST API for Lighthouse v5'

@get('/collections')    # http://localhost:<port>/collections
def get_platform_list():
    response.content_type = 'application/json'
    collection_list = []
    for key in r.keys():
        collection = key.decode("utf-8").split("@")[0]
        collection_list.append(collection)
    collections = list(set(collection_list))
    collections.sort()
    return json.dumps(collections)

@get('/platforms')    # http://localhost:<port>/platforms
def get_platform_list():
    response.content_type = 'application/json'
    input_data = json.load(request.body)
    selected_collection = input_data['collection']
    platform_list = []
    for key in r.keys():
        collection = key.decode("utf-8").split("@")[0]
        platform = key.decode("utf-8").split("@")[1]
        if collection == selected_collection:
            platform_list.append(platform)
    platforms = list(set(platform_list))
    platforms.sort()
    return json.dumps(platforms)

@get('/components')    # http://localhost:<port>/components
def get_component_list():
    response.content_type = 'application/json'
    input_data = json.load(request.body)
    selected_collection = input_data['collection']
    selected_platform = input_data['platform']
    component_list = []
    for key in r.keys():
        collection = key.decode("utf-8").split("@")[0]
        platform = key.decode("utf-8").split("@")[1]
        component = key.decode("utf-8").split("@")[2]
        if platform == selected_platform and collection == selected_collection:
            component_list.append(component)
    components = list(set(component_list))
    components.sort()
    return json.dumps(components)

@get('/releases')    # http://localhost:<port>/releases
def get_release_list():
    response.content_type = 'application/json'
    input_data = json.load(request.body)
    selected_collection = input_data['collection']
    selected_platform = input_data['platform']
    selected_component = input_data['component']
    release_list = []
    for key in r.keys():
        collection = key.decode("utf-8").split("@")[0]
        platform = key.decode("utf-8").split("@")[1]
        component = key.decode("utf-8").split("@")[2]
        release =  key.decode("utf-8").split("@")[3]
        if platform == selected_platform and component == selected_component and collection == selected_collection:
            release_list.append(release)

    releases = list(set(release_list))
    releases.sort()
    return json.dumps(releases)

@get('/entry')    # http://localhost:<port>/entry
def get_entry():
    response.content_type = 'application/json'
    input_data = json.load(request.body)
    collection = input_data['collection']
    platform = input_data['platform']
    component = input_data['component']
    release = input_data['release']
    selected_key = collection + "@" + platform + "@" + component + "@" + release
    selected_value = r.get(selected_key)
    return json.loads(selected_value)

if __name__ == '__main__':
    run(host='localhost', port=9600)
