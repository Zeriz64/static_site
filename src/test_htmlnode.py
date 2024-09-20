import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_methods(self):
        test_list = []
        test_list.append(HTMLNode("tag", "value", "children", {"prop": "value", "prop2": "value2"}))
        test_list.append(HTMLNode("tag", "value", "children", {"prop": "value"}))
        test_list.append(HTMLNode(None, "value", None, {"prop": "value", "prop2": "value2"}))
        test_list.append(HTMLNode("tag", "value", "children", None))
        for item in test_list:
            print(item)
            print(item.props_to_html())

if __name__ == "__main__":
    unittest.main()
