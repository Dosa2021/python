import asyncio
import time
import os
import re

async def exec_batch(file):
    await asyncio.sleep(5)
    print(f"{time.strftime('%X')} - {file}")

async def main():
    print(f"{time.strftime('%X')} - start")
    files = os.listdir('/Users/tatsuya.sugawara/dosa/python/files')

    funcs = []

    for file in files:
        if re.search('\.txt', file) != None:
            funcs.append(exec_batch(file))

    await asyncio.gather(*funcs)
    print(f"{time.strftime('%X')} - finish")


asyncio.run(main())