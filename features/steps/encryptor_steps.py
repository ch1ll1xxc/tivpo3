import os
import shutil
from behave import given, when, then
from encryptor import FileEncryptor

@given('файл "{file_name}" с содержимым "{content}"')
def step_impl(context, file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

@when('я шифрую файл "{file_name}"')
def step_impl(context, file_name):
    encryptor = FileEncryptor(shift=3)
    encryptor.encrypt_file(file_name)

@then('создается файл "{file_name}"')
def step_impl(context, file_name):
    assert os.path.exists(file_name), f"Файл {file_name} не создан"

@then('содержимое файла "{file_name}" не равно "{content}"')
def step_impl(context, file_name, content):
    with open(file_name, 'r') as f:
        file_content = f.read()
    assert file_content != content, f"Содержимое файла {file_name} не изменилось после шифрования"

@given('зашифрованный файл "{file_name}"')
def step_impl(context, file_name):
    # Предполагаем, что файл уже зашифрован в предыдущем сценарии
    assert os.path.exists(file_name), f"Зашифрованный файл {file_name} не найден"

@when('я дешифрую файл "{file_name}"')
def step_impl(context, file_name):
    encryptor = FileEncryptor(shift=3)
    encryptor.decrypt_file(file_name)

@then('содержимое файла "{file_name}" равно "{content}"')
def step_impl(context, file_name, content):
    with open(file_name, 'r') as f:
        file_content = f.read()
    assert file_content == content, f"Содержимое файла {file_name} не соответствует ожидаемому"

@given('папка "{folder_name}" с файлами')
def step_impl(context, folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    os.makedirs(folder_name, exist_ok=True)
    for row in context.table:
        file_path = os.path.join(folder_name, row['имя_файла'])
        with open(file_path, 'w') as f:
            f.write(row['содержимое'])

@when('я шифрую папку "{folder_name}"')
def step_impl(context, folder_name):
    encryptor = FileEncryptor(shift=3)
    context.encrypted_files = encryptor.encrypt_folder(folder_name)

@then('создаются файлы')
def step_impl(context):
    for row in context.table:
        file_path = row['имя_файла']
        full_path = os.path.join('test_folder', file_path)
        assert os.path.exists(full_path), f"Файл {file_path} не создан"

@given('зашифрованная папка "{folder_name}" с файлами')
def step_impl(context, folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    os.makedirs(folder_name, exist_ok=True)
    for row in context.table:
        file_path = os.path.join(folder_name, row['имя_файла'])
        with open(file_path, 'w') as f:
            f.write('Encrypted content')  # Просто заглушка для зашифрованного содержимого

@when('я дешифрую папку "{folder_name}"')
def step_impl(context, folder_name):
    encryptor = FileEncryptor(shift=3)
    encryptor.decrypt_folder(folder_name)

# Очистка после каждого сценария
def after_scenario(context, scenario):
    if os.path.exists('test_folder'):
        shutil.rmtree('test_folder')
    if os.path.exists('test_file.txt'):
        os.remove('test_file.txt')
    if os.path.exists('test_file.txt.encrypted'):
        os.remove('test_file.txt.encrypted')
    if os.path.exists('empty_file.txt'):
        os.remove('empty_file.txt')
    if os.path.exists('empty_file.txt.encrypted'):
        os.remove('empty_file.txt.encrypted')

@given('пустой файл "{file_name}"')
def step_impl(context, file_name):
    with open(file_name, 'w') as f:
        pass

@then('содержимое файла "{file_name}" пустое')
def step_impl(context, file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    assert content == '', f"Файл {file_name} не пустой"

# Очистка после каждого сценария
def after_scenario(context, scenario):
    # ... существующий код ...
    if os.path.exists('empty_file.txt'):
        os.remove('empty_file.txt')
    if os.path.exists('empty_file.txt.encrypted'):
        os.remove('empty_file.txt.encrypted')