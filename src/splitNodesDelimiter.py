from textnode import TextNode,TextType
import re
def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
    result=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        parts=node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("text type incorrected, check end delimiter")
        resultPart=[]
        for i in range(0,len(parts)):
            part_text_type = text_type
            if i % 2 == 0:
                part_text_type = TextType.TEXT
            if len(parts[i]) > 0:
                resultPart.append(TextNode(text_type=part_text_type,text=parts[i]))
        result.extend(resultPart)
    return result

def extract_markdown_images(text):
    matches=re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches
        
def split_nodes_image(old_nodes:list[TextNode]):
    result=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        parts = extract_markdown_images(node.text)
        if len(parts) == 0:
            result.append(node)
            continue
        textNode = node.text
        result_parts=[]
        for part in parts:
            alt,image = part
            textNodeEls=textNode.split(f"![{alt}]({image})",1)
            if len(textNodeEls) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if len(textNodeEls[0]) > 0:
                result_parts.append(TextNode(text_type=TextType.TEXT,text =textNodeEls[0]))
            result_parts.append(TextNode(text_type=TextType.IMAGE,text=alt,url=image))
            textNode = textNodeEls[-1]
        if len(textNode) > 0:
            result_parts.append(TextNode(text_type=TextType.TEXT,text =textNode))
        result.extend(result_parts)
    return result
def split_nodes_link(old_nodes:list[TextNode]):
    result=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        parts = extract_markdown_links(node.text)
        if len(parts) == 0:
            result.append(node)
            continue
        textNode = node.text
        result_parts=[]
        for part in parts:
            alt_text,url_link = part
            textNodeEls=textNode.split(f"[{alt_text}]({url_link})",1)
            if len(textNodeEls) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if len(textNodeEls[0]) > 0:
                result_parts.append(TextNode(text_type=TextType.TEXT,text =textNodeEls[0]))
            result_parts.append(TextNode(text_type=TextType.LINK,text=alt_text,url=url_link))
            textNode = textNodeEls[-1]
        if len(textNode) > 0:
            result_parts.append(TextNode(text_type=TextType.TEXT,text =textNode))
        result.extend(result_parts)
    return result



def text_to_textnodes(text):
    result=[TextNode(text_type=TextType.TEXT,text=text)]
    result = split_nodes_delimiter(result,"**",TextType.BOLD)
    result = split_nodes_delimiter(result,"_",TextType.ITALIC)
    result=split_nodes_delimiter(result,"`",TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result

        
