## Лабораторная работа 6
### cli_text.py
```python
import sys, os, argparse

from lib import stats_text

def cat_command(input_file: str, number_lines: bool = False):
    if not check_file(input_file):
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1): #строки нумируем
                if number_lines:# Если включена нумерация строк
                    print(f"{line_number:6d}  {line}", end='') # Вывод номера строки (шириной 6 символов) и содержимого строки
                else:
                    print(line, end='') # Простой вывод строки
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)

def check_file(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не существует", file=sys.stderr)
        return False
    if not os.path.isfile(file_path):
        print(f"Ошибка: '{file_path}' не является файлом", file=sys.stderr)
        return False

    return True

def stats_command(input_file: str, top_n: int = 5):
    if not check_file(input_file): #проверка файл сущ и доступен для чтения
        sys.exit(1)
    
    if top_n <= 0:
        print("Ошибка: значение --top должно быть положительным числом", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
            stats_text(text, top_n)

    except Exception as e: # Обработка исключений
        print(f"Ошибка при анализе файла: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Лабораторная №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True) #путь к файлу
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5) 

    args = parser.parse_args() #преобразует sys.argv в объект args
    #проверяет какую команду выбрал
    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
    else:

        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
```
### Вывод строк с номерами:
<img width="1012" height="139" alt="image01" src="https://github.com/user-attachments/assets/85278da2-6368-44d7-9afd-879765fdd2b6" />
### Вывод топ слов:
<img width="813" height="364" alt="image02" src="https://github.com/user-attachments/assets/c433b1ba-1368-4e62-a2d2-3ea1d9aa39e2" />


### cli_convert.py

```python
import sys, argparse

from lib import csv_to_xlsx
from lib import json_to_csv, csv_to_json
from ex1 import check_file


def cli_convert():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True) # Создание подпарсеров для разных команд
    
    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    
    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            if not check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)
                
            json_to_csv(args.input, args.output)
            print(f"Успешно: JSON -> CSV")
            
        elif args.cmd == "csv2json":
            if not check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)
                
            csv_to_json(args.input, args.output)
            print(f"Успешно: CSV -> JSON")
            
        elif args.cmd == "csv2xlsx":
            if not check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)
                
            csv_to_xlsx(args.input, args.output)
            print(f"Успешно: CSV -> XLSX")
            
        else:
            print("Ошибка: Неизвестная команда")
            sys.exit(1)
        return 0
        
    except Exception as e:
        print(f"Ошибка при конвертации: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(cli_convert())
```
### Вывод JSON -> CSV:
<img width="1356" height="77" alt="image03" src="https://github.com/user-attachments/assets/011ef1fa-972c-4102-a9d1-2d178b4ec798" />
<img width="405" height="287" alt="image04" src="https://github.com/user-attachments/assets/edf9b85e-4979-4091-b701-16cfb79485bc" />
<img width="343" height="143" alt="image05" src="https://github.com/user-attachments/assets/9e140b15-8979-49b6-89f7-c5a880009f38" />
### Вывод CSV -> JSON:
<img width="1333" height="92" alt="image06" src="https://github.com/user-attachments/assets/8ac9479a-5c78-41a9-a50e-d3f96968fbbf" />
### Вывод CSV -> XLSX:
<img width="1264" height="79" alt="image07" src="https://github.com/user-attachments/assets/ca978c5a-6540-42ef-9d5c-3abe67799a14" />
### Help:
<img width="764" height="205" alt="image08" src="https://github.com/user-attachments/assets/97815909-f46c-4ac0-b75e-6818628a7b8f" />
