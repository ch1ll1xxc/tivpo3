import argparse
from encryptor import FileEncryptor

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files in a folder')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform')
    parser.add_argument('folder', help='Folder to process')
    parser.add_argument('--shift', type=int, default=3, help='Shift value for encryption/decryption (default: 3)')
    
    args = parser.parse_args()
    
    encryptor = FileEncryptor(args.shift)
    
    if args.action == 'encrypt':
        encryptor.encrypt_folder(args.folder)
        print(f"Folder '{args.folder}' encrypted successfully.")
    else:
        encryptor.decrypt_folder(args.folder)
        print(f"Folder '{args.folder}' decrypted successfully.")

if __name__ == '__main__':
    main()