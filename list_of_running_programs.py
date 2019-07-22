import subprocess
import os


def close_this_application(program_name):
    # Closes application on Windows
    os.system("TASKKILL /F /IM {}".format(program_name))


def open_this_application():
    # Opens application on Windows
    os.system(r'"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2019.1.2\bin\idea64.exe"')


def string_of_currently_running_applications():
    # Returns a string output of the currently running apps.
    cmd = 'WMIC PROCESS get Caption'
    output = subprocess.check_output(cmd, shell=False, universal_newlines=True)
    return output

# Close the .exe on Windows.
if 'cmd.exe' in string_of_currently_running_applications():
    close_this_application('cmd.exe')

#Opens IDE
open_this_application()






