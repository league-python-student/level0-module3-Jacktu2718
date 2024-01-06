from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = False


def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    playsound('shiny-objects.wav')

    # TODO 2) Ask the user how many shiny objects they want
    shiny = simpledialog.askstring(title='shiny', prompt='How many shiny objects do you want?')
    if shiny == '1':
        for i in range(1):
            playsound('shiny-objects.wav')
    elif shiny == '2':
        for i in range(2):
            playsound('shiny-objects.wav')
    elif shiny == '3':
        for i in range(3):
            playsound('shiny-objects.wav')
    elif shiny == '4':
        for i in range(4):
            playsound('shiny-objects.wav')
    elif shiny == '5':
        for i in range(5):
            playsound('shiny-objects.wav')

    # TODO 3) Play the sound that many times

    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
