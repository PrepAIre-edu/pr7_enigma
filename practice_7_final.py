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

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    csv_reader = csv.reader(f, delimiter=',')

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:

    for line in f:
        clean_line = line.strip()
        parts = clean_line.split(",")

        name = parts[0]
        math = float(parts[1])
        python = float(parts[2])
        english = float(parts[3])

# TODO 3: по ходу циклу накопичуйте:

        total_math += math
        total_english += english
        total_python += python
        student_count += 1

        current_avg = (math + english + python) / 3

        if current_avg > best_avg_score:
            best_avg_score = current_avg
            best_student_name = name

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета

total_math_avg = total_math / student_count
total_english_avg = total_english / student_count
total_python_avg = total_python / student_count

# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат

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
