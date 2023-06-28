import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('logWin.py', # working fine!
             #'logKeys.py', # NOT working, still giving an error and I don't need it
             #'logFocus.py', # NOT working, some error :/
             'PyAutomate.py',
             'logTyping.py' # working to record type speed and acc each day
             )                                    
                                                                   
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)  
pool.map(run_process, processes)  


