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

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        print(text_to_textnodes(text))
        print("====================\nTextNode Test End\n====================")

    if __name__ == "__main__":
        unittest.main()
