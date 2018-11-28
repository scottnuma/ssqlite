import ctypes

c_helper = ctypes.CDLL('./simpletest.so')

#host_ip = '192.168.62.135'
#file_name = 'testtxt'
#b_host_ip = host_ip.encode('utf-8')
#b_file_name = file_name.encode('utf-8')
c_helper.create_client_py.argtypes = [ctypes.c_char_p]
c_helper.open_file_py.argtypes = [ctypes.c_char_p]
c_helper.read_file_py.argtypes = [ctypes.c_int]

#c_helper.create_client_py(b_host_ip)
#c_helper.create_file_py(b_file_name)
#c_helper.read_file_py()

def mount(host_ip):
    b_host_ip = host_ip.encode('utf-8')
    c_helper.create_client_py(b_host_ip)

def open(file_name):
    b_file_name = file_name.encode('utf-8')
    c_helper.open_file_py(b_file_name)
    return FileObjectWrapper()

def read(size):
    c_helper.read_file_py(size)

class FileObjectWrapper:
    def __init__(self):
      #self._f = fileObject
      pass

    def __enter__(self):
      return self

    def __exit__(self, type, value, traceback):
      pass 

    def read(self, size):
      c_helper.read_file_py(size)
