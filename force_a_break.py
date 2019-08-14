import subprocess
import os


def close_this_application(exe_file):
    # Closes application on Windows
    os.system("TASKKILL /F /IM {}".format(exe_file))


def open_this_application(exe_path= (r'"C:\Program Files\JetBrains\IntelliJ'
                                     r' IDEA Community Edition '
                                     r'2019.1.2\bin\idea64.exe"')):
    # Opens application on Windows, default is JAVA IDE
    subprocess.call(exe_path)


def currently_running_applications() -> str:
    # Returns a string output of the currently running apps.
    command = 'WMIC PROCESS get Caption'
    string_output = subprocess.check_output(command, shell=False, universal_newlines=True)
    return string_output


# Close application on Windows, two examples:
if 'cmd.exe' in currently_running_applications():
    close_this_application('cmd.exe')
if 'Spotify.exe' in currently_running_applications():
    close_this_application('Spotify.exe')

# Opens any program notepad++ as an example
open_this_application(r"C:\Program Files (x86)\Notepad++\notepad++.exe")
#hello






