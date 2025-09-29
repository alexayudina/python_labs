# Лабораторная работа 1

## Задание 1
```bash
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
<img width="1544" height="828" alt="hi" src="https://github.com/user-attachments/assets/96ef6458-59a9-457e-ab52-558c0faa0b70" />

## Задание 2
```bash
a = (input("a:"))
b = (input("b:"))
a=a.replace(",",".",1)
b=b.replace(",",".",1)
a=float(a)
b=float(b)
print(f"sum={(a+b):.2f}; avg={((a+b)/2):.2f}")
```
<img width="1142" height="807" alt="sum" src="https://github.com/user-attachments/assets/55e18727-8f53-4412-bef7-6ed30d4f88e8" />

## Задание 3
```bash
price=int(input("price:"))
discount=int(input("discount:"))
vat=int(input("vat:"))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
<img width="1171" height="896" alt="discount" src="https://github.com/user-attachments/assets/9743294a-932b-4853-bae9-0b003febd015" />

## Задание 4
```bash
m = int(input("Минуты:"))
print(f"{m//60}:{m%60}")
```
<img width="1129" height="793" alt="min" src="https://github.com/user-attachments/assets/b68f5c8a-17c9-4dad-9fe8-da1e5953cd00" />

## Задание 5
```bash
fio = input("ФИО: ")
fio=fio.split()
print(fio)
print(f"Инициалы:{(fio[0][:1]).upper()}{(fio[1][:1]).upper()}{(fio[2][:1]).upper()}")
print(len(fio[0])+len(fio[2])+len(fio[1])+2)
```
<img width="1774" height="844" alt="fio" src="https://github.com/user-attachments/assets/1c8aa8ab-beeb-4839-ab86-001be3f61cb7" />
