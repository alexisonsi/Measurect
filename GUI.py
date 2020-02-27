from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
from zipfile import ZipFile
import shutil
import os.path
import os
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from SWV_calc import *

d = {}
session_menu = {}
session_menu['values'] = {}
session_menu['temp'] = []


def design_window():
    """Contains submodules to generate GUI window and generate necessary
    functionality.
    """

    # BUTTON ACTIONS
    def enter_btn_action():
        """Actions performed when the enter button is clicked

        """
        file_list.delete(0, 'end')
        user = user_id.get()
        if user == '':
            messagebox.showerror('Error - Missing Field',
                                 'Please enter a valid User ID!')
        elif user not in d:
            messagebox.showinfo('New User', 'New user ID entered.')
            d[user] = {}
            d[user]['Filenames'] = []
        else:
            messagebox.showinfo('Returning User', 'Existing user ID entered.')

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
        else:
            messagebox.showinfo('CALIBRATE', 'Calibrating system.')



    def import_btn_action():
        """Actions performed when the import button is clicked

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
            import_data(user)


    def calc_btn_action():
        """Actions performed when the calculate button is clicked

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
            run_calc(user)

    def download_btn_action():
        """Actions performed when the download button is clicked

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
            download_data(user)



    def close_btn_action():
        """Action performed when the close button is clicked

        This button force closes the entire GUI window.
        """
        root.destroy()
        return


# FEATURES OF BUTTON ACTIONS
    def import_data(user):
        """
        """
        # insert code to import data from Matlab
        messagebox.showinfo('IMPORT', 'Measurements imported.')
        root.mainloop()
        return


    def run_calc(user):
        """
        """
        # insert code to run calculations
        messagebox.showinfo('CALCULATE', 'Calculating.')
        root.mainloop()
        return

    def download_data(user):
        """
        """
        # insert code to download database
        messagebox.showinfo('EXPORT', 'Data has been exported.')
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
        # elif selected == '':
        #     messagebox.showerror('Error', 'Please select images.')
        #     return
        # elif len(selected) > 0:
        #     if len(selected) > 1:
        #         messagebox.showerror('Error - Multiple Files',
        #                              'Please select only one file!')
            # else:
                # enter code for real-time plotting here
        xdata = [1, 2, 3, 4, 5]
        ydata = [1, 2, 3, 4, 5]
        plot_data(xdata, ydata)


# WINDOW DESIGN
    root = Tk()
    root.title("Measurect GUI")
    root.geometry('600x400')
    root.configure(background='linen')

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

    import_btn = ttk.Button(root, text='Import Data', command=import_btn_action)
    import_btn.grid(column=0, row=2, sticky=W, columnspan=1)

    calc_btn = ttk.Button(root, text='Calculate Rigidity',
                              command=calc_btn_action)
    calc_btn.grid(column=0, row=3, sticky=W, columnspan=1)

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

    process_label = ttk.Label(root, text="Export Options:")
    process_label.grid(column=0, row=8, sticky=W, pady=(20, 20), padx=(0, 5))

    process = StringVar()
    process.set('Export to LabChart')
    process_menu = ttk.Combobox(root, textvariable=process, width=30)
    process_menu.grid(column=1, row=8, sticky=W, columnspan=2, pady=(20, 20))
    process_menu['values'] = ('Export to LabChart', 'Export as CSV')

    root.mainloop()
    return


def plot_data(xdata, ydata):
    """
    """
    # need to decide what to call here
    time = [0, 1, 2, 3, 4, 5, 6, 7]
    SWV = [1, 10, 3.4, 7.6, 8.1, 2, 4.5, 8.7, 9, 7]
    SWV_to_rig(time, SWV)
    plt.plot(([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    plt.show()
    return


def main():
    """Calls the module containing all modules necessary to generate and
    operate the GUI window and functionality.
    """
    design_window()


if __name__ == '__main__':
    main()
