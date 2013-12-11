from threading import Thread

import sys
import subprocess

exclude_directories = ['.hg', '.git']

def return_pastfile(directory):
    
    current_directory = os.path.abspath(directory)
    files_of_directory = os.listdir(current_directory)

    for file in files_of_directory:
        current_file = os.path.join(current_directory, file)
        if os.path.isfile(current_file):

            if current_file.endswith('.ini'):
                if current_file.endswith('dev.ini') or current_file.endswith('development.ini'):
                    return current_file 
        else:
            if current_file not in exclude_directories:
                return_pastfile(current_file) 

class MultiPserve(Thread):

    def __init__(self, dir_project):
        Thread.__init__(self)
        self.dir_project = dir_project

    def run(self):
        paste_file = return_pastfile(self.dir_project)
        log_file = '--log-file=' + self.dir_project +'.log'
        pid_file = '--pid-file=' + self.dir_project +'.pid'
        subprocess.call(['pserve', paste_file, '--daemon', log_file, pid_file])


def main(args):

    for arg in args[1:]:
        thread = MultiPserve(arg)
        thread.start()
