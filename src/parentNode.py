from htmlnode import HTMLNode
from leafNode import LeafNode


class ParentNode(HTMLNode):
     def __init__(self,tag =None,children=None,props=None):
        super().__init__(tag,None,children,props)
     def to_html(self):
         if self.tag is None:
             raise ValueError("invalid HTML: no tag")
         if self.children is None:
             raise ValueError("invalid HTML: no children")
         result =f"<{self.tag}{self.props_to_html()}>"
         for child in self.children:
             if child is None:
                 continue
             if not isinstance(child,LeafNode) and not isinstance(child,HTMLNode):
                 continue
             result+= child.to_html()
         return result +f"</{self.tag}>"
    