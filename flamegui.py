from tkinter import*

root = Tk()
root.title("FLAMES")

boyframe = Frame(root)
boyframe.pack(side=TOP, expand = TRUE)

girlframe = Frame(root)
girlframe.pack(side=TOP)

resultframe = Frame(root)
resultframe.pack(side=TOP)

labelboy = Label(boyframe, text="Enter Boy's name : ")
labelboy.pack(side = LEFT, fill = BOTH)

labelgirl = Label(girlframe, text="Enter Girl's name : ")
labelgirl.pack(side = LEFT, fill = BOTH)

e1 = Entry(boyframe)
e1.pack(side = RIGHT, fill = BOTH)

e2 = Entry(girlframe)
e2.pack(side = RIGHT, fill = BOTH)

tex = Text(root)
tex.pack(side= TOP, fill = BOTH)

def wordsplitter():
    l =[]
    h= []
    global e
    boy = e1.get() 
    girl = e2.get()
    for i in boy:
        l.append(i)
    for i in girl:
        h.append(i)
    global x
    x = 3
    def counter():
        global x
        x = x -1
        if x== 0:
            finder(l,h)
        for i in h:
            for j in l:
                if i == j:
                    l.remove(i)
                    h.remove(i)
                    counter()
                    break
    counter()

def finder(l,h):
    l = l + h
    fl = len(l)
    flame =['f','l','a','m','e','s']
    flames = {'f':"Friends",'l':"Love",'a':"Affection",'m':"Marriage",'e':'Enemy','s':"Sister"}
    s = 6 
    i= 0
    while s > 1:
        i = i+fl
        while i > s:
            i = i - s
        del flame[i-1]
        if s == 2:
            tex.delete(0.0, END)
            tex.insert(0.0, flame[0],'',flames[flame[0]])
        s = s - 1
                   
b = Button(resultframe,text='Check your result',command=wordsplitter, bg='red'
           , relief=SUNKEN)
b.pack(side = RIGHT, fill = BOTH)

root.mainloop()

