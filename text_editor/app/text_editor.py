import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
saved = ''
class App(tk.Tk):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        #-------Config Area-----------------------------------------------------------------------------------------------
        self.config(bg="#000000")
        self.geometry('750x500')
        self.protocol("WM_DELETE_WINDOW", self.exit)
        #-------Menu Area-------------------------------------------------------------------------------------------------
        self.menu = tk.Menu(self)
        self.view_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        p1 = tk.PhotoImage(file = 'm.png')
        self.iconphoto(False, p1)
        #-------Command Area----------------------------------------------------------------------------------------------
        self.view_menu.add_command(label="Night Mode", command=self.dark_mode)
        self.view_menu.add_command(label="Light Mode", command=self.light_mode)

        self.file_menu.add_command(label='New File', accelerator='Ctrl+N', command=self.new_file)
        self.file_menu.add_command(label='Open', accelerator='Ctrl+O', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', accelerator='Ctrl+S', command=self.save_file)
        self.file_menu.add_command(label='Save as', accelerator='Ctrl+Shift+S', command=self.saveas_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=self.exit)
        self.filename = ''
        self.title('Untitled - Mnotes')
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.menu.add_cascade(label='View', menu=self.view_menu)
        self.config(menu=self.menu)
        #-------Bind Area-------------------------------------------------------------------------------------------------
        self.bind('<Control-o>', self.open_file)
        self.bind('<Control-s>', self.save_file)
        self.bind('<Control-Shift-S>', self.saveas_file)
        self.bind('<Control-q>', self.exit)
        #-------Text Area-------------------------------------------------------------------------------------------------
        self.text_area = tk.Text(self, tabs=4)
        self.scroll_bar = ttk.Scrollbar(self, orient='vertical', command=self.text_area.yview)
        #-------Control Area----------------------------------------------------------------------------------------------
        self.text_area.pack(side='left', fill='both', expand=True)
        self.scroll_bar.pack(side='right', fill='y')
#---Function Area-------------------------------------------------------------------------------------------------
    def dark_mode(self, *args):
        self.text_area.config(bg="#131413", fg="white", insertbackground="white")
    def light_mode(self, *args):
        self.text_area.config(bg="white", fg="black", insertbackground="black")
    def new_file(self, *args):
        self.text_area.delete('1.0', 'end')
        self.title('Untitled - Mnotes')
        self.filename = ''

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(title='Open File', filetypes=(('All File', '*.*'),
                                                                            ('Python File', '*.py'),
                                                                            ('HTML File', '*.html'),
                                                                            ('CSS File', '*.css'),
                                                                            ('Javascript File', '*.js')))

        print(self.filename)
        if self.filename in (tuple(), ''):
            pass
        else:
            self.text_area.delete('1.0', 'end')
            opened_file = open(self.filename, 'r')
            stuff = opened_file.read()
            self.text_area.insert('1.0', stuff)
            opened_file.close()
            self.title(f'{self.filename} - Mnotes')
    def save_file(self, *args):
        if self.filename in (tuple(), ''):
            self.saveas_file()
        else:
            saved_file = open(f'{self.filename}', 'w')
            saved_file.write(self.text_area.get('1.0', 'end'))
            saved_file.close()
            saved = self.text_area.get('1.0', 'end')
            self.title(f'{self.filename} - Mnotes')

    def saveas_file(self, *args):
        self.filename = filedialog.asksaveasfilename(title='Save File', filetypes=(('All File', '*.*'),
                                                                                    ('Python File', '*.py'),                                                                                ('HTML File', '*.html'),
                                                                                    ('CSS File', '*.css'),
                                                                                    ('Javascript File', '*.js')))
        if self.filename in (tuple(), ''):
            pass
        else:
            savedas_file = open(self.filename, 'w')
            savedas_file.write(self.text_area.get('1.0', 'end'))
            savedas_file.close()
            self.title(f'{self.filename} - Mnotes')
    def exit(self, *args):
        if saved == self.text_area.get('1.0', 'end'):
            self.destroy()
        else:
            confirm = messagebox.askyesnocancel(title='Quit', message='You haven\'t saved your projects, Do you want to save it?',
                                                default=messagebox.YES, parent=self)
            if confirm:
                self.save_file()
                self.destroy()
            elif confirm is None:
                return None
            else:
                self.destroy()
#------------------------------------------------------App End----------------------------------------------------

master = App()
master.mainloop()

