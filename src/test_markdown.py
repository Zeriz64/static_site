import unittest

from markdown import *

class TestMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        print("====================\nMarkdown Test Start\n====================")
        block = "  this is the first line  \n\n a second line     \n\nand lastly a third line\n\n"
        print(markdown_to_blocks(block))

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        print(text_to_textnodes(text))

    def test_block_to_blocktype(self):
        markdown = "This is the start of the paragraph\n\n# 1 header \n\n ## 2 header \n\n ### 3 header \n\n #### 4 header \n\n ##### 5 header \n\n ###### 6 header \n\n```\n this is a code block \n``` \n\n>this is a quote block \n\n* unorder1\n* unorder2\n\n- unorder1\n- unorder2\n\n1. order1\n2. order2\n3. order3\n\nend of the paragraph"
            
        block = markdown_to_html_node(markdown)

        print(block)
        print("====================\nMarkdown Test End\n====================")

    if __name__ == "__main__":
        unittest.main()
