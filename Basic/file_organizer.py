import os
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Colors:
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'

folders = {
    "Pictures": ['png', 'jpg', 'jpeg', 'jfif', 'bmp', 'gif', 'tiff', 'svg', 'webp', 'raw', 'heic'],
    "Videos": ['mp4', 'mkv', 'flv', 'avi', 'mov', 'wmv', 'webm', 'mpeg', 'mpg', '3gp', 'flv', 'rmvb'],
    "Java Libraries": ['jar', 'aar', 'class', 'war', 'ear'],
    "Fonts": ['ttf', 'otf', 'woff', 'woff2', 'eot'],
    "Apps": ['aia', 'apk', 'ipa', 'xap'],
    "Extensions": ['aix', 'nix', 'deb', 'rpm'],
    "Documents": ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'txt', 'csv', 'odt', 'epub', 'mobi', 'rtf', 'ps', 'tex'],
    "Compressed": ['zip', 'rar', 'tar', 'gz', '7z', 'bz2', 'xz', 'lzma', 'iso'],
    "Audio": ['mp3', 'wav', 'aac', 'flac', 'm4a', 'wma', 'ogg', 'aiff', 'alac'],
    "Scripts": ['py', 'sh', 'bat', 'js', 'pl', 'rb', 'php', 'ts', 'go'],
    "Web Files": ['html', 'css', 'js', 'php', 'xml', 'json', 'svg', 'asp', 'jsp'],
    "Code": ['java', 'cpp', 'c', 'h', 'cs', 'go', 'rs', 'swift', 'kt', 'py', 'ts', 'lua', 'm', 'vb', 'html', 'scss', 'yaml'],
    "Spreadsheets": ['xls', 'xlsx', 'ods', 'csv', 'xlsm'],
    "Presentations": ['ppt', 'pptx', 'key', 'odp', 'sxi'],
    "Database": ['sql', 'db', 'sqlite', 'mdb', 'accdb', 'json', 'yaml'],
    "Log Files": ['log', 'err', 'trace', 'out'],
    "E-books": ['epub', 'mobi', 'azw3', 'pdf', 'lit', 'cbz', 'fb2'],
    "Archives": ['zip', 'rar', 'tar', 'gz', '7z', 'bz2', 'xz', 'tar.gz'],
    "Installers": ['exe', 'msi', 'dmg', 'pkg', 'bat'],
    "Temporary": ['tmp', 'temp', 'swp'],
    "Markdown": ['md', 'markdown', 'rst', 'txt'],
    "Executables": ['exe', 'bin', 'app', 'com', 'msi'],
    "Configurations": ['conf', 'cfg', 'ini', 'json', 'xml'],
    "Templates": ['dotx', 'dotm', 'otd', 'xltx'],
    "3D Models": ['obj', 'stl', 'fbx', 'dae', 'blend', 'max'],
    "Animations": ['anim', 'blend', 'bvh', 'x', 'fbx'],
    "CAD Files": ['dwg', 'dxf', 'iges', 'step', 'stp'],
    "System Files": ['sys', 'dll', 'drv', 'vxd', 'ocx'],
    "Project Files": ['proj', 'sln', 'xcodeproj', 'vcxproj', 'androidproj'],
    "Email": ['eml', 'msg', 'pst'],
    "Source Control": ['git', 'svn', 'hg', 'bzr'],
    "Certificates": ['crt', 'pem', 'key', 'cer', 'csr'],
    "Scripts Executable": ['exe', 'bat', 'sh', 'jar'],
    "Cloud Files": ['csv', 'json', 'xml', 'yaml'],
    "Package Managers": ['npm', 'gem', 'pip', 'composer', 'yarn', 'cargo'],
    "Network Files": ['pcap', 'log', 'net', 'cap'],
    "Firmware": ['bin', 'hex', 'img'],
    "Virtual Machines": ['vmdk', 'vhd', 'vdi', 'iso'],
    "Backup": ['bak', 'bkp', 'swp', 'tmp'],
    "Logs": ['log', 'out', 'txt', 'err', 'trace'],
    "Machine Learning": ['pkl', 'h5', 'model'],
    "Web Design": ['psd', 'ai', 'xd', 'sketch'],
    "GIS": ['shp', 'geojson', 'kml'],
}

def create_and_move_files(base_dir):
    if not os.path.exists(base_dir):
        logging.error(f"{Colors.ERROR}Directory {base_dir} does not exist!{Colors.RESET}")
        return
    
    files_found = {folder: False for folder in folders}

    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)

        if os.path.isfile(item_path):
            file_extension = item.split('.')[-1].lower()

            moved = False
            for folder_name, extensions in folders.items():
                if file_extension in extensions:
                    files_found[folder_name] = True
                    target_folder = os.path.join(base_dir, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder, exist_ok=True)
                        logging.info(f"{Colors.INFO}Created folder: {folder_name}{Colors.RESET}")
                    
                    target_file_path = os.path.join(target_folder, item)

                    if os.path.exists(target_file_path):
                        try:
                            shutil.copy(item_path, target_file_path)
                            logging.info(f"{Colors.WARNING}File {item} already exists. Merged into {folder_name}{Colors.RESET}")
                        except Exception as e:
                            logging.error(f"{Colors.ERROR}Error merging {item} into {folder_name}: {e}{Colors.RESET}")
                    else:
                        try:
                            shutil.move(item_path, target_folder)
                            logging.info(f"{Colors.SUCCESS}Moved {item} to {folder_name}{Colors.RESET}")
                        except Exception as e:
                            logging.error(f"{Colors.ERROR}Error moving {item} to {folder_name}: {e}{Colors.RESET}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(base_dir, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder, exist_ok=True)
                try:
                    shutil.move(item_path, other_folder)
                    logging.info(f"{Colors.SUCCESS}Moved {item} to Others{Colors.RESET}")
                except Exception as e:
                    logging.error(f"{Colors.ERROR}Error moving {item} to Others: {e}{Colors.RESET}")

    for folder_name, found in files_found.items():
        if not found:
            folder_path = os.path.join(base_dir, folder_name)
            if os.path.exists(folder_path):
                try:
                    if not os.listdir(folder_path):
                        os.rmdir(folder_path)
                        logging.info(f"{Colors.INFO}Deleted empty folder: {folder_name}{Colors.RESET}")
                except Exception as e:
                    logging.error(f"{Colors.ERROR}Error deleting empty folder {folder_name}: {e}{Colors.RESET}")

def main():
    base_directory = input(f"{Colors.INFO}Enter the path of the directory you want to organize: {Colors.RESET}")
    create_and_move_files(base_directory)

if __name__ == "__main__":
    main()
