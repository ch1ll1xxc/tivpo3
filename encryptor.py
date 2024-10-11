import os

class FileEncryptor:
    def __init__(self, shift):
        self.shift = shift
    
    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
        
        encrypted_content = bytes([(byte + self.shift) % 256 for byte in content])
        
        encrypted_file_path = file_path + '.encrypted'
        with open(encrypted_file_path, 'wb') as f:
            f.write(encrypted_content)
        
        return encrypted_file_path
    
    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
        
        decrypted_content = bytes([(byte - self.shift) % 256 for byte in content])
        
        decrypted_file_path = file_path[:-10]  # Удаляем '.encrypted'
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_content)
        
        # Удаляем зашифрованный файл после дешифрования
        os.remove(file_path)
    
    def encrypt_folder(self, folder_path):
        encrypted_files = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not file_path.endswith('.encrypted'):
                    encrypted_file = self.encrypt_file(file_path)
                    encrypted_files.append(encrypted_file)
        return encrypted_files
    
    def decrypt_folder(self, folder_path):
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith('.encrypted'):
                    self.decrypt_file(file_path)