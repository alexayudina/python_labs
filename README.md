# Лаборторная работа 4
## Задание A — модуль src/lab04/io_txt_csv.py
```python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
     try:
        return Path(path).read_text(encoding=encoding)
     except FileNotFoundError:
         return "Такого файла нету"
     except UnicodeDecodeError:
         return "Неудалось изменить кодировку"

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    with p.open('w', newline="", encoding="utf-8") as file: 
        f = csv.writer(file)
        if header is None and rows == []: 
            file_c.writerow(('a', 'b')) 
        if header is not None:
            f.writerow(header)
        if rows != []:
            const = len(rows[0])
            for i in rows:
                if len(i) != const:
                    return ValueError
        f.writerows(rows)

def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
 
print(read_text("scr/lab_4/data/input.txt"))
write_csv([("word","count"),("test",3)], "scr/lab_4/data/check.csv") 

```
<img width="1214" height="188" alt="привет мир" src="https://github.com/user-attachments/assets/9356f475-dfad-481b-8a27-7285f8d748b2" />
<img width="1254" height="254" alt="chek" src="https://github.com/user-attachments/assets/9ecc0895-ea43-4992-b84a-377138c9f136" />

## Задание B — скрипт src/lab04/text_report.py
```python
from io_txt_csv import read_text, write_csv, ensure_parent_dir
import sys
from pathlib import Path

sys.path.append('scr\lab_4\lib')

from text import normalize, tokenize, count_freq, top_n


def exist_path(path_f: str):
    return Path(path_f).exists()


def main(file: str, encoding: str = 'utf-8'):
    if not exist_path(file):
        raise FileNotFoundError
    
    file_path = Path(file)
    text = read_text(file, encoding=encoding)
    norm = normalize(text)
    tokens = tokenize(norm)
    freq_dict = count_freq(tokens)
    top = top_n(freq_dict, 5)
    top_sort = sorted(top, key=lambda x: (x[1], x[0]), reverse=True)
    report_path = file_path.parent / 'report.csv'
    write_csv(top_sort, report_path, header=('word', 'count'))
    
    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(freq_dict)}')
    print('Топ-5:')
    for cursor in top_sort:
        print(f'{cursor[0]}: {cursor[-1]}')


main('scr\lab_4\data\input.txt')
```
<img width="1168" height="242" alt="репорт" src="https://github.com/user-attachments/assets/60c3146c-a31f-4821-8f67-6f392429093e" />
<img width="1828" height="318" alt="конец" src="https://github.com/user-attachments/assets/8f07f0ef-4e4f-4d5d-804a-b782205f709c" />
