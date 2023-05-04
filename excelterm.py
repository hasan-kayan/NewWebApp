import os
import shutil

source_folder = r"C:\Users\hasan.kayan\Desktop\excel"
destination_folder = r"C:\Users\hasan.kayan\Desktop\new"

# Klasördeki Excel dosyalarını al
excel_files = [file for file in os.listdir(source_folder) if file.endswith('.xlsx')]

for file in excel_files:
    # Dosya adını al ve yıla göre kategorize et
    filename = os.path.splitext(file)[0]
    year = int(filename.split()[-1])
    decade = year - (year % 10)
    period = str(decade) + " - " + str(decade + 9)
    # Kategoriyi oluştur
    category_path = os.path.join(destination_folder, period)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    # Dosyayı yeni kategoriye taşı
    source_file_path = os.path.join(source_folder, file)
    destination_file_path = os.path.join(category_path, file)
    shutil.move(source_file_path, destination_file_path)
