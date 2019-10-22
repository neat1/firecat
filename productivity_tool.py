import subprocess


class Application:
    '''This class needs an exe file to operate. The XYZ.exe file will be inserted into commands in the terminal.'''

    def __init__(self,exe):
        self.exe = exe

    def open_this_application(self):

        command_to_search = 'WHERE {}'.format(self.exe)
        # select the first line which contains the actual exe file.
        command_output = subprocess.check_output(command_to_search, universal_newlines=True)
        start_of_the_command = command_output.find('C')
        end_of_the_command = command_output.find('exe')
        sliced_final_command = slice(start_of_the_command, end_of_the_command + 3)
        print('Opening up application...:')
        print(command_output[sliced_final_command])

        subprocess.call(command_output[sliced_final_command])

    def close_this_application(self):
            subprocess.call("TASKKILL /F /IM {}".format(self.exe))




instance = Application('notepad.exe')
instance.open_this_application()


