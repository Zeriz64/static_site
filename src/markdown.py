import re

from textnode import *

block_type_para = "paragraph"
block_type_head = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered list"
block_type_olist = "ordered list"

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
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

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
                if split_node == "":
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

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        if block == "":
            continue
        cleaned_blocks.append(block.strip())
    return cleaned_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_head

    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_para
        return block_type_quote

    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_para
        return block_type_ulist

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_para
        return block_type_ulist

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_para
            i += 1
        return block_type_olist

    return block_type_para

def markdown_to_html_node(markdown):
    blocks =  markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == block_type_para:
            node = para_to_html(block)
        
        elif block_type == block_type_head:
            node = head_to_html(block)

        elif block_type == block_type_code:
            node = code_to_html(block)
        
        elif block_type == block_type_quote:
            node = quote_to_html(block)

        elif block_type == block_type_ulist:
            node = ulist_to_html(block)

        elif block_type == block_type_olist:
            node = olist_to_html(block)
        
        else:
            raise ValueError("Invalid block type.")

        children.append(node)
    return ParentNode("div", children)

def para_to_html(block):
    split = block.split("\n")
    text = " ".join(split)
    children = text_to_children(text)
    return ParentNode("p", children)

def head_to_html(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    if count + 1 >= len(block):
        raise ValueError("Invalid heading level.")
    children = text_to_children(block[count + 1:])
    return ParentNode(f"h{count}", children)

def code_to_html(block):
    split = block.split("```")
    text = block[4:-3]
    children = text_to_children(text)
    node = ParentNode("code", children)
    return ParentNode("pre", [node])

def quote_to_html(block):
    split = block.split("\n")
    new_text = []
    for line in split:
        line = line.lstrip(">")
        new_text.append(line.strip())
    text = " ".join(new_text)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def ulist_to_html(block):
    split = block.split("\n")
    items = []
    for line in split:
        line = line[2:]
        children = text_to_children(line)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def olist_to_html(block):
    split = block.split("\n")
    items = []
    for line in split:
        line = line[3:]
        children = text_to_children(line)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No Header.")
