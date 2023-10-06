import os
import sys
import json

settings = {
    'crumb_path': None,
    'output_path': ""
}

def get_merged_content():
    print("Beginning file merge...")
    files = {}

    for file_name in os.scandir(settings['crumb_path']):
        if file_name.is_file() and file_name.name != "crumbs.json":
            file_index = file_name.name.removesuffix(".json")
            file_content = open(file_name.path).read()

            files[file_index] = json.loads(file_content)
    
    print("Finished merging files")
    return json.dumps(files)

def bake_crumbs():
    if settings['crumb_path']:
        if os.path.exists(settings['crumb_path']):
            merged_content = get_merged_content()

            message = "provided directory"
            if settings['output_path'] == "":
                message = "execution location"
            
            print(f"Writing packed crumb file to {message}...")

            with open(settings['output_path'] +  "crumbs.json", "w") as output:
                output.write(merged_content)
                output.close()
        else:
            return "Provided crumb directory does not exist!"
    else:
        return "No crumb directory provided!"

if __name__ == "__main__":
    for arg in sys.argv:
        if arg.startswith("-P"):
            real_arg = arg.removeprefix("-P")

            settings['crumb_path'] = real_arg
            settings['output_path'] = real_arg
        elif arg.lower() == "-k" and settings['crumb_path'] is not None:
            settings['output_path'] = ""
    
    bake_error = bake_crumbs()
    if bake_error:
        print("Failed to bake crumbs:\n\t" + bake_error)
    else:
        print("Successfully baked crumbs!")