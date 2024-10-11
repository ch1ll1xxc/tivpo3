# language: ru
Функция: Шифрование и дешифрование файлов

  Сценарий: Шифрование одного файла
    Дано файл "test_file.txt" с содержимым "Hello, World!"
    Когда я шифрую файл "test_file.txt"
    Тогда создается файл "test_file.txt.encrypted"
    И содержимое файла "test_file.txt.encrypted" не равно "Hello, World!"

  Сценарий: Дешифрование одного файла
    Дано зашифрованный файл "test_file.txt.encrypted"
    Когда я дешифрую файл "test_file.txt.encrypted"
    Тогда создается файл "test_file.txt"
    И содержимое файла "test_file.txt" равно "Hello, World!"

  Сценарий: Шифрование папки
    Дано папка "test_folder" с файлами:
      | имя_файла   | содержимое |
      | file1.txt   | Hello      |
      | file2.txt   | World      |
    Когда я шифрую папку "test_folder"
    Тогда создаются файлы:
      | имя_файла           |
      | file1.txt.encrypted |
      | file2.txt.encrypted |

  Сценарий: Дешифрование папки
    Дано зашифрованная папка "test_folder" с файлами:
      | имя_файла           |
      | file1.txt.encrypted |
      | file2.txt.encrypted |
    Когда я дешифрую папку "test_folder"
    Тогда создаются файлы:
      | имя_файла | содержимое |
      | file1.txt | Hello      |
      | file2.txt | World      |

  Сценарий: Шифрование пустого файла
    Дано пустой файл "empty_file.txt"
    Когда я шифрую файл "empty_file.txt"
    Тогда создается файл "empty_file.txt.encrypted"
    И содержимое файла "empty_file.txt.encrypted" пустое