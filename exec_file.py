__author__ = 'zwhitman'

import subprocess
#execfile("C:\\Users\\zwhitman\\Documents\census\\psu_app_clean2\\psu_app.py")
args = execfile("C:\\Users\\zwhitman\\Documents\census\\psu_app_clean2\\psu_app.py")
subprocess.Popen(args, close_fds=True)
