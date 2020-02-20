from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
from zipfile import ZipFile
import shutil
import os.path
from datetime import datetime
from PIL import ImageTk, Image
import os
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

d = {}
session_menu = {}
session_menu['values'] = {}
session_menu['temp'] = []


# this could be used if user data is retrievable through the program
def define_users():
    """
    """
    id_list = []
    for id in id_list:
        d[id] = {}
        d[id]['Filenames'] = []
        session_menu['values'] = []


def design_window():
    """Contains submodules to generate GUI window and generate necessary
    functionality.
    """

    # BUTTON ACTIONS
    def enter_btn_action():
        """Actions performed when the enter button is clicked

        """
        define_users()
        file_list.delete(0, 'end')
        user = user_id.get()
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showinfo('New User')
            d[user] = {}
            d[user]['Filenames'] = []
        else:
            messagebox.showinfo('Returning User')

    def calibrate_btn_action():
        """Actions performed when the calibrate button is clicked

        """
        user = user_id.get()
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showerror('Error - Missing User',
                                 'User not in database, make sure to click '
                                 'enter after adding ID!')


    def start_btn_action():
        """Actions performed when the start button is clicked

        """
        user = user_id.get()
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showerror('Error - Missing User',
                                 'User not in database, make sure to click '
                                 'enter after adding ID!')
        else:
            start_rec(user)


    def stop_btn_action():
        """Actions performed when the stop button is clicked

        """
        user = user_id.get()
        dtype = download_type.get()
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showerror('Error - Missing User',
                                 'User not in database, make sure to click '
                                 'enter after adding ID!')

    def download_btn_action():
        """Actions performed when the download button is clicked

        """
        user = user_id.get()
        dtype = download_type.get()
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showerror('Error - Missing User',
                                 'User not in database, make sure to click '
                                 'enter after adding ID!')


    def close_btn_action():
        """Action performed when the close button is clicked

        This button force closes the entire GUI window.
        """
        root.destroy()
        return

# FEATURES OF BUTTON ACTIONS
    def start_rec(user):
        """
        """
        # insert code to start recording
        messagebox.showinfo('Measurements started.')
        root.mainloop()
        return


    def stop_rec(user, dtype):
        """
        """
        # insert code to stop recording
        messagebox.showinfo('Measurements stopped.')
        root.mainloop()
        return

    def download_data(user, dtype):
        """
        """
        # insert code to download database
        messagebox.showinfo('Data has been exported.')
        root.mainloop()
        return

    def select(): # this would give us the option to select multiple sessions
        """Select the highlighted files from the session box

        This saves all the selected files in the file box so that the user
        can select what action they would like for the files.

        Returns
        -------
        list
            Contains list of all files selected
        """
        reslist = list()
        selected = []
        seleccion = file_list.curselection()
        for i in seleccion:
            entrada = file_list.get(i)
            reslist.append(entrada)
        for val in reslist:
            selected.append(val)
        return selected

# we may not need this
    def refresh():
        """Refresh user information

        """
        user = user_id.get()
        users = []
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID')

        else:
            define_users()
            filelist = []
            for val in filelist:
                if val not in session_menu['temp']:
                    file_list.insert(END, val)
                    session_menu['temp'] += (val,)


    def plot_action():
        """ Real-time plotting of data
        """
        user = user_id.get()
        selected = select()
        if user is '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showerror('Error - Missing User',
                                 'User not in database, make sure to click '
                                 'enter after adding ID!')
        elif selected == '':
            messagebox.showerror('Error', 'Please select images.')
            return
        elif len(selected) > 0:
            if len(selected) > 1:
                messagebox.showerror('Error - Multiple Files',
                                     'Please select only one file!')
            else:
                # enter code for real-time plotting here
                data = [0, 0, 0, 0, 0]
                plot_data(data, selected[0])


# WINDOW DESIGN
    root = Tk()
    root.title("Measurect GUI")
    root.geometry('800x400')

    # USER ID FIELD (REQUIRED):
    user_label = ttk.Label(root, text="User ID:")
    user_label.grid(column=0, row=0, pady=(5, 20), padx=(0, 5), sticky=W)

    user_id = StringVar()
    name_entry = ttk.Entry(root, textvariable=user_id, width=30)
    name_entry.grid(column=1, row=0, sticky=W, columnspan=2, pady=(5, 20))

    # DEFINE BUTTONS:
    enter_btn = ttk.Button(root, text='Enter', command=enter_btn_action)
    enter_btn.grid(column=2, row=0, pady=(5, 20), sticky=E, columnspan=1)

    close_btn = ttk.Button(root, text='Close', command=close_btn_action)
    close_btn.grid(column=0, row=9, sticky=W, columnspan=1)

    calib_btn = ttk.Button(root, text='Calibrate', command=calibrate_btn_action)
    calib_btn.grid(column=0, row=1, sticky=W, columnspan=1)

    start_btn = ttk.Button(root, text='Start Readings', command=start_btn_action)
    start_btn.grid(column=0, row=2, sticky=W, columnspan=1)

    stop_btn = ttk.Button(root, text='Stop Readings',
                              command=stop_btn_action)
    stop_btn.grid(column=0, row=3, sticky=W, columnspan=1)

    plot_btn = ttk.Button(root, text='Real-Time Graph', command=plot_action)
    plot_btn.grid(column=3, row=7, sticky=E, columnspan=1)

    download_btn = ttk.Button(root, text='Export Data',
                                command=download_btn_action)
    download_btn.grid(column=0, row=4, sticky=W, columnspan=1)

    # DEFINE DROPDOWNS:
    session_label = ttk.Label(root, text="Sessions:")
    session_label.grid(column=0, row=6, sticky=W, pady=(20, 20))

    file_list = Listbox(root, selectmode=MULTIPLE, width=45, height=5)
    file_list.grid(column=1, row=6, sticky=W, columnspan=2, pady=(20, 20))

    refresh_btn = ttk.Button(root, text="Refresh", command=refresh)
    refresh_btn.grid(column=1, row=7, sticky=W)

    process_label = ttk.Label(root, text="Drop-Down Menu:")
    process_label.grid(column=0, row=8, sticky=W, pady=(20, 20), padx=(0, 5))

    process = StringVar()
    process.set('Option 1')
    process_menu = ttk.Combobox(root, textvariable=process, width=30)
    process_menu.grid(column=1, row=8, sticky=W, columnspan=2, pady=(20, 20))
    process_menu['values'] = ('Option 1', 'Option 2',
                              'Option 3', 'Option 4')

    root.mainloop()
    return


def plot_data(b64, filename):
    """
    """
    plt.show()


def main():
    """Calls the module containing all modules necessary to generate and
    operate the GUI window and functionality.
    """
    design_window()


if __name__ == '__main__':
    main()
