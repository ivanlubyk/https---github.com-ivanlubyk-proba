import shutil
from pathlib import Path
import re
import sys

category = {
    "images": ['.jpeg', '.png', '.jpg', '.svg'],
    "audio": ['.mp3', '.ogg', '.wav', '.amr'],
    "video": ['.avi', '.mp4', '.mov', '.mkv'],
    "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "archives": ['.zip', '.gz', '.tar'],
    "unknown": []
}


def create_cat_dirs(path: Path):
    for cat in category.keys():
        cat_dir = path / cat
        if not cat_dir.exists():
            cat_dir.mkdir()


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
BAD_SYMBOLS = (" ", "@", "!", "-", "+")

TRANS = {}

for c, l in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

for symbol in BAD_SYMBOLS:
    TRANS[ord(symbol)] = "_"


def normalize_name(name: str):
    # TODO
    tranlation = name.translate(TRANS)
    return name.translate(TRANS)


def unpack_arch(arch: Path, target_dir: Path):
    arch_dir = target_dir / normalize_name(arch.name[0: -len(arch.suffix)])
    print(f"unpacking archive: {arch}, to: {arch_dir}")
    shutil.unpack_archive(arch, arch_dir)
    return arch_dir


def move_file(target_folder: Path, file: Path):
    extension = file.suffix.lower()
    is_moved = False
    for cat, extensions in category.items():
        new_place: Path = None
        if extension in extensions:
            to_file = target_folder / cat / normalize_name(file.name)
            print(f"moving file: {file}, to {to_file}")
            new_place = file.replace(to_file)
            is_moved = True
        if cat == "archives" and new_place:
            unpack_arch(new_place, target_folder / cat/ new_place.stem)
    if not is_moved:
        file.replace(target_folder / 'unknown' / normalize_name(file.name))

        


def sort(path: Path):
    for file in path.rglob("**/*.*"):
        move_file(path, file)
        
def main():
    try:
        path = Path(r"d:\testfolder") #Path(sys.argv[1])
    except IndexError:
        print("Sorry, must be parameter - path to folder")
        return None

    if not path.exists():
        print(f"The folder - {path} dos't exist")
        return None
    
    create_cat_dirs(path)
    sort(path)


if __name__ == "__main__":
    main()


