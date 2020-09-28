#%%
import json
import requests
import os

def verify_plugin(item):
    if(item in update_center['plugins']): 
        p = update_center['plugins'][item]
        r = get_donwload(item, base_core, p['url'])
        print('{:30} {}'.format(item, r))
        verify_dep(p['dependencies'])


def verify_dep(lista):
    for d in lista:
        item = d['name']
        if(item in update_center['plugins']): 
            p = update_center['plugins'][item]
            r = get_donwload(item, base_core, p['url'])
            print(' - {:27} {}'.format(item, r))
            verify_dep(p['dependencies'])


def get_donwload(name, core_version, url):
    instalado.append(name)
    file_name = "./plugins/{}/{}.hpi".format(core_version, name)
    if(not os.path.exists(file_name)):
        r = requests.get(url, allow_redirects=True, verify=True)
        open(file_name, 'wb').write(r.content)
        return 'Downloading...'
    else:
        return 'Downloaded'


#base_core=2.0190
base_core='2.19.4'
plugins_dir = "./plugins/2.19.4"
update_center = {}
install={}
instalado=[]

with open(plugins_dir+'/update-center.json', 'r') as json_file: 
    json_str = json_file.readlines()[1]
    update_center = json.loads(json_str)


with open('./install-config.json', 'r') as json_file:
    install = json.load(json_file)

#criar Diretorio
if(not os.path.exists(plugins_dir)):
    os.makedirs(plugins_dir)

for item in install['install']:
    verify_plugin(item)
    print()

#print(instalado)





#for plugin in update_center['plugins']:
#    core_list = update_center['plugins'][plugin]['requiredCore'].split('.')
#    core_str = '{}.{:0>3d}{:0>1d}'.format(core_list[0],int(core_list[1]), int(core_list[2]) if len(core_list)==3 else 0)
#    core = float('{:.4f}'.format(float(core_str)))
#    #print('{:.4f} => {}'.format(core, update_center['plugins'][plugin]['requiredCore']))
#    if(core >  base_core):
#        print("{}:{}                {}".format(plugin,update_center['plugins'][plugin]['requiredCore'],core))
#        for dep in update_center['plugins'][plugin]['dependencies']:
#            print("\t - {}:{}".format(dep['name'],dep['version']))



