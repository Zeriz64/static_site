import os
import shutil

def static_to_public(static="/home/zeriz/workspace/course_projects/static_site/static", public="/home/zeriz/workspace/course_projects/static_site/public"):
    if not os.path.exists(static):
        raise Exception(f"{static} does not exist.")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    path_list = os.listdir(path)
    for path in path_list:
        static = static + "/" + path
        public = public + "/" + path
        if not os.path.isfile(path):
            os.mkdir(static)
            os.mkdir(public)
            static_to_public(static, public_path)
        else:
            shutil.copy(path, public_path)
