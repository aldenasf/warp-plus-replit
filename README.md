# WARP+ Worker for Replit
This script is a modified version of [warp-plus-cloudflare](https://github.com/Zeus-Kernel-Development/warp-plus-cloudflare) to work on replit with multiple repls and is able to track the "good" and "bad" using MongoDB. **This script is for personal use and is not meant for public use, which means that you cannot just run the script and expecting it to work without modifying it.**

The script works by doing the referrer thing (i dont really know how it works tbh) and on "good" instead of just saying you got 1GB of WARP+, it also increments the "good" value in an object in MongoDB with an id unique to the repl.

You can display all the information using a table like so

| Thread    | Good   | Bad    | Status |
| --------- | ------ | ------ | ------ |
| Thread 1  | 23     | 17     | 🟢 200 |
| Thread 2  | 38     | 29     | 🟢 200 |
| Thread 3  | 12     | 37     | 🟢 200 |
| Thread 4  | 24     | 15     | 🔴 500 |
| Thread 5  | 21     | 34     | 🔴 500 |
| **Total** | **118**| **132**|        |