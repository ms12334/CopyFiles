import sys

def copyfiles(src_folder,dst_folder,file_ext):
    import os
    import shutil
    
    FILE_EXT = file_ext
    root_src_path = os.path.join('.',src_folder)
    root_dst_path = os.path.join('.',dst_folder)

    for dirpath, dirnames, filenames in os.walk(root_src_path):
        dst_path = dirpath.replace(root_src_path, root_dst_path)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        for file in filenames:
            src_file = os.path.join(dirpath, file)
            dst_file = os.path.join(dst_path, file)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            if file.endswith(FILE_EXT):
                shutil.copy(src_file, dst_file)

    # Remove empty folders
    for dirpath, dirnames, filenames in os.walk(root_dst_path):
        if len(dirnames) == 0 and len(filenames) == 0 :
            os.rmdir(dirpath)

if __name__ == '__main__':
    copyfiles(*sys.argv[1:])

