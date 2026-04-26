from enum import Enum
from leafNode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 
    def __eq__(self, other_text_node):
        if not isinstance(other_text_node,TextNode):
            return False
        return (
            self.text == other_text_node.text
            and self.text_type == other_text_node.text_type
            and self.url == other_text_node.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    

def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b",value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i",value=text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code",value=text_node.text)
    if text_node.text_type == TextType.LINK:
        props={
            "href":text_node.url,
            
        }
        return LeafNode(tag="a",value=text_node.text,props=props)
    if text_node.text_type == TextType.IMAGE:
        props={
            "src":text_node.url,
            "alt":text_node.text,
        }
        return LeafNode(tag="img",value="",props=props)
    raise ValueError(f"invalid text type: {text_node.text_type}")
        