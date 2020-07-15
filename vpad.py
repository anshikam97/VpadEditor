import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_app = tk.Tk()
main_app.geometry("1000x500")
main_app.title("Vpad text editor")

# -------------|| main menu ||----------------------------------
main_menu = tk.Menu()

# icons for menubar
new_icon = tk.PhotoImage(file="icon/add f.png")
open_icon = tk.PhotoImage(file="icon/openf.png")
save_icon = tk.PhotoImage(file="icon/savef.png")
saveas_icon = tk.PhotoImage(file="icon/saveasf.png")
exit_icon = tk.PhotoImage(file="icon/exitf.png")
cut_icon = tk.PhotoImage(file="icon/cut.png")
copy_icon = tk.PhotoImage(file="icon/copy.png")
paste_icon = tk.PhotoImage(file="icon/paste.png")
clear_icon = tk.PhotoImage(file="icon/clearall.png")
find_icon = tk.PhotoImage(file="icon/find.png")
toolbar_icon = tk.PhotoImage(file="icon/toolbar.png")
statusbar_icon = tk.PhotoImage(file="icon/statusbar.png")
ldefault_icon = tk.PhotoImage(file="icon/lightDef.png")
lplain_icon = tk.PhotoImage(file="icon/lightplain.png")
dark_icon = tk.PhotoImage(file="icon/dark.png")
red_icon = tk.PhotoImage(file="icon/red.png")
monokai_icon = tk.PhotoImage(file="icon/monokai.png")
nightblue_icon = tk.PhotoImage(file="icon/nightblue.png")
bold_icon = tk.PhotoImage(file="icon/bold.png")
italic_icon = tk.PhotoImage(file="icon/italic.png")
underline_icon = tk.PhotoImage(file="icon/underline.png")
colourp_icon = tk.PhotoImage(file="icon/color-palette.png")
lefta_icon = tk.PhotoImage(file="icon/align-left.png")
righta_icon = tk.PhotoImage(file="icon/align-right.png")
centera_icon = tk.PhotoImage(file="icon/align-center.png")

# menubar
file = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)

color_theme = tk.Menu(main_menu, tearoff=False)
theme_chooser = tk.StringVar()
color_icon = (ldefault_icon, lplain_icon, dark_icon, red_icon, monokai_icon, nightblue_icon)
color_dict = {
    "Light Default": ("#000000", "#ffffff"),
    "Light Plain": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Red": ("#2d2d2d", "#ffe8e8"),
    "Monokai": ("#d3b774", "#474747"),
    "Night Blue": ("#ededed", "#6b9dc2")
}

# cascade
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)
# -------------end main menu------------------------------


# -------------|| toolbar ||----------------------------------

tool_bar = ttk.Label(main_app)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font box
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='randomly')
font_box['values'] = font_tuples
font_box.current(font_tuples.index("Arial"))
font_box.grid(row=0, column=0, padx=5)

# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='randomly')
font_size['values'] = tuple(range(8, 80))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)
colorp_btn = ttk.Button(tool_bar, image=colourp_icon)
colorp_btn.grid(row=0, column=5, padx=5)
lefta_btn = ttk.Button(tool_bar, image=lefta_icon)
lefta_btn.grid(row=0, column=6, padx=5)
centera_btn = ttk.Button(tool_bar, image=righta_icon)
centera_btn.grid(row=0, column=7, padx=5)
righta_btn = ttk.Button(tool_bar, image=righta_icon)
righta_btn.grid(row=0, column=8, padx=5)

# -------------end toolbar------------------------------


# -------------|| text editor ||----------------------------------
text_editor = tk.Text(main_app)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and size funtionality
current_ff = 'Arail'
current_fs = '12'


def change_font(main_app):
    global current_ff
    current_ff = font_family.get()
    text_editor.config(font=(current_ff, current_fs))


def change_fontsize(main_app):
    global current_fs
    current_fs = font_size.get()
    text_editor.config(font=(current_ff, current_fs))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

text_editor.config(font=('Arial', 12))


# button funtionality
def change_bold():
    text_p = tk.font.Font(font=text_editor['font'])
    if text_p.actual()['weight'] == 'normal':
        text_editor.config(font=(current_ff, current_fs, "bold"))
    if text_p.actual()['weight'] == 'bold':
        text_editor.config(font=(current_ff, current_fs, "normal"))


bold_btn.config(command=change_bold)


def change_italic():
    text_p = tk.font.Font(font=text_editor['font'])
    if text_p.actual()['slant'] == 'roman':
        text_editor.config(font=(current_ff, current_fs, "italic"))
    if text_p.actual()['slant'] == 'italic':
        text_editor.config(font=(current_ff, current_fs, "normal"))


italic_btn.config(command=change_italic)


def change_underline():
    text_p = tk.font.Font(font=text_editor['font'])
    if text_p.actual()['underline'] == 0:
        text_editor.config(font=(current_ff, current_fs, "underline"))
    if text_p.actual()['underline'] == 1:
        text_editor.config(font=(current_ff, current_fs, "normal"))


underline_btn.config(command=change_underline)


# font color funtionality
def change_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.config(fg=color_var[1])


colorp_btn.config(command=change_color)


# font align
def change_lalign():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


lefta_btn.config(command=change_lalign)


def change_ralign():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


righta_btn.config(command=change_ralign)


def change_calign():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


centera_btn.config(command=change_calign)

# -------------end main menu------------------------------


# -------------|| status bar ||----------------------------------
status_bar = ttk.Label(main_app, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", changed)

# -------------end status bar------------------------------


# -------------|| main menu funtionality ||----------------------------------

url = ''


def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                     filetypes=(('Text File', "*.txt"), ("All Files", "*.*")))
    try:
        with open(url, "r") as filereader:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, filereader.read())
    except FileExistsError:
        return
    except:
        return
    main_app.title(os.path.basename(url))


def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, encoding='utf-8') as filewriter:
                filewriter.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextention=".txt",
                                           filetypes=(('Text File', "*.txt"), ("All Files", "*.*")))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextention=".txt",
                                   filetypes=(('Text File', "*.txt"), ("All Files", "*.*")))
        url.write(content)
        url.close()
    except:
        return


def exit_file(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("Warning","Do you want to save the file?")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url, 'w', encoding='utf-8') as filewriter:
                        filewriter.write(content)
                        main_app.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    url = filedialog.asksaveasfile(mode='w', defaultextention=".txt",
                                   filetypes=(('Text File', "*.txt"), ("All Files", "*.*")))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return

# file command
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)
file.add_command(label="Save As", image=saveas_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as)
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q",command=exit_file)

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos : text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')


    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content =text_editor.get(1.0,tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_dialouge = tk.Toplevel()
    find_dialouge.geometry('450x250+500+200')
    find_dialouge.title("Find")
    find_dialouge.resizable(0,0)

    find_frame = ttk.LabelFrame(find_dialouge, text='Find/Replace')
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame, text='Find: ')
    text_replace_label = ttk.Label(find_frame, text='Replace ')

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    find_btn = ttk.Button(find_frame, text='Find', command=find)
    replace_btn = ttk.Button(find_frame, text='Replace', command=replace)


# edit command
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X", command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C", command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V", command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear All", image=clear_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X", command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F", command = find_func)

# view checkbutton
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, variable=show_toolbar,image=toolbar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", onvalue=1, offvalue=False, variable=show_statusbar, image=statusbar_icon, compound=tk.LEFT, command=hide_statusbar)

# colour radio button
def change_theme():
    choosen_theme = theme_chooser.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icon[count], variable=theme_chooser, compound=tk.LEFT, command=change_theme)
    count += 1

# -------------end main menu------------------------------

main_app.bind("<Control-n>", new_file)
main_app.bind("<Control-o>", open_file)
main_app.bind("<Control-s>", save_file)
main_app.bind("<Control-Alt-s>", save_as)
main_app.bind("<Control-q>", exit_file)
main_app.bind("<Control-f>", find_func)

main_app.config(menu=main_menu)
main_app.mainloop()
