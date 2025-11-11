## Лабораторная работа 5
### Задание A — JSON ↔ CSV
```python
import csv, json, sys, os 
from pathlib import Path 

def right_json(path: str)-> bool: # Функция проверки что файл имеет расширение .json
    path=Path(path)
    if path.suffix.lower() != ".json":  # Проверяем расширение файла (приводим к нижнему регистру)
        return False

def right_csv(path: str)-> bool:  # Функция проверки что файл имеет расширение .csv
    path=Path(path)
    if path.suffix.lower() != ".csv":
        return False
    
def is_valid_json_file(file_path: str) -> bool: # Функция проверки валидности JSON файла
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0: # Проверяем что файл существует и не пустой
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)  # Загружаем и парсим JSON данные из файла
            return isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(item, dict) for item in json_data) #все элементы в списке являются словарями
    except:
        return False

def is_valid_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
            
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  # Создаем объект reader для чтения CSV файла построчно
            header = next(reader, None) # Читаем первую строку (заголовок) из CSV файла
            return header is not None and len(header) > 0
    except:
        return False

def json_to_csv(json_path: str, csv_path: str) -> None:
    if not is_valid_json_file(json_path): # Проверяем валидность CSV файла с помощью нашей функции
        print("ValueError: Input file is not a valid JSON or is empty")
        sys.exit(1) # Завершаем программу с кодом ошибки 1

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file) # loads - из строки JSON в Python-объект 

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys()) # Создаем объект DictWriter для записи словарей в CSV
        writer.writeheader()  # Записываем заголовок в CSV файл
        writer.writerows(json_data) # Записываем все данные из json_data в CSV файл построчно

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not is_valid_csv_file(csv_path):
        print("ValueError: Input file is not a valid CSV or is empty")
        sys.exit(1)

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Создаем объект DictReader для чтения CSV в виде словарей
        data = list(reader) # Читаем все строки и преобразуем в список словарей
    # dump - из Python-объекта в файл JSON
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4) #разрешаем Unicode символы м красиво форматирум с отпступом 4 пробела
csv_to_json(r"C:\Users\Sanek\Documents\GitHub\python_labs\scr\lab_5\data\samples\people.csv",r"C:\Users\Sanek\Documents\GitHub\python_labs\scr\lab_5\data\out\people_from_csv.json")

json_to_csv( r"C:\Users\Sanek\Documents\GitHub\python_labs\scr\lab_5\data\samples\people.json",  r"C:\Users\Sanek\Documents\GitHub\python_labs\scr\lab_5\data\out\people_from_json.csv")
```
<img width="640" height="162" alt="im1" src="https://github.com/user-attachments/assets/cba28a17-e400-4962-890d-a12534870ffa" />
<img width="696" height="504" alt="im2" src="https://github.com/user-attachments/assets/54896db7-1a13-4c0d-9a62-00ac6e4fe7fe" />
<img width="668" height="150" alt="im3" src="https://github.com/user-attachments/assets/4f872dc9-594a-4e9b-89da-b2b493978752" />
<img width="676" height="204" alt="im4" src="https://github.com/user-attachments/assets/22c6765e-046a-4291-9fe0-cdb0001f3974" />


### Задание B — CSV → XLSX

```python
import os
import csv
import sys
from pathlib import Path

from openpyxl import Workbook #из библиотеки openpyx1 импортирует только класс Workbook для создаия Excel файлов

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None: #функция конвертанции CSV в XLSX
    if not os.path.exists(csv_path): #если не существует файл по указанному пути, то 
        print("FileNotFoundError") #выводит сообщение об ошибке
        sys.exit(1) #завершает программу с кодом ошибки 1
    xlsx_path=Path(xlsx_path)
    csv_path=Path(csv_path)
    if xlsx_path.suffix.lower() != ".xlsx":
        raise ValueError(f"Неверный формат выходного файла: ожидается .xlsx")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    if os.path.getsize(csv_path) == 0: #получает размер в байтах и проверяет не равен ли он 0 (пустой файл) 
        print("ValueError")
        sys.exit(1)
    wb = Workbook() #создаем новую Excel книгу
    ws = wb.active #берем первый лист 
    ws.title = "Sheet1" #переменовываем лист в Sheet1

    with open(csv_path, "r", encoding="utf-8") as csv_file: #безопасно открывае файл для прочтения(автомвтически закрывает после использовния #csv_path - путь к файлу
        reader = csv.reader(csv_file) #создает объект для чтения CSV файла
        for row in reader: #перебирает каждую строку в CSV файле, row - переменная, содержащая данные одной строки(как список)
            ws.append(row) #добавляет строку данных в Excel лист

#Настройка ширины колонок
    for column_cells in ws.columns: #перебирает содержания ячейки одной колонки и возвращает все колонки листа 
        max_length = 0 #создает переменную для хранения максимальной длины теста в колонке 
        column_letter = column_cells[0].column_letter #присваивает букву колонки
        for cell in column_cells: #перебирает все ячейки в текущей колонке
            if cell.value: #проверяет есть ли значение в ячейки(не пустая)
                max_length = max(max_length, len(str(cell.value))) #обновляет длину строкиб сравнивая прошлое значение с настоящим 
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8) #обращается к настройкам ширины конкретной колонки, устанавливает ширину колонки, максимальная длина + 2 символа для отступа, 8- выбирает большее значение между расчитанной шириной и минимальной шириной 8 
    wb.save(xlsx_path) #сохраняет Excel книгу по указанному пути
csv_to_xlsx(r"C:\Users\Sanek\Documents\GitHub\python_labs\scr\lab_5\data\samples\cities.csv", r"C:\Users\Sanek\Documents\GitHub\python_labs\scr\lab_5\data\out\people.xlsx")      
```
<img width="696" height="194" alt="im5" src="https://github.com/user-attachments/assets/6fa1bd41-483a-4680-95d8-08eec05a0e77" />
<img width="618" height="190" alt="im6" src="https://github.com/user-attachments/assets/a58c1e6b-dcf2-438d-add1-57a63241f12d" />


