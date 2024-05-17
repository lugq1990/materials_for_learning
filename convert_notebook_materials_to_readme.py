"""This func should be enhanced!"""
import os

def get_md_files_dict(directory):
    """
    This function will iteratively loop through the full current folder, with each folder will be a title as parent folder,
    iterative get each folder as sub-parent folder, for these folders are formated as markdown format.
    For the .md files should be a tuple, with .md file name as the first value, the .md file path as second value.
    
    The return value is a string that could used in markdown file.
    
    
    Parameters:
    directory (str): The directory to scan for MD files.
    """
    # Initialize an empty dictionary
    md_files_dict = {}
    markdown_str = ""
    seen_folder = set()

    # Iterate through all files in the given directory
    for root, dirs, files in os.walk(directory):
        if not dirs:
            folder_path = os.path.relpath(root)
            files = [x for x in files if x.endswith('.md')]
            if not files:
                continue
            root_path_name = root.split('/')[1]
            if root_path_name not in seen_folder:
                seen_folder.add(root_path_name)
                markdown_str += '\n## {}\n\n'.format(root_path_name)
            
            md_files_dict[folder_path] = files
            for i, f in enumerate(files):
                f_name = f.split('.')[0]
                file_path = os.path.join(folder_path, f)
                markdown_str += "[{}](./{})\n\n".format(file_path, file_path)
            
    return markdown_str

# Example usage:
directory_path = '.'
markdown_str = get_md_files_dict(directory_path)


markdown_prefix = """# materials_for_learning
Materials summary during daily learning

This repo is a daily learning path to enhance the ability of software engineering, including basic computer info, distributed, AI, cloud, python etcs.

For each folder is a sub-materials, will try to add a functionality that will match each of the folder of the content here, so that for later will get be easier to read. Some of them are based on LLM models output like ChatGPT.
"""


final_markdown = markdown_prefix + markdown_str

print(final_markdown)


with open('./README.md', 'w') as f:
    f.write(final_markdown)
