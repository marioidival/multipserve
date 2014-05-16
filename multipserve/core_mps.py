from subprocess import Popen, PIPE, STDOUT

import os

exclude_directories = ['.hg', '.git']
dev_files = ('dev.ini', 'development.ini')
kill = os.kill


def return_pastfile(directory):
    """Search by paste file in directory"""
    current_directory = os.path.abspath(directory)
    files_of_directory = os.listdir(current_directory)

    for each_file in files_of_directory:
        current_file = os.path.join(current_directory, each_file)
        if os.path.isfile(current_file):

            if current_file.endswith('.ini'):
                pastefile = current_file.split('/')[-1]
                if pastefile in dev_files:
                    return current_file
        else:

            if current_file not in exclude_directories:
                return_pastfile(current_file)


class MultiPserve(object):

    def __init__(self, dir_project):
        self.dir_project = dir_project
        self.projects = self.find_start_files()

    def find_start_files(self):
        '''Return dict with name application and .ini respective'''
        return_dict = {}
        for directory in self.dir_project:
            return_dict[directory] = return_pastfile(directory)

        return return_dict

    def load_server(self, dir_app):
        '''Load applications as subprocess'''
        try:
            log_file = '--log-file=' + dir_app + '.log'
            pid_file = '--pid-file=' + dir_app + '.pid'
            Popen(['pserve', self.projects[dir_app], '--reload',
                   log_file, pid_file], stdout=PIPE, stderr=STDOUT)

        except Exception as e:
            print e
        else:
            print 'init server {0}'.format(dir_app)

    def kill_servers(self, apps):
        '''the name says '''
        import signal
        for app in apps:
            pid = self.find_read_pid_file(app)
            if pid:
                kill(pid, signal.SIGTERM)
                print 'kill {0} with pid {1}'.format(app, pid)
            else:
                print 'pid file of {0} not found'.format(app)

    def find_read_pid_file(self, app_name):
        '''search pid file and get content'''
        pid_file = '{0}.pid'.format(app_name)

        if not os.path.exists(pid_file):
            return
        with open(pid_file) as f:
            content = f.read().strip()
        try:
            pid_in_file = int(content)
        except ValueError:
            pid_in_file = None

        return pid_in_file
