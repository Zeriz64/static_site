import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("====================\nTextNode Test Start\n====================")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_methods(self):
        node_list = []
        node_list.append(TextNode("This is Text Node", "text"))
        node_list.append(TextNode("This is Bold Node", "bold"))
        node_list.append(TextNode("This is Italic Node", "italic"))
        node_list.append(TextNode("This is Code Node", "code"))
        node_list.append(TextNode("This is link Node", "link", "link.url"))
        node_list.append(TextNode("This is Image Node", "image", "image.url"))
        for node in node_list:
            print(text_node_to_html_node(node))

    def test_delimiter(self):
        delimit_list = []
        delimit_list.append(TextNode("This is a Text Node", "text"))
        delimit_list.append(TextNode("This is a Text Node with **Bold**", "text"))
        delimit_list.append(TextNode("This is a Text Node with *Italic*", "text"))
        delimit_list.append(TextNode("This is a Text Node with `code`", "text"))
        delimit_list.append(TextNode("This is a Text Node with `code` and **Bold**", "text"))
        delimit_list.append(TextNode("This is a Text Node with *Italic*, **Bold**, and `code`", "text"))
        for delimit in delimit_list:
            new_nodes = split_nodes_delimiter([delimit], "**", text_type_bold)
            new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
            new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)

    def test_markdown_images(self):
        print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"))

    def test_markdown_links(self):
        print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)"))

    def test_split_image(self):
        print(split_nodes_image([TextNode("This is a Text Node with an ![image](http://link_to_image.com)", "text")]))
        print(split_nodes_image([TextNode("This is a Text Node ![image](http://link_to_image.com) with an ![image2](http://link_to_image2.com)", "text")]))
        print(split_nodes_image([TextNode("This is a Text Node with an ![image](http://link_to_image.com) and a ![image2](http://link_to_image2.com) and a ![image3](http://link_to_image3.com)", "text")]))

    def test_split_link(self):
        print(split_nodes_link([TextNode("This is a Text Node with an [description](http://link.com)", "text")]))
        print(split_nodes_link([TextNode("This is a Text Node [description](http://link.com) with an [description2](http://link2.com)", "text")]))
        print(split_nodes_link([TextNode("This is a Text Node with an [description](http://link.com) and a [description2](http://link2.com) and a [description3](http://link3.com)", "text")]))
        print("====================\nTextNode Test End\n====================")

if __name__ == "__main__":
    unittest.main()
