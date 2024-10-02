import os
import shutil

def static_to_public(static_path="/home/zeriz/workspace/course_projects/static_site/static", public_path="/home/zeriz/workspace/course_projects/static_site/public"):
    if not os.path.exists(static_path):
        raise Exception(f"{static_path} does not exist.")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    path_list = os.listdir(static_path)
    for path in path_list:
        new_static_path = static_path + "/" + path
        new_public_path = public_path + "/" + path
        if not os.path.isfile(new_static_path):
            static_to_public(new_static_path, new_public_path)
        else:
            shutil.copy(new_static_path, new_public_path)
