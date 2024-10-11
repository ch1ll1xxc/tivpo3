import unittest
import os
import shutil
from encryptor import FileEncryptor

class TestFileEncryptor(unittest.TestCase):
    def setUp(self):
        self.encryptor = FileEncryptor(shift=3)
        self.test_file = 'test_file.txt'
        self.encrypted_file = 'test_file.txt.encrypted'
        self.test_folder = 'test_folder'
        
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)
        
    def tearDown(self):
        for file in [self.test_file, self.encrypted_file]:
            if os.path.exists(file):
                os.remove(file)
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)
    
    def test_encrypt_file(self):
        original_content = 'Hello, World!'
        with open(self.test_file, 'w') as f:
            f.write(original_content)
        
        print(f"\nТест шифрования файла:")
        print(f"Исходное содержимое файла {self.test_file}: {original_content}")
        print("Пожалуйста, проверьте содержимое файла. Нажмите Enter для продолжения...")
        input()
        
        self.encryptor.encrypt_file(self.test_file)
        
        print(f"Файл зашифрован. Проверьте содержимое файла {self.encrypted_file}.")
        print("Нажмите Enter для завершения теста...")
        input()
        
        self.assertTrue(os.path.exists(self.encrypted_file))
        with open(self.encrypted_file, 'rb') as f:
            encrypted_content = f.read()
        
        self.assertNotEqual(encrypted_content, original_content.encode())

    def test_decrypt_file(self):
        original_content = 'Hello, World!'
        with open(self.test_file, 'w') as f:
            f.write(original_content)
        
        self.encryptor.encrypt_file(self.test_file)
        
        print(f"\nТест дешифрования файла:")
        print(f"Зашифрованный файл: {self.encrypted_file}")
        print("Пожалуйста, проверьте содержимое зашифрованного файла. Нажмите Enter для продолжения...")
        input()
        
        self.encryptor.decrypt_file(self.encrypted_file)
        
        decrypted_file = self.test_file
        with open(decrypted_file, 'r') as f:
            decrypted_content = f.read()
        
        print(f"Файл дешифрован. Проверьте содержимое файла {decrypted_file}.")
        print(f"Дешифрованное содержимое: {decrypted_content}")
        print("Нажмите Enter для завершения теста...")
        input()
        
        self.assertEqual(decrypted_content, original_content)

    def test_encrypt_folder(self):
        os.mkdir(self.test_folder)
        files_content = {'file1.txt': 'Hello', 'file2.txt': 'World'}
        for filename, content in files_content.items():
            with open(os.path.join(self.test_folder, filename), 'w') as f:
                f.write(content)
        
        print(f"\nТест шифрования папки:")
        print(f"Исходные файлы и содержимое: {files_content}")
        print(f"Проверьте содержимое папки {self.test_folder}.")
        print("Нажмите Enter для продолжения...")
        input()
        
        encrypted_files = self.encryptor.encrypt_folder(self.test_folder)
        
        print(f"Папка зашифрована. Проверьте содержимое папки {self.test_folder}.")
        print(f"Зашифрованные файлы: {encrypted_files}")
        print("Нажмите Enter для завершения теста...")
        input()
        
        self.assertEqual(len(encrypted_files), 2)
        self.assertTrue(all(file.endswith('.encrypted') for file in encrypted_files))
    
    def test_decrypt_folder(self):
        os.mkdir(self.test_folder)
        files_content = {'file1.txt': 'Hello', 'file2.txt': 'World'}
        for filename, content in files_content.items():
            with open(os.path.join(self.test_folder, filename), 'w') as f:
                f.write(content)
        
        self.encryptor.encrypt_folder(self.test_folder)
        
        print(f"\nТест дешифрования папки:")
        print(f"Зашифрованная папка: {self.test_folder}")
        print("Проверьте содержимое зашифрованной папки. Нажмите Enter для продолжения...")
        input()
        
        self.encryptor.decrypt_folder(self.test_folder)
        
        decrypted_files = os.listdir(self.test_folder)
        decrypted_content = {}
        for filename in decrypted_files:
            with open(os.path.join(self.test_folder, filename), 'r') as f:
                decrypted_content[filename] = f.read()
        
        print(f"Папка дешифрована. Проверьте содержимое папки {self.test_folder}.")
        print(f"Дешифрованные файлы и содержимое: {decrypted_content}")
        print("Нажмите Enter для завершения теста...")
        input()
        
        self.assertEqual(len(decrypted_files), 2)
        self.assertEqual(files_content, decrypted_content)

    def test_encrypt_empty_file(self):
        with open(self.test_file, 'w') as f:
            f.write('')
        
        print(f"\nТест шифрования пустого файла:")
        print(f"Создан пустой файл: {self.test_file}")
        print("Проверьте, что файл пустой. Нажмите Enter для продолжения...")
        input()
        
        self.encryptor.encrypt_file(self.test_file)
        
        print(f"Пустой файл зашифрован. Проверьте содержимое файла {self.encrypted_file}.")
        print("Нажмите Enter для завершения теста...")
        input()
        
        self.assertTrue(os.path.exists(self.encrypted_file))
        with open(self.encrypted_file, 'rb') as f:
            encrypted_content = f.read()
        
        self.assertEqual(encrypted_content, b'')

if __name__ == '__main__':
    unittest.main(verbosity=2)