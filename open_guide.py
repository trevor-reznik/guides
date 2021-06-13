"""
Script to open guide/cheatsheet from this repo.
Usage:
    python3 open_guide.py name [keyword]
Example:
    python3 open_guide.py css
    >> opens all guides in css folder
    python3 open_guide.py python style
    >> opens python style guide
    python3 open_guide.py cpp workflow
    >> opens cpp workflow checklist
"""

import webbrowser, ntpath, os, sys
from os import walk


ROOT = "https://github.com/trevor-reznik/guides/blob/master/{}"
IMG_EXTENSIONS = ["jpg", "png", "tif", "raw", "eps", "gif", "psd", "xcf",
            "ai", "cdr", "bmp", "jpeg", "cr2", "nef", "orf",
            "sr2", "jpe", "jif", "jfif", "jfi", "webp", "k25",
            "nrw", "arw", "dib", "heif", "heic", "ind", "indd",
            "indt", "jp2", "j2k", "jpf", "jpx", "jpm", "mj2",
            "svg", "svgz"]


def get_directories(dir_name):
    """ 
    Recursively build list of directories in and below dir_name.

    Returns:
        list : all files in every directory in and below dir_name, 
            recursively. File elements are named with their path relative to the 
            root (dir_name). Last element in list will be the dir_name.
    
    Args: 
        dir_name (str): relative path to root directory.
    """

    subfolders= [f.path for f in os.scandir(dir_name) if f.is_dir()]
    for dir_name in list(subfolders):
        subfolders.extend(get_directories(dir_name))
    subfolders.append(dir_name)

    return subfolders


def treeify_directory(path_list, valid_extensions=False):
  """
  Accepts list of paths and returns dictionary with details about
  every folder.

  Args:
    path_list (list): paths (strings)
    valid_extensions (:obj:`list`, optional): only include these types of 
        files in contents value for each folder. Defaults to ["md", "docx", "doc", "txt", "rtf"]
  
  Returns:
    dict : {
        $folder-names : (dict) {
            name (str): base name of folder,
            path (str): absolute path to folder,
            size (int): number of items in folder,  
            contents list (list): all files in folders (not dirs),
            contents dict (dict): {
                $file-name (str): path
            }
        },
    }
  """

  if not valid_extensions:
    valid_extensions = [
        "md",
        "docx",
        "doc",
        "txt",
        "rtf"
    ]
  
  dir_output = {}
  for link in path_list:
    
    name_only = ntpath.basename(link)
    p = link.replace("\\", "/")
    if ".git" in p:
        continue
    contents = []
    for (dirPath, dirnames, filenames) in walk(p):
      contents.extend(filenames)
      break
    if not contents:
      continue

    contents_dict = {}
    for fi in contents:
        code = fi.split(".")[-1]
        if code in valid_extensions:
            contents_dict[fi] =  p.strip("/")+"/" + fi
    
    dir_output[name_only] = {
      "name" : name_only,
      "path" : p.strip("/")+"/",
      "contents list" : contents,
      "content dict" : contents_dict,
      "size" : len(contents)
    }

  return dir_output


def abs_to_rel(folder_tree):
    """
    Accepts path and removes base path.
    """
    base_path = os.getcwd().split("/")
    target_path = [_ for _ in folder_tree["path"].split("/") if _ not in base_path]
    return "/".join(target_path) + "/"


def main():
    category_option = sys.argv[1]

    recursive_dirs = (get_directories(os.getcwd()))
    dirs_dict = treeify_directory(recursive_dirs)
    target = abs_to_rel(dirs_dict[category_option])

    for guide in dirs_dict[category_option]["content dict"].keys():
        if len(sys.argv) > 2:
            if sys.argv[2].lower() not in guide.lower():
                continue 
        print(f"opening {guide} guide. . . ")
        guide_path = target + guide
        url = ROOT.format(guide_path)
        webbrowser.open(url)


if __name__ == "__main__":
    main()