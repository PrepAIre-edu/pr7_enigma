"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

import csv

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

total_math = 0
total_english = 0
total_python = 0

student_count = 0
best_student_name = ""
best_avg_score = 0

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    csv_reader = csv.reader(f, delimiter=',')

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

    for line in f:
        clean_line = line.strip()
        parts = clean_line.split(",")

        name = parts[0]
        math = float(parts[1])
        python = float(parts[2])
        english = float(parts[3])

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

        total_math += math
        total_english += english
        total_python += python
        student_count += 1

        current_avg = (math + english + python) / 3

        if current_avg > best_avg_score:
            best_avg_score = current_avg
            best_student_name = name

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)

total_math_avg = total_math / student_count
total_english_avg = total_english / student_count
total_python_avg = total_python / student_count


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("Середній бал по класу:\n")
    f.write(f"math: {total_math_avg:.1f}\n")
    f.write(f"python: {total_python_avg:.1f}\n")
    f.write(f"english: {total_english_avg:.1f}\n\n")
    f.write(f"Найкращий студент: {best_student_name} ({best_avg_score:.1f})")

print("Середній бал по класу:")
print(f"math: {total_math_avg:.1f}")
print(f"python: {total_python_avg:.1f}")
print(f"english: {total_english_avg:.1f}")
print(f"Найкращий студент: {best_student_name} ({best_avg_score:.1f})")
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
