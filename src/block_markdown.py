from enum import Enum
from textnode import TextNode,TextType,text_node_to_html_node
from splitNodesDelimiter import text_to_textnodes
from parentNode import ParentNode
from leafNode import LeafNode

def markdown_to_blocks(md:str)->list[str]:
    blockStr=md.split("\n\n")
    return list(
        filter(lambda block: len(block) > 0,
        map(lambda el: el.strip(),blockStr)))

class BlockType (Enum):
    PARAGRAPH= "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def is_heading_block(block:str):
    last_Char_Block=-1
    if len(block) < 0:
        return False
    limit_for = min(len(block),6)
    for i in range(limit_for +1):
        el=block[i]
        if el == "#":
            last_Char_Block = i 
        if el != "#":
            break
    return last_Char_Block >=0 and last_Char_Block <= 5 and block[last_Char_Block+1] ==" "

def is_code_block(block:str):
    start_substr="```\n"
    end_substr ="```"
    return block.startswith(start_substr) and block.endswith(end_substr)

def is_quote_block(block: str):
    lines = block.splitlines()
    return all(line.startswith(">") for line in lines)

def is_unorder_block(block:str):
    lines = block.splitlines()
    result_lines = list(filter(lambda line:line.startswith("- "),lines))
    return len(lines) == len(result_lines)

def is_order_block(block:str):
    lines = block.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        #idx=line.find(". ")
        if not line.startswith(f'{i+1}. '):
            return False
        

    return True




def block_to_block_type(block:str):
    if is_heading_block(block):
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unorder_block(block):
        return BlockType.ULIST
    if is_order_block(block):
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def get_tag_block_type(type_block:BlockType,block:str)->str:
    match type_block:
        case BlockType.HEADING:
            return get_tag_heading(block)
        case BlockType.CODE:
            return "pre"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.ULIST:
            return "ul"
        case BlockType.OLIST:
            return "ol"
        case BlockType.PARAGRAPH:
            return "p"
        case _:
            raise ValueError(f"invalid block type: {type_block}")


def text_to_children_quote(text: str):
    lines = text.split("\n")
    cleaned = [line.lstrip(">").strip() for line in lines]
    content = " ".join(cleaned)
    return ParentNode(tag="blockquote", children=text_to_children(content))


    

def text_to_children_order_list(text:str):
    lines = text.splitlines()
    for i in range(len(lines)):
        lines[i]=lines[i].removeprefix(f'{i+1}. ').strip()
    result=[]
    for line in lines:
        result.append(ParentNode(tag = "li",children=text_to_children(line)))
    return result

def text_to_children_unorder_list(text:str):
    lines = text.splitlines()
    for i in range(len(lines)):
        lines[i]=lines[i].removeprefix("- ").strip()
    result=[]
    for line in lines:
        result.append(ParentNode(tag = "li",children=text_to_children(line)))
    return result

def text_to_children_p(text:str):
    update_text = text.replace("\n"," ")
    return text_to_children(update_text)
    #nodes = list(map(lambda el:text_to_textnodes(el),lines))

def get_tag_heading(text:str):
    pos = -1
    index = 0
    while(text[index] == "#"):
        index+=1
        pos=index
    
    if pos == -1 or pos > 6:
        raise ValueError("invalid heading")
    return f'h{pos}'

def text_to_children_heading(text:str):
    pos = -1
    index = 0
    while(text[index] == "#"):
        index+=1
        pos=index
    
    new_text = text[pos +1:].strip()
    return text_to_children(new_text)






def text_to_children(text:str):
    return list(map(lambda html_node:text_node_to_html_node(html_node),text_to_textnodes(text)))
   


def markdown_to_html_node(block:str):
   blocks=markdown_to_blocks(block)
   children_nodes=[]
   for block in blocks:
       block_type = block_to_block_type(block)
       tag_html_block = get_tag_block_type(block_type,block)
       ###
       #if block_type == BlockType.CODE:
        #node = TextNode(text_type=TextType.CODE,text=block)
        #children_node = TextNode(text=block,text_type=TextType.CODE)
        #children_node = text_node_to_html_node(children_node)
        #children_html_nodes_block = map(lambda html_node:text_node_to_html_node(html_node),text_to_textnodes(block))
        #children_nodes.append(ParentNode(tag=tag_html_block,children=children_node))
       #else:
           #children_nodes.append(ParentNode(tag=tag_html_block,children=text_to_children(block)))
   
       match block_type:
           case BlockType.PARAGRAPH:
               children_nodes.append(ParentNode(tag=tag_html_block,children=text_to_children_p(block)))
               
           case BlockType.CODE:
               #node = TextNode(text_type=TextType.CODE,text=block[4:-3])
               children_nodes.append(ParentNode(tag=tag_html_block,children=[LeafNode(tag ="code",value=block[4:-3])]))
               
           case BlockType.QUOTE:
               children_nodes.append(text_to_children_quote(block))
               
           case BlockType.OLIST:
               children_nodes.append(ParentNode(tag = tag_html_block,children=text_to_children_order_list(block)))
                             
           case BlockType.ULIST:
                children_nodes.append(ParentNode(tag = tag_html_block,children=text_to_children_unorder_list(block)))
           case BlockType.HEADING:
               #children_nodes.append(text_to_children_heading(block))
               children_nodes.append(ParentNode(tag=tag_html_block,children=text_to_children_heading(block)))
               
               

               
           
   
   
   return ParentNode(tag="div",children=children_nodes)
def extract_title(markdown:str)->str:
    blocks = markdown_to_blocks(markdown)
    if len(blocks) == 0:
        raise ValueError("invalid markdown")
    head_block = list(filter(lambda bl:get_tag_heading(bl) == "h1",filter(is_heading_block,blocks)))
    
    if len(head_block) != 1:
        raise ValueError("no tag heading present")
    return head_block[0].strip("# ")



    
    

