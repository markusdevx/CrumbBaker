import os
import sys
import json

CRUMB_PATH = "./yukon/assets/media/crumbs/en"

def merge_files():
    print("Beginning file merge...")
    files = {}

    for file_name in os.scandir(CRUMB_PATH):
        if file_name.is_file() and file_name.name != "crumbs.json":
            file_index = file_name.name.removesuffix(".json")
            file_content = open(file_name.path).read()

            files[file_index] = json.loads(file_content)
    
    return json.dumps(files)

if __name__ == "__main__":
    #arg_path = sys.argv[1]
    merged = merge_files()

    with open("crumbs.json", "w") as output:
        output.write(merged)
        output.close()
    
    print("Finished baking crumbs file!")