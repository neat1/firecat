import subprocess


class Application:
    '''This class needs an exe file to operate. The XYZ.exe file will be inserted into commands in the terminal.'''

    def __init__(self,exe):
        self.exe = exe

    def open_this_application(self):
        # command to find the executable path of the exe.
        command = '''WHERE /R C:\ {}*'''.format(self.exe)
        # select the first line which contains the actual exe file.
        output = subprocess.check_output(command, universal_newlines=True)
        start_of_the_command = output.find('C')
        end_of_the_command = output.find('exe')
        sliced_final_command = slice(start_of_the_command, end_of_the_command + 3)
        print(output[sliced_final_command])
        # run the exe with the full path
        subprocess.call(output[sliced_final_command])

    def close_this_application(self):
            subprocess.call("TASKKILL /F /IM {}".format(self.exe))




instance = Application('spotify.exe')
instance.open_this_application()





