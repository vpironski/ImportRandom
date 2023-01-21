import os
path = os.path.dirname(os.path.abspath(__file__))
cut_index = path.find("Engine\\") + len('Engine\\')
if cut_index != -1:
    os.chdir(path[:cut_index])
