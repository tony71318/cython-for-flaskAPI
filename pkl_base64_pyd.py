import base64, platform, subprocess, os

modelName = 'lasso'
folderName = 'lassoModelParams/'

if platform.system() == 'Windows':
    with open(modelName + '.py', 'w') as f:
        f.write('#cython: language_level=3\n')
        f.write('enc_model = {\n')
        
        for fileName in os.listdir(folderName):
            _name = fileName.split('.')[0]
            _id = fileName.split('_')[1]

            with open(folderName + fileName, 'rb') as file:
                byteArray = file.read()

            enc_byteArray = base64.b64encode(byteArray)
            f.write(" '{}' : {}, \n".format(_name, enc_byteArray))

        f.write('}')
        f.close()

    process = subprocess.Popen('python setup.py ' + modelName + ' build_ext --inplace', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('build pyd success.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + modelName + '.py', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('delete ' + modelName + '.py sucess.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + modelName + '.c ', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('remove .c sucess')
    else:
        print('something wrong')

    process = subprocess.Popen('mv ' + modelName + '.cp36-win_amd64.pyd ' + modelName + '.pyd', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('rename ' + modelName + '.pyd sucess.')
    else:
        print('something wrong')

else:
    with open(modelName + '.py', 'w') as f:
        f.write('#cython: language_level=3\n')
        f.write('enc_model = {\n')
        
        for fileName in os.listdir(folderName):
            _name = fileName.split('.')[0]
            _id = fileName.split('_')[1]

            with open(folderName + fileName, 'rb') as file:
                byteArray = file.read()

            enc_byteArray = base64.b64encode(byteArray)
            f.write(" '{}' : {}, \n".format(_name, enc_byteArray))

        f.write('}')
        f.close()
        
    process = subprocess.Popen('python3 setup.py ' + modelName + ' build_ext --inplace', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('build pyd success.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + modelName + '.py', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('delete ' + modelName + '.py sucess.')
    else:
        print('something wrong')

    process = subprocess.Popen('rm ' + modelName + '.c ', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('remove .c sucess')
    else:
        print('something wrong')

    process = subprocess.Popen('mv ' + modelName + '.*.so ' + modelName + '.so', shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print('rename ' + modelName + '.so sucess.')
    else:
        print('something wrong')

    ## ex. gcc -shared -o libhello.so -fPIC hello.c
    #process = subprocess.Popen('gcc -shared -o ../flaskAPI/py/pkl/'+ _id + '/' + modelName + '.so -fPIC ./c/' + _id + '/' + modelName + '.c', shell=True, stdout=subprocess.PIPE)
    #process.wait()
    #if process.returncode == 0:
    #    print('compile ' + modelName + '.so sucess.')
    #else:
        #    print('something wrong')
