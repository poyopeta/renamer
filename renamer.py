import os
cd = os.getcwd() #pythonファイルがあるディレクトリ. この中にあるファイルが対象
if os.path.isfile(cd+'/.DS_Store'): #ゴミ
    os.remove(cd+'/.DS_Store')
target = os.listdir(cd)
temp_log = '' #rename log
i = 1 #単純にナンバリング
for item in target:
    if os.path.isfile(item) and item != __file__ and item != '.rename_log':
        #itemがディレクトリではなく、かつ自身かlogではない場合
        get_ext = os.path.splitext(item)
        item_cdir = os.path.join(cd,item) #現在のフルアドレス
        item_ndir = os.path.join(cd,str(i) + get_ext[1]) #文字列の結合 rename後のアドレス
        os.rename(item_cdir,item_ndir)
        temp_log += item + ' >>> ' + str(i) + get_ext[1] + '\n'
        i += 1
print('done!')
log_dir = os.path.join(cd,'.rename_log')
with open(log_dir, mode='w') as f:
    f.write(temp_log)