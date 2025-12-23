import json
from typing import List
from lab_8.models import Student

def students_to_json(students: List[Student], path: str) -> None:

    data = [student.to_dict() for student in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = []
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при создании студента из данных {item}: {e}")
                continue
                
        return students
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON из файла {path}")
        return []

# if __name__ == "__main__":
students = [
    Student("Иванов Иван", "2000-05-15", "SE-01", 4.5),
    Student("Петрова Анна", "2001-08-22", "SE-02", 3.8),
    Student("Сидоров Алексей", "1999-12-10", "SE-01", 4.2)
]
    
