"""mio: modules, (contains functions capture_output, restore_output,
    print_file, clear_file)"""
import sys
_file_object = None

def capture_output(file = 'capture_file.txt'):
    """capture_output(file = 'capture_file.txt'): redirect the standard
    output to 'file'"""
    global _file_object
    print("output will be sent to the file {0}".format(file))
    print("restore to normal by calling 'mio.restore_output()'")
    _file_object = open(file, 'w')
    sys.stdout = _file_object

def restore_output():
    """restore_output(): restore the standard output back to the
    defult (also closes the capture file)"""
    global _file_object
    sys.stdout = sys.__stdout__
    _file_object.close()
    print("standard output has been restored back to normal")

def print_file(file = 'capture_file.txt'):
    """print_file(file = 'capture_file.txt'): print the given file to
    the standard output"""
    f = open(file, 'r')
    print(f.read())
    f.close()

def clear_file(file = 'capture_file.txt'):
    """clear_file(file = 'capture_file.txt'): clear the contents of
    the given file"""
    f = open(file, 'w')
    f.close()
