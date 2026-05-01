import os
import shutil

def check_exists_is_dir(path:str):
    if not os.path.exists(path):
          raise ValueError(f"{path} ivalid path")
    if not os.path.isdir(path):
         raise ValueError(f"{path} is not a directory")
    

    

def copy_dir_to_dest(src:str,dest:str):
     abs_path_source = os.path.abspath(src)
     abs_path_dest =os.path.abspath(dest)
     check_exists_is_dir(abs_path_source)
     check_exists_is_dir(abs_path_dest)
     print(f"copying the content of dir {abs_path_source} in dest dir:{abs_path_dest}")
     #1) delete all the file from dest source
     shutil.rmtree(abs_path_dest)
     os.mkdir(abs_path_dest)
     #2) find all the files/dir from src source
     elements_in_dir_src = os.listdir(abs_path_source)
     for element in elements_in_dir_src:
        path_element = os.path.join(abs_path_source,element)
        print(f"considering element {path_element}")
        if os.path.isdir(path_element):
             print(f"element {path_element} is a directory")
             new_dir_dest = os.path.join(abs_path_dest,element)
             os.mkdir(new_dir_dest)
             copy_dir_to_dest(path_element,new_dir_dest)
             
        if os.path.isfile(path_element):
            print(f"element {path_element} is a file,cpytng the file in {abs_path_dest}")
            shutil.copy(path_element,abs_path_dest)
        
        #print(f"element {path}, is_dir:{os.path.isdir(path)}, is_file:{os.path.isfile(path)}")   


         


