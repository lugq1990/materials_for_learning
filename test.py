import os

def get_file_paths(folder_path):
  """
  This function reads a folder recursively and returns a list of file paths
  with the format "[folder1/folder2/.../filename.ext]".

  Args:
      folder_path: The path to the root folder to be scanned.

  Returns:
      A list of file paths in the desired format.
  """
  file_paths = []
  for root, _, files in os.walk(folder_path):
    if '.git' in root or '/' not in root:
        continue
    for file in files:
      relative_path = os.path.join(root.replace(folder_path, ""), file)

      file_paths.append(f"[{'.' + relative_path}]")  # Add "./" for clarity
  return file_paths

# Example usage
folder_path = os.path.abspath(os.curdir)
file_list = get_file_paths(folder_path)

for path in file_list:
  print(path)
