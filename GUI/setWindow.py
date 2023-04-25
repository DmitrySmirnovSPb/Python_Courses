def setWindow(root):
    root.title('Окно программы')
    root.resizable(False, False)
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int(ws / 2 - w / 2)
    y = int(hs / 2 - h / 2)
    root.geometry('{0}x{1}+{2}+{3}'.format(w,h,x,y))