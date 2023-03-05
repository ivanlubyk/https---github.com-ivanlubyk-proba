import os
import shutil
from pathlib import Path

category = {
    "images": ['.jpeg', '.png', '.jpg', '.svg'],
    "video": ['.avi', '.mp4', '.mov', '.mkv'],
    "audio": ['.mp3', '.ogg', '.wav', '.amr'],
    "document": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "archives": ['.zip', '.gz', '.tar']
}

def move_file(target_folder:Path, file: Path):
    
    extension = file.suffix.lower()
    for cat, extensions in category.items():
        if extension in extensions:
            return file.replace(target_folder / cat / file.name)
    return file.replace(target_folder / file.name)

def sort(path : Path):

    for file in path.glob('**/*.*'):
        move_file(path, file)
            




def create_cat_dirs(path:Path):
    dirs = {}
    for cat in category.keys():
        # cat_dir = Path(path, cat)
        cat_dir = path / cat
        if not cat_dir.exists():
            cat_dir.mkdir()
            dirs[cat] = cat_dir
    return dirs



if __name__ == '__main__':
    path = Path(r'D:\DZ')
    create_cat_dirs(path)
    sort(path)
