import re
import requests
import os


def get_content(dirname, data):
    os.mkdir(dirname)
    os.chdir(f"./{dirname}")

    pattern = r'(https:\/\/[A-Za-z0-9.]+\/[A-Za-z0-9\-_]+\/[A-Za-z0-9]+\/12\/[0-9_]+\.jpg)'
    data_collect = re.findall(pattern, data)
    collection_length = len(data_collect)

    names = []
    print("Collecting data from web...")

    for url in data_collect:
        filename = url[-7:]
        names.append(filename)
        response = requests.get(url)
        if response.status_code == 200:
            try:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                    #print(f"Saving {len(names)} out of {collection_length} ...")
            except FileNotFoundError:
                print(f"{filename}: FileNotFoundError")

    names.sort()

    length = int(names[-1][0]) + 1
    width = int(names[-1][2]) + 1
    #print("Saved successfully.")

    return length, width
