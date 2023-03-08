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
# for i in path.iterdir():
#         if i.is_dir():
#             nimesil(i)
#         else:
#             names.append(i)
#     return namesif s.suffix in audios:
# #             os.path.join(s, new_audios

def move_file(target_folder:Path, file: Path):
    extension = file.suffix.lower()
    for cat, extensions in category.items():
        if extension in extensions:
            return file.replace(target_folder / cat / file.name)
    return file.replace(target_folder / file.name)

def sort(path : Path):
    # dir_list = []
    # file_list = []
    # list_dir(path, file_list, dir_list)
    # cat_dirs = create_cat_dirs(path)
    # for file in file_list:
    #     if file.suffix in category["images"]:
    for file in path.glob('**/*.*'):
        move_file(path, file)
            

    # for d in dir_list:
    #     if d.is_dir():
    #         sotr(b)
    #     else:
    #         names.append(i)

# def list_dir(path:Path, files: [], dirs: []):
#     for p in path.iterdir():
#         if p.is_dir() and p.name not in category.keys():
#             dirs.append(p)
#         elif p.is_file():
#             files.append(p)


def create_cat_dirs(path:Path):
    dirs = {}
    for cat in category.keys():
        # cat_dir = Path(path, cat)
        cat_dir = path / cat
        if not cat_dir.exists():
            cat_dir.mkdir()
            dirs[cat] = cat_dir
    return dirs


# sort(Path('D:\DZ'))

if __name__ == '__main__':
    path = Path(r'D:\DZ')
    create_cat_dirs(path)
    sort(path)
