import csv
from pathlib import Path
from typing import List
from lab_8.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
    
    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write('fio,birthdate,group,gpa\n')
    
    def _read_all(self) -> List[dict]:
        self._ensure_storage_exists()
        with open(self.path, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    
    def _write_all(self, students: List[dict]):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(students)
    
    def list(self) -> List[Student]:
        return [
            Student(row['fio'], row['birthdate'], row['group'], float(row['gpa']))
            for row in self._read_all()
        ]
    
    def add(self, student: Student):
        rows = self._read_all()
        if any(row['fio'] == student.fio for row in rows):
            raise ValueError(f"Студент {student.fio} уже существует")
        rows.append({
            'fio': student.fio,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': str(student.gpa)
        })
        self._write_all(rows)
        print(f"Студент {student.fio} добавлен")
    
    def find(self, substr: str) -> List[Student]:
        return [s for s in self.list() if substr.lower() in s.fio.lower()]
    
    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        filtered = [r for r in rows if r['fio'] != fio]
        if len(filtered) != len(rows):
            self._write_all(filtered)
            print(f"Студент {fio} удален")
            return True
        print(f"Студент {fio} не найден")
        return False
    
    def update(self, old_fio: str, new_fio: str = None, **fields) -> bool:
        rows = self._read_all()
        updated = False
    
        for row in rows:
            if row['fio'] == old_fio:
                # Если передано новое ФИО - обновляем его
                if new_fio:
                    row['fio'] = str(new_fio)
            
                # Обновляем остальные поля
                for key, value in fields.items():
                    if key == 'birthdate' and hasattr(value, 'strftime'):
                        row[key] = value.strftime('%Y-%m-%d')
                    else:
                        row[key] = str(value)
            
                updated = True
                break
    
        if updated:
            self._write_all(rows)
            print(f"Данные студента '{old_fio}' обновлены")
        else:
            print(f"Студент '{old_fio}' не найден")
    
        return updated
    
    def stats(self) -> dict:
        students = self.list()
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [s.gpa for s in students]
        
        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups,
            "top_5_students": [
                {"fio": s.fio, "gpa": s.gpa} 
                for s in sorted(students, key=lambda x: x.gpa, reverse=True)[:5]
            ]
        }
    
    def print_stats(self):
        """Красиво выводит статистику по студентам"""
        stats = self.stats()
        
        print("\n" + "="*50)
        print("СТАТИСТИКА ПО СТУДЕНТАМ".center(50))
        print("="*50)
        
        print(f"Всего студентов: {stats['count']}")
        print(f"Минимальный GPA: {stats['min_gpa']:.2f}")
        print(f"Максимальный GPA: {stats['max_gpa']:.2f}")
        print(f"Средний GPA: {stats['avg_gpa']:.2f}")
        
        if stats['groups']:
            print("\nРаспределение по группам:")
            for group_name, count in stats['groups'].items():
                print(f"  {group_name}: {count} студентов")
        
        if stats['top_5_students']:
            print("\nТоп-5 студентов по успеваемости:")
            for i, student in enumerate(stats['top_5_students'], 1):
                print(f"  {i}. {student['fio']} - GPA: {student['gpa']:.2f}")
        print("="*50)
if __name__ == "__main__":
    group = Group("data/lab09/students.csv")
    
    student = Student("Юдина Александра", "2007-06-25", "БИВТ25-5", 2.0)
    
    # print("1. Добавление студента...")
    # group.add(student)
    
    # print("\n2. Все студенты:")
    # for s in group.list():
    #     print(f"{s.fio}, {s.group}, GPA: {s.gpa}")
    
    # print("\n3. Поиск 'Peter':")
    # results = group.find("Peter")
    # for r in results:
    #     print(f"  Найден: {r.fio}")
    
    # print("\n4. Обновление данных")
    # group.update("Юдина Александра",new_fio="Иванов Иван", gpa=5.0)
    
    # print("\n5. Удаление студента...")
    # group.remove("Иванов Иван")

    # print("\n6. Статистика:")
    # group.print_stats()
    