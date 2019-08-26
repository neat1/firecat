import subprocess


class Application:

    def __init__(self,exe):
        self.exe = exe

    def close_this_application(self):
        command = '''wmic process where "name='{}'" get ExecutablePath'''.format(self.exe)
        if self.exe in command:
            subprocess.call("TASKKILL /F /IM {}".format(self.exe))

    def open_this_application(self):
        # command to find the Executable path of the exe
        command = '''wmic process where "name='{}'" get ExecutablePath'''.format(self.exe)
        # find the exact path out of multiple possible paths
        output = subprocess.check_output(command, universal_newlines=True)
        start_of_the_command = output.find('C')
        end_of_the_command = output.find('exe')
        sliced_final_command = slice(start_of_the_command, end_of_the_command + 3)
        # run the exe with the full path
        print(output[sliced_final_command])
        #subprocess.call(output[sliced_final_command])


instance = Application('cmd.exe')
instance.close_this_application()





