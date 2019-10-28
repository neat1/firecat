import subprocess


class Application:
    '''This class needs an exe file to operate. The XYZ.exe file will be inserted into commands in the terminal.
    Please add your exe to PATH'''

    def __init__(self,exe):
        self.exe = exe

    def open_this_application(self):

        command_to_run = '{}'.format(self.exe)
        subprocess.Popen(command_to_run)

    def close_this_application(self):
        subprocess.call("TASKKILL /F /IM {}".format(self.exe))











