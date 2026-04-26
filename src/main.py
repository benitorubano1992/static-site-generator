from textnode import TextNode,TextType
from htmlnode import HTMLNode


def main():
    text_node = TextNode("example_text",TextType.TEXT)
    second_text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    dict_link={
             "href": "https://www.google.com",
             "target": "_blank"
             }
    node = HTMLNode("a","prova link",[],dict_link)
    print(node.props_to_html())
    dict_img={
            "src":"https://www.google.com",
            "width":"400"
        }
    img_node = HTMLNode("img","image text",[],dict_img)
    print(img_node.props_to_html())
    print(f"test is passed {img_node.props_to_html() == ' src="https://www.google.com" width="400"'} ")
    #print(text_node)
    #print(second_text_node)
main()