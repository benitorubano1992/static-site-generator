import os
from block_markdown import markdown_to_html_node,extract_title
PATH_FILE = "index.html"
def generate_pages_recursive(dir_path_content:str, template_path:str, dest_dir_path:str,base_path:str):
    if os.path.isfile(dir_path_content):
        return generate_page(dir_path_content,template_path,os.path.join(dest_dir_path,PATH_FILE),base_path)
    elements_content = os.listdir(dir_path_content)
    for el in elements_content:
        path_el = os.path.join(os.path.abspath(dir_path_content),el)
        if os.path.isdir(path_el):
            generate_pages_recursive(path_el,template_path,os.path.join(dest_dir_path,el),base_path)
            continue
        generate_page(path_el,template_path,os.path.join(dest_dir_path,PATH_FILE),base_path)
    



def generate_page(from_path, template_path, dest_path,base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file=""
    with open(os.path.abspath(from_path), "r") as f:
        markdown_file = f.read()
    template_file=""
    with open(os.path.abspath(template_path),"r") as t:
        template_file=t.read()
    html_str_md = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    template_file = template_file.replace("{{ Title }}",title).replace("{{ Content }}",html_str_md)
    template_file.replace('href="/',f'href="{base_path}').replace('src="/',f'src="{base_path}')
    os.makedirs(os.path.dirname(os.path.abspath(dest_path)), exist_ok=True) 
    with open(os.path.abspath(dest_path),"w") as d:
        d.write(template_file)
    



    


