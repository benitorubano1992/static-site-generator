import unittest

from leafNode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        #dict_link={
         #    "href": "https://www.google.com",
          #   "target": "_blank"
           #  }
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),"<p>This is a paragraph of text.</p>" )
       
    def a_leafNode(self):
        a_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(a_leaf.props_to_html(),' href="https://www.google.com"')
        self.assertEqual(a_leaf.to_html(),'<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
  
   


if __name__ == "__main__":
    unittest.main()