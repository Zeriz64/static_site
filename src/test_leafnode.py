import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_methods(self):
        print("====================\nLeafNode Test Start\n====================")
        test_list = []
        test_list.append(LeafNode("tag", "value", {"prop": "value", "prop2": "value2"}))
        test_list.append(LeafNode("tag", "value", {"prop": "value"}))
        test_list.append(LeafNode(None, "value", {"prop": "value", "prop2": "value2"}))
        test_list.append(LeafNode("tag", "value", None))
        for item in test_list:
            print(item)
            print(item.to_html())
        print("====================\nLeafNode Test End\n====================")

if __name__ == "__main__":
    unittest.main()