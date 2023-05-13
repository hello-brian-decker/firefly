from flask import Flask
import consul
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]
post = {"title": "My post", "content": "This is my first post!"}
collection.insert_one(post)



app = FastAPI()


@app.post("/download")
def download(data: dict):
    download_ip = get_ip_by_name(data["download_name"])
    upload_ip = get_ip_by_name(data["upload_name"])
    url = get_ip_by_name(data["url"])
    path = data["path"]
    dot_torrent, torrent_name = parse_url(url)
    cmd = f"qbittorrent {path}/{dot_torrent}"
    upload_location = data["upload_location"]
    file = ""
    unzip(file)
    return {"message": "JSON received"}


def parse_url(url):
    dot_torrent = ""
    torrent_name = ""
    return dot_torrent, torrent_name


def unzip(file):
    # check if file is zipped and unzip if needed
    ...


@app.post("/upload")
def upload():
    ...


def get_ip_by_name(service_name):
    c = consul.Consul()
    # Use the Consul API to retrieve the list of nodes providing the service
    index, nodes = c.health.service(service_name)
    # Select a node at random (you could also use a load-balancing algorithm here)
    node = nodes[0]
    # Retrieve the IP address of the node
    ip_address = node['Service']['Address']
    return ip_address


# uvicorn main:app --reload
#
# curl --header "Content-Type: application/json" \
#   --request POST \
#   --data '{"key": "value"}' \
#   http://localhost:8000/json


