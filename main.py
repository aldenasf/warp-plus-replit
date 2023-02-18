from pymongo import MongoClient
from dotenv import load_dotenv
from threading import Thread
from flask import Flask
import urllib.request
import urllib.error
import datetime
import string
import random
import time
import json
import os

############# IMPORTANT #############

load_dotenv()
thread_number = 1
referrer = os.environ['ID']
thread = MongoClient(os.environ['MONGODB'])["test"]["Thread"]

############# IMPORTANT #############


# time_start = int(str(datetime.datetime.now().timestamp())[:10])

app = Flask("")


@app.route("/")
def index():
    return f"<pre>Thread ID: {thread_number}<br>Good: {good}<br>Bad: {bad}<br>Total: {good+bad}</pre>"


Thread(target=app.run, args=("0.0.0.0", 8080)).start()

print("Script coded by ALILAPRO\nModified by AldenizenMC")


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


def createObjIfNotExist():
    print("checking if object exists...")
    object = thread.find_one({"Thread": thread_number})
    if (object == None):
        print("object not found, creating one...")
        thread.insert_one({
            "Thread": thread_number,
            "good": 0,
            "bad": 0,
        })
        print("object created!")
    else:
        print("object exists!")


def incrementGood():
    object = thread.find_one_and_update(
        {"Thread": thread_number},
        {"$inc": {"good": 1}}
    )


def incrementBad():
    object = thread.find_one_and_update(
        {"Thread": thread_number},
        {"$inc": {"bad": 1}}
    )


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
print(url)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    try:
        install_id = genString(22)
        body = {
            "key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES"
        }
        data = json.dumps(body).encode('utf8')
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
        print("creating request...")
        req = urllib.request.Request(url, data, headers)
        print("opening request...")
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except urllib.error.HTTPError as error:
        return error.code


good = 0
bad = 0

createObjIfNotExist()

print("executing while loop...")

while True:
    print("executing run()")
    result = run()
    if result == 200:
        good = good + 1
        cls()
        print(
            f"thread: {thread_number}\nreferrer: {referrer} (last 5 digit)")
        print(f"code: {result} | good. sleeping for 18 seconds")
        print(f"{good+bad} total | {good} good | {bad} bad")
        incrementGood()
        time.sleep(18)
    elif result == 429:
        bad = bad + 1
        cls()
        print(
            f"thread: {thread_number}\nreferrer: {referrer} (last 5 digit)")
        print(f"code: {result} | rate limit. sleeping for 18 seconds")
        print(f"{good+bad} total | {good} good | {bad} bad")
        incrementBad()
        time.sleep(18)
    else:
        bad = bad + 1
        cls()
        print(
            f"thread: {thread_number}\nreferrer: {referrer} (last 5 digit)")
        print(f"code: {result} | retrying...")
        print(f"{good+bad} total | {good} good | {bad} bad")
        incrementBad()
