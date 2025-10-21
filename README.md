# Лабораторная работа 3
## Задание A — `src/lib/text.py`

1. `normalize`  
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t")) 
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
<img width="1324" height="880" alt="normalize" src="https://github.com/user-attachments/assets/1d2f92a2-8b93-4226-a7b1-84324cac8496" />


2. `tokenize`  
```
import re 
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)
# Используем регулярное выражение для поиска слов:
# \w+ - одна или более букв/цифр/подчеркивания
# (?:-\w+)* - ноль или более повторов: дефис + буквы/цифры/подчеркивания
# Это позволяет находить слова с дефисами внутри (например, "по-русски")
# re.findall возвращает все непересекающиеся совпадения с шаблоном
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
<img width="856" height="818" alt="tokenize" src="https://github.com/user-attachments/assets/7446f3eb-0fc3-43e1-866e-e9e36f1ebf14" />


3+4. `count_freq+top_n`  
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    c = {}  
    for w in tokens:
        cu = c.get(w, 0)
        c[w] = cu + 1
    return c
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    t = []
    for w, count in freq.items():
        t.append((-count, w))
    t.sort()
    result = []
    for neg_count, w in t:
        result.append((w, -neg_count))
    return result[:n]
tok = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tok)
print(top_n(freq, n=2))
tok_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_2 = count_freq(tok_2)
print(top_n(freq_2, n=2))
```
<img width="1206" height="1136" alt="count_freq+top_n" src="https://github.com/user-attachments/assets/413aab4a-02de-450a-bcc5-f9cc8b87565b" />


## Задание B — `src/text_stats.py`

`src/text_stats`
```
from lib.text import normalize, tokenize, count_freq, top_n
import sys
def main():
    text = sys.stdin.buffer.read().decode('utf-8')
    if not text.strip():
        print("Нет входных данных")
        return
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    

    if not tokens:
        print("В тексте не найдено слов")
        return

    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":  
    main()
```

<img width="1128" height="1208" alt="text_stats" src="https://github.com/user-attachments/assets/66b6128b-4a42-44ac-ae03-6c6456c1c92c" />

<img width="1128" height="160" alt="text" src="https://github.com/user-attachments/assets/b6098f7d-98c1-4489-bb6a-ed168fc54cf1" />
