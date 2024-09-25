import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_methods(self):
        test_list = []

        test_list.append(ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
))

        test_list.append(ParentNode(
    "p",
    [
        ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
))

        test_list.append(ParentNode(
    "p",
    [
        ParentNode(
    "p",
    [
        ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
))

        test_list.append(ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
))

        for item in test_list:
            print(item.to_html())

if __name__ == "__main__":
    unittest.main()