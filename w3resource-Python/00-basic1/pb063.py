'''
63. Escreva um programa Python para obter um caminho de arquivo absoluto.
'''
def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("00PytthonBasic.txt"))

# outra solução
'''
from pathlib import Path
p = Path("00PytthonBasic.txt").resolve()
print(p)
'''
