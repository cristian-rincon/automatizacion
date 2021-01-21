import os
import shutil
import logging
import tempfile
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Borrar temporales')
main_canvas = tk.Canvas(root, width=300, height=150)
main_canvas.pack()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(process)d - %(levelname)s - %(message)s',  datefmt='%d-%b-%y %H:%M:%S')
tmp_folder_path = tempfile.gettempdir()


def clean():

    logging.info("Temp files path:")
    logging.info(tmp_folder_path)
    tmp_contents = os.listdir(tmp_folder_path)
    # logging.info(tmp_contents)
    for i in tmp_contents:
        try:
            if os.path.isfile(i):
                filename = os.path.join(tmp_folder_path, i)
                logging.warning(f"Removing file {filename}")
                os.remove(filename)
            elif os.path.isdir(i):
                foldername = os.path.join(tmp_folder_path, i)
                logging.warning(f"Removing folder {foldername}")
                shutil.rmtree(foldername)
        except Exception as e:
            messagebox.showerror("Opps! Tenemos un problema", e)
        else:
            break

    messagebox.showinfo(
        "Muy bien", "Hemos eliminado todos tus archivos temporales.")


button1 = tk.Button(text='Borrar temporales',
                    command=clean, bg='white', fg='black')
main_canvas.create_window(150, 75, window=button1)

root.mainloop()
