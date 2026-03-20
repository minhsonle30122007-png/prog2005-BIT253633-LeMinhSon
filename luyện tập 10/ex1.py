#Bài 1
def get_full_filename_manual(path):
    return path.replace('\\','/')

def get_song_name_only_manual(path):
    full_name = get_full_filename_manual(path)
    if '.' in full_name:
        return".".join(full_name.split('.')[:-1])
    return full_name

link = "d:\\music\\muabui.mp3"
print(f"Tên đầy đủ: {get_full_filename_manual(link)}")
print(f"Tên bài hát:{get_song_name_only_manual(link)}")