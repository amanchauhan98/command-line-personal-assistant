from pygame import mixer
def music(file,volume,next,skip):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == "stop":
            mixer.music.stop()
            break
        elif input_of_user == "pause" :
            mixer.music.pause()
            continue
        elif input_of_user == next:
            mixer.music.queue(next)
            mixer.music.load(next)
            mixer.music.play()
            continue
        elif input_of_user ==  "rewind":
            mixer.music.rewind()
            continue
        elif input_of_user == "unpause":
            mixer.music.unpause()
            continue
        elif input_of_user == volume:
            mixer.music.set_volume(volume) 
            continue
        elif input_of_user == skip:
            mixer.music.fadeout(skip)
            continue


music_name = str(input("Enter the name of music\n"))
music_volume = float(input("Enter the volume of music\n"))
music_next = str(input("enter the next music you want to play\n"))
music_skip = int(input("enter the time in sec. foor skipping the music\n"))
music(music_name,music_volume,music_next,music_skip)


# music_skip = int(input("enter the time in sec. foor skipping the music"))
# music(music_name,music_volume,music_next,music_skip)

# print(dir(mixer.music))
# mixer.music.fadeout(35)







