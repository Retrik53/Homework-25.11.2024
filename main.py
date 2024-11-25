import os

current_dir = os.getcwd()

file1_path = os.path.abspath(os.path.join(current_dir, 'data_path_1', 'test_file_1.txt'))
print(f"Абсолютный путь к файлу test_file_1.txt: {file1_path}")

for root, dirs, files in os.walk(current_dir):
    print(f'Путь: {root}')
    for dir in dirs:
        print(f'\tДиректория: {dir}')
    for file in files:
        print(f'\tФайл: {file}')

file3_path = os.path.join(current_dir, 'data_path_2', 'test_file_3.txt')
file3_abs_path = os.path.abspath(file3_path)
print(f"\nАбсолютный путь к файлу test_file_3.txt: {file3_abs_path}")

new_folder_name = "new_folder"
new_folder_path = os.path.join(current_dir, 'data_path_2', new_folder_name)
os.makedirs(new_folder_path, exist_ok=True)
print(f"\nНовая папка создана: {new_folder_path}")

if os.path.exists(new_folder_path):
    os.rmdir(new_folder_path)
    print(f"Папка удалена: {new_folder_path}")
else:
    print("Папка не найдена.")