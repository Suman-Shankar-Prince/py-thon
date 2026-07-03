
import subprocess as sp  
import threading
import time 


try:
    f =open(input('input result file name \n')+'.csv','a')
except:
    print('error in resultant files')
    
# open a file load the site
t = time.time()
try:
    with open(input('give file name\n'),'r') as file:
        site = set([i.strip('\n') for i in file.readlines()])
except Exception as e:
    print(f'exception in file -> {e}')
finally:
    try:
        print(f'total number of site loaded are {len(site)}')
    except:
        print('error in loading file / no site in file')


#
def record(obj:str):
    f.writelines(f'{obj}\n')

def pings(obj:str):
    #print(obj)
    temp = sp.run(['ping',f'{obj}','-n','1'],capture_output=True,text=True)
    #print(temp)
    if temp.returncode ==1:
        if temp.stdout.find('[') != -1:
            print(obj)
            record(obj)

try:
    for pc in site:
        #print(pc)
        building = [f'{pc}-ai00{i}' for i in range(1,10)]+[f'{pc}-ai0{j}' for j in range(10,100)]+[f'{pc}-ai{k}' for k in range(100,1000)]
        #print(building)
        switch=[]
        for device in building:
            switch.append(threading.Thread(target =pings,args=(device,)))
            #print('threads accumulated')
        try:
            for lan in switch:
                try:
                    lan.start()
                except Exception as e:
                    print(f'error in marking pc {e}')
            for wire in switch:
                wire.join()
        except Exception as e:
            print(f'error in switch threads {e}')
        finally:
            switch.clear()
        

except Exception as e:
    print(f'error in loading pc {e}')
finally:
    _t = time.time()
    print(f'time taken to perform task = {_t - t}')

try:
    f.close()
except Exception as e:
    print(f'no such file {e}')
finally:
    print('programme closed')

 





