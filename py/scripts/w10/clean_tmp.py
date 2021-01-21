import os
import shutil
import logging
import tempfile
import PySimpleGUI as sg

class Handler(logging.StreamHandler):

    def __init__(self):
        logging.StreamHandler.__init__(self)

    def emit(self, record):
        global buffer
        record = f'{record.asctime} - [{record.levelname}] - {record.message}'
        buffer = f'{buffer}\n{record}'.strip()
        window['log'].update(value=buffer)

log_file = 'run_log.txt'

# Logging setup to send one format of logs to a log file and one to stdout:
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | [%(levelname)s] - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    filename=log_file,
    filemode='w')

buffer = ''
ch = Handler()
ch.setLevel(logging.INFO)
logging.getLogger('').addHandler(ch)

tmp_folder_path = tempfile.gettempdir()


def clean():

    logging.info("Temp files path:")
    logging.info(tmp_folder_path)
    tmp_contents = os.listdir(tmp_folder_path)
    # logging.info(tmp_contents)
    for i in tmp_contents:
        element = os.path.join(tmp_folder_path, i)
        logging.info(element)
        try:
            if os.path.isfile(element):
                logging.warning(f"Intentando eliminar {element}")
                os.remove(element)

            elif os.path.isdir(element):
                logging.warning(f"Intentando eliminar {element}")
                shutil.rmtree(element, ignore_errors=True)

        except Exception as e:
            logging.error(e)

sg.theme('SystemDefaultForReal')

layout = [  [sg.Text('Haz click en el botón limpiar para eliminar los archivos temporales de tu sistema')],
            [sg.Button('limpiar')],
            [sg.Output(size=(100,15), key='log')]
         ]


window = sg.Window('Limpiar temporales', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'limpiar':
        clean()

window.close()