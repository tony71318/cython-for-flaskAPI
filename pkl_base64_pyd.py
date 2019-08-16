import base64, platform, subprocess, os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("pydFileName", help="pydFileName")
parser.add_argument("targetFolderName", help="targetFolderName")
args = parser.parse_args()

pydFileName = args.pydFileName
targetFolderName = args.targetFolderName + '/'

if platform.system() == 'Windows':
    with open(pydFileName + '.py', 'w') as f:
        f.write('#cython: language_level=3\n')
        f.write('enc_model = {\n')
        
        for fileName in os.listdir(targetFolderName):
            _name = fileName.split('.')[0]

            with open(targetFolderName + fileName, 'rb') as file:
                byteArray = file.read()

            enc_byteArray = base64.b64encode(byteArray)
            f.write(" '{}' : {}, \n".format(_name, enc_byteArray))

        f.write('}')
        f.close()

    process = subprocess.Popen('python setup.py ' + pydFileName + ' build_ext --inplace', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('build pyd success.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + pydFileName + '.py', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('delete ' + pydFileName + '.py sucess.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + pydFileName + '.c ', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('remove .c sucess')
    else:
        print('something wrong')

    process = subprocess.Popen('mv ' + pydFileName + '.cp36-win_amd64.pyd ' + pydFileName + '.pyd', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('rename ' + pydFileName + '.pyd sucess.')
    else:
        print('something wrong')

else:
    with open(pydFileName + '.py', 'w') as f:
        f.write('#cython: language_level=3\n')
        f.write('enc_model = {\n')
        
        for fileName in os.listdir(targetFolderName):
            _name = fileName.split('.')[0]

            with open(targetFolderName + fileName, 'rb') as file:
                byteArray = file.read()

            enc_byteArray = base64.b64encode(byteArray)
            f.write(" '{}' : {}, \n".format(_name, enc_byteArray))

        f.write('}')
        f.close()
        
    process = subprocess.Popen('python3 setup.py ' + pydFileName + ' build_ext --inplace', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('build pyd success.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + pydFileName + '.py', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('delete ' + pydFileName + '.py sucess.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + pydFileName + '.c ', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('remove .c sucess')
    else:
        print('something wrong')

    process = subprocess.Popen('mv ' + pydFileName + '.*.so ' + pydFileName + '.so', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('rename ' + pydFileName + '.so sucess.')
    else:
        print('something wrong')

    ## ex. gcc -shared -o libhello.so -fPIC hello.c
    #process = subprocess.Popen('gcc -shared -o ../flaskAPI/py/pkl/'+ _id + '/' + pydFileName + '.so -fPIC ./c/' + _id + '/' + pydFileName + '.c', shell=True, stdout=subprocess.PIPE)
    #process.wait()
    #if process.returncode == 0:
    #    print('compile ' + pydFileName + '.so sucess.')
    #else:
        #    print('something wrong')
