import random
import io

refranes_file = "REFRANES.txt"

def random_line():
    with open(refranes_file, 'r', encoding='utf8') as afile:
        line = next(afile)
        for num, aline in enumerate(afile, 2):
          if random.randrange(num): continue
          line = aline
        return line

def mix_refranes_commas():
    '''
    This funnction need that REFRANES.txt contains refranes with commas.
    refran 1: aaaaaaaa,bbbbbb.
    refran 2: cccccccc,dddddd.
    mix_refran = aaaaaaaa, dddddd.
    '''
    refran_1 = random_line()
    while(not(',' in refran_1)):
        refran_1 = random_line()

    refran_2 = random_line()
    while(not(',' in refran_2)):
        refran_2 = random_line()

    part_1 = refran_1[:refran_1.find(",")+1]
    part_2 = refran_2[refran_2.find(",")+1:]
    part_2 = part_2.lower()
    mix_refran = part_1+""+part_2    
    mix_refran=mix_refran.replace('\n','')
    return(mix_refran)

def get_cool_refran():    
    return mix_refranes_commas()

      
    
    
    
    
    
