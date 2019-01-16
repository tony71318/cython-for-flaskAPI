import base64, platform, subprocess, os

_id = '1002010002'
pkl_name_list = ['one', 'two', 'three', 'four', 'five', 'six', 'features', 'num_previous']

if platform.system() == 'Windows':
    for pkl_name in pkl_name_list:
        with open('pkl/' + pkl_name + '.pkl', 'rb') as f:
            byteArray = f.read()

        enc_byteArray = base64.b64encode(byteArray)

        with open(pkl_name + '.py', 'w') as f:
            f.write('#cython: language_level=3\n')
            if pkl_name == 'features':
                f.write('enc_features = ' + str(enc_byteArray))
            elif pkl_name == 'num_previous':
                f.write('enc_num_previous = ' + str(enc_byteArray))
            else:
                f.write('enc_model = ' + str(enc_byteArray))
                
            f.close()

        process = subprocess.Popen('python setup.py ' + pkl_name + ' build_ext --inplace', shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('build pyd success.')
        else:
            print('something wrong')

        process = subprocess.Popen('rm ' + pkl_name + '.py', shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('delete ' + pkl_name + '.py sucess.')
        else:
            print('something wrong')

        id_dir = "c/" + _id
        if not os.path.isdir(id_dir):
            os.mkdir(id_dir)
            print("make dir for: " + _id)

        process = subprocess.Popen('mv ' + pkl_name + '.c ' + id_dir, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('move to c_id folder sucess')
        else:
            print('something wrong')

        process = subprocess.Popen('mv ' + pkl_name + '.cp36-win_amd64.pyd ' + pkl_name + '.pyd', shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('rename ' + pkl_name + '.pyd sucess.')
        else:
            print('something wrong')

        id_dir = "pkl/" + _id
        if not os.path.isdir(id_dir):
            os.mkdir(id_dir)
            print("make dir for: " + _id)

        process = subprocess.Popen('mv pkl/' + pkl_name + '.pkl ' + id_dir, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('move to pkl_id folder sucess.')
        else:
            print('something wrong')

        id_pyd_dir = "./web_taipower/py/pkl/" + _id
        if not os.path.isdir(id_pyd_dir):
            os.mkdir(id_pyd_dir)
            print("make dir for: " + _id)

        process = subprocess.Popen('mv ' + pkl_name + '.pyd ' + id_pyd_dir, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('move to web_taipower sucess.')
        else:
            print('something wrong')
else:
    for pkl_name in pkl_name_list:
        # ex. gcc -shared -o libhello.so -fPIC hello.c
        process = subprocess.Popen('gcc -shared -o ../flaskAPI/py/pkl/'+ _id + '/' + pkl_name + '.so -fPIC ./c/' + _id + '/' + pkl_name + '.c', shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('compile ' + pkl_name + '.so sucess.')
        else:
            print('something wrong')