import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
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


if __name__ == "__main__":
    unittest.main()