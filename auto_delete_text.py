from tkinter import *
from tkinter import filedialog
from threading import Timer


class AutoDeleteText:
    def __init__(self, root):
        self.root = root
        self.root.title('The Most Dangerous Writing App')
        self.root.geometry('800x600')
        self.description = ("The Most Dangerous Writing App is a GUI app for free writing that combats writer's block "
                            "by deleting all progress if the user stops typing for five seconds. It is targeted at "
                            "creative writers who want to write first drafts without worrying about editing or "
                            "formatting.\n\nThis app is built on the same technique and the written text will be "
                            "deleted after 5 seconds by default if you stop writing. You will have the option of "
                            "setting your own inactivity timer and also saving the text if you wish to take a break.")

        # Widgets
        self.description_label = None
        self.deletion_label = None
        self.typing_area_text = None
        self.restart_button = None
        self.timer_label = None
        self.timer_entry = None
        self.save_button = None
        self.timer = None
        self.inactivity_time = 5

        self.create_widgets()

    def create_widgets(self):
        self.description_label = Label(self.root, text=self.description, wraplength=750, justify='left')
        self.description_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.deletion_label = Label(self.root, text='', justify='left', fg='red')
        self.deletion_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.timer_label = Label(self.root, text='Enter Inactivity Time: ')
        self.timer_label.grid(row=2, column=0, padx=5, pady=10)

        self.timer_entry = Entry(self.root)
        self.timer_entry.grid(row=2, column=1, padx=5, pady=10)
        self.timer_entry.insert(0, '5')

        self.typing_area_text = Text(self.root, height=20, width=110)
        self.typing_area_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.typing_area_text.bind('<KeyRelease>', self.reset_timer)

        self.restart_button = Button(self.root, text='Restart', command=self.restart_app)
        self.restart_button.grid(row=4, column=0, padx=10, pady=10)

        self.save_button = Button(self.root, text='Save Text', command=self.save_text)
        self.save_button.grid(row=4, column=1, padx=10, pady=10)

    def get_inactivity_time(self):
        try:
            time = int(self.timer_entry.get())
            if time <= 0:
                self.deletion_label.config(text='Enter a positive integer value for Inactivity Time!', fg='red')
                return None
            return time
        except ValueError:
            self.deletion_label.config(text='Enter a valid number!', fg='red')
            return None

    def reset_timer(self, event=None):
        if self.timer:
            self.timer.cancel()

        self.inactivity_time = self.get_inactivity_time()
        if self.inactivity_time is None:
            return

        self.timer = Timer(self.inactivity_time, self.delete_text)
        self.timer.start()

    def delete_text(self):
        self.typing_area_text.delete(1.0, END)
        self.deletion_label.config(text=f'Text has been deleted as you did not write for {self.inactivity_time} '
                                        f'seconds!!', fg='red')

    def restart_app(self):
        self.typing_area_text.delete(1.0, END)
        self.deletion_label.config(text='')
        self.timer_entry.delete(0, END)
        self.timer_entry.insert(0, str(self.inactivity_time))
        self.reset_timer()

    def save_text(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'),
                                                                                     ('All Files', '*.*')])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.typing_area_text.get(1.0, END).strip())
            self.deletion_label.config(text=f'Text file saved to {file_path}!', fg='green')
