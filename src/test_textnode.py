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
            print(new_nodes)
        print("====================\nTextNode Test End\n====================")


if __name__ == "__main__":
    unittest.main()