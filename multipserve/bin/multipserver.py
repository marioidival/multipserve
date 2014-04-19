#!/usr/bin/env python
from multipserve import core_mps as mps

import argparse
import sys


class MPCommand(object):

    prog = 'multipserve'
    description = 'Trigger and kill your applications written in Pyramid'
    parse = argparse.ArgumentParser(prog=prog, description=description)

    parse.add_argument('--apps', dest='apps',
                       help='load apps passed by arguments',
                       nargs='+')
    parse.add_argument('-k', '--kill', help='kill/stop app', nargs='+')

    #TODO: NOT IMPLEMENTED - server log
    parse.add_argument('-sl', '--server-log', dest='server_log',
                       help='make an serve for log app [NOT IMPLEMENTED]')

    def __init__(self, argv):
        self.option = self.parse.parse_args(argv[1:])

    def run(self):
        if self.option.apps:
            mp = mps.MultiPserve(self.option.apps)
            for dir_app in mp.projects.keys():
                mp.load_server(dir_app)

        if self.option.kill:
            mp = mps.MultiPserve(self.option.kill)
            mp.kill_servers(self.option.kill)

        #TODO: -> NOT IMPLEMENTED
        if self.option.server_log:
            pass


def main(argv=sys.argv):
    command = MPCommand(argv)
    return command.run()

if __name__ == "__main__":
    sys.exit(main() or 0)
