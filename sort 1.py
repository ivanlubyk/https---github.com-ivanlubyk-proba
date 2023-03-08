import shutil
from pathlib import Path
import re

category = {
    "images": ['.jpeg', '.png', '.jpg', '.svg'],
    "audio": ['.mp3', '.ogg', '.wav', '.amr'],
    "video": ['.avi', '.mp4', '.mov', '.mkv'],
    "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "archives": ['.zip', '.gz', '.tar']
}


def create_cat_dirs(path: Path):
    for cat in category.keys():
        cat_dir = path / cat
        if not cat_dir.exists():
            cat_dir.mkdir()


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize_name(name: str):
    # TODO Зробити
    tranlation = name.translate(TRANS)
    for s in tranlation:
        done_rep = s.replace(' ', '_').replace('@', '_').replace('!', '_').replace('-', '_')\
            .replace('+', '_')
    return done_rep


def unpack_arch(arch: Path, target_dir: Path):
    arch_dir = target_dir / normalize_name(arch.name[0: -len(arch.suffix)])
    print(f"unpacking archive: {arch}, to: {arch_dir}")
    shutil.unpack_archive(arch, arch_dir)
    return arch_dir


def move_file(target_folder: Path, file: Path):
    extension = file.suffix.lower()
    for cat, extensions in category.items():
        if extension in extensions:
            if cat == "archives":
                return unpack_arch(file, target_folder / cat)
            else:
                to_file = target_folder / cat / normalize_name(file.name)
                print(f"moving file: {file}, to {to_file}")
                return file.replace(to_file)


def sort(path: Path):
    for file in path.rglob("*"):
        move_file(path, file)


if __name__ == "__main__":
    path = Path("D:\DZ")
    create_cat_dirs(path)
    sort(path)




