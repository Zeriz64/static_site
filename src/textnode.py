import re

from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Invalid Text Type.")

def split_nodes_delimiter(nodes, delimiter, text_type):
    new_nodes = []
    for node in nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception(f"Improper Markdown formatting in {node}")
        delimited_nodes = []
        for i in range(0, len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                delimited_nodes.append(TextNode(split_node[i], text_type_text))
            else:
                delimited_nodes.append(TextNode(split_node[i], text_type))
        new_nodes.extend(delimited_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([\w\s]*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if images == []:
            new_nodes.append(node)
            continue
        split_image_nodes = []
        for image in images:
            image_alt, image_link = image[0], image[1]
            split_node = node_text.split(f"![{image_alt}]({image_link})", 1)
            if len(split_node) != 2:
                raise ValueError("Image not closed.")
            for i in range(0, len(split_node)):
                if split_node[i] == "":
                    continue
                if i == 0:
                    new_nodes.append(TextNode(split_node[0], text_type_text))
                    new_nodes.append(TextNode(image_alt, text_type_image, image_link))
                else:
                    node_text = split_node[1]
            if node_text != "":
                new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if links == []:
            new_nodes.append(node)
            continue
        split_link_nodes = []
        for link in links:
            link_alt, link_link = link[0], link[1]
            split_node = node_text.split(f"[{link_alt}]({link_link})", 1)
            if len(split_node) != 2:
                raise ValueError("Link not closed.")
            for i in range(0, len(split_node)):
                if split_node == "":
                    continue
                if i == 0:
                    new_nodes.append(TextNode(split_node[0], text_type_text))
                    new_nodes.append(TextNode(link_alt, text_type_link, link_link))
                else:
                    node_text = split_node[1]
            if node_text != "":
                new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    node_list = split_nodes_delimiter([TextNode(text, text_type_text)], "**", text_type_bold)
    node_list = split_nodes_delimiter(node_list, "*", text_type_italic)
    node_list = split_nodes_delimiter(node_list, "`", text_type_code)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    return node_list
