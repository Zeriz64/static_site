import os
import shutil
from pathlib import Path
from markdown import *
from htmlnode import *

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path, "r")
    contents = file.read()
    file.close()
    template_file = open("template.html")
    template = template_file.read()
    template_file.close()
    node = markdown_to_html_node(contents)
    html_string = node.to_html()
    title = extract_title(contents)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    html_file = open(dest_path, "w")
    html_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        location = dir_path_content + "/" + file
        destination = dest_dir_path + "/" + file
        if os.path.isfile(location):
            destination = Path(destination).with_suffix(".html")
            generate_page(location, template_path, destination)
        else:
            generate_pages_recursive(location, template_path, destination)
