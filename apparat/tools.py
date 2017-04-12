#!/usr/bin/python
"""apparat - an application launcher for linux"""

# -----------------------------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------------------------

## general
import datetime # for timestamp in debug output
import os
import subprocess # for checking if cmd_exists
import sys

## apparat
import constants
import version


DEBUG = False

# -----------------------------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------------------------
def cmd_exists(cmd):
    """Method to check if a command exists."""
    debug_output('cmd_exists', 'starting', 1)
    return subprocess.call('type ' + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def check_arguments():
    """Checks if apparat was started with arguments or not"""
    debug_output('check_arguments', 'starting', 1)
    global DEBUG # pylint:disable=global-statement
    if len(sys.argv) > 2: # too much arguments
        print('Error: Unsupported amount of parameters')
        show_help()
        sys.exit()

    elif len(sys.argv) == 1: # no user argument available
        pass

    elif (sys.argv[1] in ("-d", "--debug")):
        DEBUG = True

    elif (sys.argv[1] in ("-h", "--help")):
        show_help()
        sys.exit()

    elif (sys.argv[1] in ("-v", "--version")):
        show_version()
        sys.exit()

    else:
        print('Error: Unknown argument. Loading help')
        show_help()
        sys.exit()

    debug_output('check_arguments', 'finished', 1)


def debug_output(source, message, message_type=0):
    """Method to print debug messages (if debug = True)."""
    if DEBUG is True:
        timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        source = source.ljust(40) # Add spaces to source until it has length of 40 chars (readability)

        # colorize the message
        if(message_type == 1): # Info
            text_color = constants.C_GREEN
            message_type_class = ' I '
        elif(message_type == 2): # Warning
            text_color = constants.C_YELLOW
            message_type_class = ' W '
        elif(message_type == 3): # Error
            text_color = constants.C_RED
            message_type_class = ' E '
        else: # Other = default value for message type
            text_color = constants.C_BLUE_LIGHT
            message_type_class = ' O '

        ## format: time + message_type_class + source + message
        print(timestamp+" # "+text_color+message_type_class+constants.C_DEFAULT+" # "+source+" # "+text_color+message+constants.C_DEFAULT)


def generate_timestamp():
    """Generates and returns a timestamp in the format: YYYYMMDD__HHMMSS"""
    timestamp = '{:%Y%m%d__%H%M%S}'.format(datetime.datetime.now())
    return timestamp


def check_linux_requirements():
    """Method to check the used linux packages on app start"""
    debug_output('check_linux_requirements', 'starting', 0)
    ## needed for session commands:
    # - gnome-screensaver-command
    # - gnome-session-quit
    # - systemctl
    # - xdg-open
    # - xdotool
    if which('gnome-screensaver-command') is None:
        debug_output('check_linux_requirements', 'Error: gnome-screensaver-command is missing', 3)
        sys.exit()

    if which('gnome-session-quit') is None:
        debug_output('check_linux_requirements', 'Error: gnome-session-quit is missing', 3)
        sys.exit()

    if which('systemctl') is None:
        debug_output('check_linux_requirements', 'Error: systemctl is missing', 3)
        sys.exit()

    if which('xdg-open') is None:
        debug_output('check_linux_requirements', 'Error: xdg-open is missing', 3)
        sys.exit()

    if which('xdotool') is None:
        debug_output('check_linux_requirements', 'Error: xdotool is missing', 3)
        sys.exit()

    debug_output('check_linux_requirements', 'finished', 1)


def which(program):
    """Method to check if executable exists"""
    debug_output('which', 'starting', 0)
    def is_exe(fpath):
        """foo"""
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    #debug_output('which', 'fpath: '+fpath, 1)
    debug_output('which', 'fname: '+fname, 1)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    debug_output('which', 'finished', 1)
    return None


def show_version():
    """Show version"""
    print(version.APP_VERSION)


def show_help():
    """Show help"""
    print("\nParameter:")
    print("\t-d / --debug\tShow debug output")
    print("\t-h / --help\tShow help")
    print("\t-v / --version\tShow version")


def check_platform():
    """Method to check the platform (supported or not)"""
    debug_output('check_platform', 'starting', 0)

    ## Linux
    if sys.platform == "linux" or sys.platform == "linux2":
        debug_output('check_platform', 'Detected linux', 1)
        debug_output('check_platform', 'Desktop environment: '+os.environ.get('DESKTOP_SESSION'), 1) # Issue: 24
        if(os.environ.get('DESKTOP_SESSION') != 'gnome'):
            debug_output('check_platform', 'Here be dragons (Untested desktop environment)', 2)
        return

    else:
        # darwin = Mac OS
        # win32 = windows
        debug_output('check_platform', 'Detected unsupported platform.', 3)
        print("Error: Unsupported platform detected. Aborting ...")
        sys.exit()


def trunc_at(s, d, n=3):
    """Returns s truncated at the n'th (3rd by default) occurrence of the delimiter, d."""
    debug_output('trunc_at', 'starting', 0)
    return d.join(s.split(d)[:n])
