import sys
import os
import shutil

def main():
    p = sys.argv[1]
    
    print(f'Started in {p}')
    
    images_list = list()
    video_list = list()
    documents_list = list()
    music_list = list()
    archives_list =  list()


    suffix_imeges = ".jpeg", ".png", ".jpg"
    suffix_videos = ".avi", ".mp4", ".mov"
    suffix_documents = ".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"
    suffix_music = ".mp3", ".ogg", ".wav", ".amr"
    suffix_archiv = ".zip", ".tar", ".gztar", ".bztar", ".xztar"

    ignor = "archives", "images", "music", "videos", "documents"


    def normalize(p):

        alphabet = {ord('А'): 'A',
                    ord('Б'): 'B',
                    ord('В'): 'V',
                    ord('Г'): 'G',
                    ord('Д'): 'D',
                    ord('Е'): 'E',
                    ord('Ё'): 'Je',
                    ord('Ж'): 'Zh',
                    ord('З'): 'Z',
                    ord('И'): 'I',
                    ord('Й'): 'Y',
                    ord('К'): 'K',
                    ord('Л'): 'L',
                    ord('М'): 'M',
                    ord('Н'): 'N',
                    ord('П'): 'P',
                    ord('Р'): 'R',
                    ord('С'): 'S',
                    ord('Т'): 'T',
                    ord('У'): 'U',
                    ord('Ф'): 'F',
                    ord('Х'): 'Kh',
                    ord('Ц'): 'C',
                    ord('Ч'): 'Ch',
                    ord('Ш'): 'Sh',
                    ord('Щ'): 'Jsh',
                    ord('Ъ'): 'Z',
                    ord('Ы'): 'Ih',
                    ord('Ь'): 'Jh',
                    ord('Э'): 'Eh',
                    ord('Ю'): 'Ju',
                    ord('Я'): 'Ja',
                    ord('а'): 'a',
                    ord('б'): 'b',
                    ord('в'): 'v',
                    ord('г'): 'g',
                    ord('д'): 'd',
                    ord('е'): 'e',
                    ord('ё'): 'je',
                    ord('ж'): 'zh',
                    ord('з'): 'z',
                    ord('и'): 'i',
                    ord('й'): 'y',
                    ord('к'): 'k',
                    ord('л'): 'l',
                    ord('м'): 'm',
                    ord('н'): 'n',
                    ord('п'): 'p',
                    ord('р'): 'r',
                    ord('с'): 's',
                    ord('т'): 't',
                    ord('у'): 'u',
                    ord('ф'): 'f',
                    ord('х'): 'kh',
                    ord('ц'): 'c',
                    ord('ч'): 'ch',
                    ord('ш'): 'sh',
                    ord('щ'): 'jsh',
                    ord('ъ'): 'z',
                    ord('ы'): 'ih',
                    ord('ь'): 'jh',
                    ord('э'): 'eh',
                    ord('ю'): 'ju',
                    ord('я'): 'ja'}
        
        for root, dirs, files in os.walk(p):
            for dir in dirs:
                d = os.path.join(root, dir)
                if os.path.exists(d):
                    os.rename(d, d.translate(alphabet))
            for file in files:
                y = os.path.join(root, file)
                if os.path.exists(y):
                    os.rename(y, y.translate(alphabet))


    def serch(p):

        for i in os.listdir(p):
            if i not in ignor:
                if os.path.isdir(p +"\\" + i):
                    serch(p + "\\" + i)
 
        for root, dirs, files in os.walk(p):
            for file in files:
                i = os.path.join(root, file)
                sort_file(i, file)
                unpuck_archives(i, file)
                
            for folder in dirs:
                f = os.path.join(root, folder)
                remove_folder(f)


    def creat_folder():

        if len(images_list) != 0:
            if not os.path.exists(p +"\\images"):
                os.mkdir(p + "\\images")

        if len(video_list) != 0:
            if not os.path.exists(p + "\\videos"):
                os.mkdir(p + "\\videos")

        if len(documents_list) != 0:
            if not os.path.exists(p + "\\documents"):
                os.mkdir(p + "\\documents")

        if len(music_list) != 0:
            if not os.path.exists(p + "\\music"):
                os.mkdir(p + "\\music")
        
        if len(archives_list) !=0:
            if not os.path.exists(p + "\\archives"):
                os.mkdir(p + "\\archives")


    def sort_file(i, file):

        if file.endswith(suffix_imeges):
            if file not in images_list:
                images_list.append(file)
            creat_folder()
            if  i != p + "\\images" + "\\" + file:
                os.replace(i, p + "\\images" + "\\" + file)
        
        elif file.endswith(suffix_videos):
            if file not in video_list:
                video_list.append(file)
            creat_folder()
            if i != p + "\\videos" + "\\" + file:
                os.replace(i , p + "\\videos" + "\\" + file)
        
        elif file.endswith(suffix_documents):
            if file not in documents_list:
                documents_list.append(file)
            creat_folder()
            if i != p + "\\documents" + "\\" + file:
                os.replace(i, p + "\\documents" + "\\" + file)
        
        elif file.endswith(suffix_music):
            if file not in music_list:
                music_list.append(file)
            creat_folder()
            if i != p + "\\music" + "\\" + file:
                os.replace(i, p + "\\music" + "\\" + file)


    def remove_folder(f):
        if not os.listdir(f):
            os.removedirs(f)


    def unpuck_archives(i, file):

        if file.endswith(suffix_archiv):
            if file not in archives_list:
                archives_list.append(file)
            creat_folder()
            name_folder_archive = file.split(".")
            shutil.unpack_archive(i, p + "\\archives"+ "\\" + name_folder_archive[0])


    normalize(p)
    serch(p)

    print (f"Sorting files by the specified path {p} completed succesfully!")


if __name__=="__main__":
    main()