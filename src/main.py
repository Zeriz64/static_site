from textnode import *
from static_to_public import *

def main():
    static_to_public()
    generate_pages_recursive("/home/zeriz/workspace/course_projects/static_site/content", "/home/zeriz/workspace/course_projects/static_site/template.html", "/home/zeriz/workspace/course_projects/static_site/public")

main()
