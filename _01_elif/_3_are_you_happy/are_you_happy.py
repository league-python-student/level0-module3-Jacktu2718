from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    happy = simpledialog.askstring(title='happy', prompt='Are you happy?')
    if happy == 'yes':
        messagebox.showinfo(message='keep doing whatever your doing')
    elif happy == 'no':
        nohappy = simpledialog.askstring(title='no happy', prompt='Do you want to be happy?')
        if

    pass
