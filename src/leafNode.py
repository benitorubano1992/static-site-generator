from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag =None,value=None,children=None,props=None):
        super().__init__(tag,value,None,props)
    def to_html(self):
        if self.value is None:
             raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        if len(self.props_to_html().strip()) > 0:
             return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result=[]
        for key,val in self.props.items():
            appendVal=" "
            if len(result) > 0:
                appendVal=""
            result.append(f'{appendVal}{key}="{val}"')

        return " ".join(result)
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.props_to_html()})"




