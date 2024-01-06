from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    story = simpledialog.askstring(title='story', prompt='Do you want to go on an adventure?')
    if story == 'no':
        messagebox.showinfo(message='keep doing whatever you are doing')
    elif story == 'yes':
        one = simpledialog.askstring(title='story', prompt='Let us start then. Once apon a time, there is a little boy, called James. James wants to go on an adventure. There are two choices, to go to the beach or go in the mountains, which one do you think James chose?')
        if one == 'beach':
            messagebox.showinfo(message='When James got on the beach, suddenly a huge wave came hitting him, James got pushed inside the wave and choked, the END.')
        elif  one == 'mountains':
            two = simpledialog.askstring(title='story', prompt='you are right! James chose the mountains! But what faced in front of him are two trails, one said that it is going to the top of the mountain. But the other one said that this trail is going to the tunnel under the mountain, which one do you want to go? Answer as top of the mountain or tunnel')
            if two == 'top of the mountain':
                 messagebox.showinfo(message='James walked to the top of the mountain and saw the alsome view of the city')
            elif two == 'tunnel':
                messagebox.showinfo(message='James walked in the tunnel, and the tunnel callaped, the END')






