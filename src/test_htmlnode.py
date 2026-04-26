import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        dict_link={
             "href": "https://www.google.com",
             "target": "_blank"
             }
        node = HTMLNode("a","prova link",[],dict_link)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())
       
    def test_h1(self):
        h1_node = HTMLNode("h1","test title",[])
        self.assertEqual("HTMLNode(h1,test title,[],"")",repr(h1_node))
    def test_img(self):
        dict_img={
            "src":"https://www.google.com",
            "width":"400"
        }
        img_node = HTMLNode("img","image text",[],dict_img)
        self.assertEqual(' src="https://www.google.com" width="400"',img_node.props_to_html())
   


if __name__ == "__main__":
    unittest.main()