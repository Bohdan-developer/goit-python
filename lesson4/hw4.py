# Домашнее задание
# Задача
# У многих на рабочем столе есть папка, которая называется как-то вроде "Разобрать".
#  Как правило, разобрать эту папку руки никогда так и не доходят.

# Мы с вами напишем скрипт, который разберет эту папку. В конечном итоге вы сможете 
# настроить эту программу под себя и она будет выполнять индивидуальный сценарий 
# соответствующий вашим нуждам. Для этого наше приложение будет проверять расширение 
# файла (последние символы в имени файла, как правило после точки) и в зависимости от 
# расширения принимать решение к какой категории отнести этот файл.

# Скрипт принимает один аргумент при запуске — это имя папки в которой он будет проводить 
# сортировку. Допустим файл с программой называется sort.py, тогда чтобы отсортировать 
# папку /user/Desktop/Хлам надо запустить скрипт командой python sort.py /user/Desktop/Хлам

# Критерии приёма задания#
# Для того, чтобы успешно справится с этим заданием вы должны вынести логику обработки папки 
# в отдельную функцию.
# Чтобы скрипт мог пройти на любую глубину вложенности функция обработки папок должна рекурсивно 
# вызывать сама себя когда ей встречаются вложенные папки.
# Скрипт должен проходить по указанной во время вызова папке и сортировать все файлы по группам:

# изображения ('JPEG', 'PNG', 'JPG', 'SVG');
# видео файлы ('AVI', 'MP4', 'MOV', 'MKV');
# документы ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
# музыка ('MP3', 'OGG', 'WAV', 'AMR');
# архивы ('ZIP', 'GZ', 'TAR');
# неизвестные расширения.
# Вы можете расширить и дополнить этот список если хотите.

# Скрипт выводит результаты работы в консоль.

# В результатах работы должны быть:

# Список файлов в каждой категории (музыка, видео, фото и пр.)
# Перечень всех известных скрипту расширений, которые встречаются в целевой папке.
# Перечень всех расширений, которые скрипту неизвестны.

import sys
import os

def main():
    path = sys.argv[1]
    print(f'Started in {path}')

    files = os.listdir(path)

    images_list = list()
    video_list = list()
    documents_list = list()
    music_list = list()
    no_category =  list()

    extensions = set()

    suffix_imeges = ".jpeg", ".png", ".jpg"
    suffix_videos = ".avi", ".mp4", ".mov"
    suffix_documents = ".doc", ".docx", ".txt"
    suffix_music = ".mp3", ".ogg", ".wav", ".amr"

    imeges = 0
    videos = 0
    documents = 0
    music = 0
    no_categories = 0

    try:
        for i in files:
            if i.endswith(suffix_imeges):
                images_list.append(i)
                imeges +=1
                extensions.add(i.split(".")[1])
            elif i.endswith(suffix_videos):
                videos +=1
                video_list.append(i)
                extensions.add(i.split(".")[1])
            elif i.endswith(suffix_documents):
                documents += 1
                documents_list.append(i)
                extensions.add(i.split(".")[1])
            elif i.endswith(suffix_music):
                music += 1
                music_list.append(i)
                extensions.add(i.split(".")[1])
            else:
                no_categories += 1
                no_category.append(i)
                extensions.add(i.split(".")[1])


        print()
        print(f'Found {imeges} file(-s) Images files')
        print('Filenames: ', end="") 
        print(*images_list, sep=", ")

        print()
        print(f'Found {videos} file(-s) Video files')
        print('Filenames: ', end="")
        print(*video_list, sep=", ")

        print()
        print(f'Found {documents} file(-s) Documents files')
        print('Filenames: ', end="")
        print(*documents_list, sep=", ")

        print()
        print(f'Found {music} file(-s) Music files')
        print('Filename: ', end="")
        print(*music_list, sep=", ")

        print()
        print(f'Found {no_categories} file(-s) No categories')
        print('Filenames: ', end="")
        print(*no_category, sep=", ")

        print()
        print(f"All file extensions: ", end="")
        print(*extensions, sep=", ")
    except Exception:
        print("File with no extension is in folder!")

if __name__=="__main__":
    main()