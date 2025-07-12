import csv

def dele_c():
    filename = "Contact.csv"

    # خواندن داده‌های موجود
    with open(filename, "r", newline="", encoding="utf-8") as file:
        data = list(csv.reader(file))

    name = input("Enter the name to delete: ")

    # فیلتر کردن داده‌ها و حذف ردیف مورد نظر
    filtered_data = [row for row in data if row and row[0] != name]

    # بازنویسی فایل بدون ردیف حذف‌شده
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(filtered_data)
    
    print(f"Contact with name '{name}' deleted (if it existed).")

dele_c()
