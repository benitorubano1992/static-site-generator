import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_diff(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_link_difff(self):
        second_text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
        first_text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.google.com")
        self.assertNotEqual(second_text_node, first_text_node)
    def test_link_eq(self):
        second_text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
        first_text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
        self.assertEqual(second_text_node, first_text_node)


if __name__ == "__main__":
    unittest.main()