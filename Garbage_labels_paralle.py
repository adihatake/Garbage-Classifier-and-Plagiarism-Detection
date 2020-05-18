import operator
from multiprocessing import Process
from Bins import BLUEBIN, BLACKBIN, GREENBIN
from Bins import Bluebin1, Bluebin2, Bluebin3, Bluebin4, Bluebin5, Bluebin6
from Bins import Blackbin1, Blackbin2, Blackbin3, Blackbin4
from Bins import Greenbin1, Greenbin2, Greenbin3

def find_in_bin(label, BIN, Results):
    for bn in BIN:
        if(bn in label.description and float(label.score) > 0.5):
                Results[label.description] = float(label.score)
                if(float(label.score) > 0.75):
                    break

def find_in_bluebin(label, Blue_Results):
    find_in_bin(label,BLUEBIN, Blue_Results)
    
def find_in_blackbin(label, Black_Results):
    find_in_bin(label,BLACKBIN, Black_Results)

def find_in_greenbin(label, Green_Results):
    find_in_bin(label,GREENBIN, Green_Results)

def find_in_bluebin1(label, Blue_Results):
    find_in_bin(label,Bluebin1, Blue_Results)

def find_in_bluebin2(label, Blue_Results):
    find_in_bin(label,Bluebin2, Blue_Results)

def find_in_bluebin3(label, Blue_Results):
    find_in_bin(label,Bluebin3, Blue_Results)    

def find_in_bluebin4(label, Blue_Results):
    find_in_bin(label,Bluebin4, Blue_Results)

def find_in_bluebin5(label, Blue_Results):
    find_in_bin(label,Bluebin5, Blue_Results)    

def find_in_bluebin6(label, Blue_Results):
    find_in_bin(label,Bluebin6, Blue_Results)
    
    
    

def find_in_blackbin1(label, Black_Results):
    find_in_bin(label,Blackbin1, Black_Results)

def find_in_blackbin2(label, Black_Results):
    find_in_bin(label,Blackbin2, Black_Results)
    
def find_in_blackbin3(label, Black_Results):
    find_in_bin(label,Blackbin3, Black_Results)

def find_in_blackbin4(label, Black_Results):
    find_in_bin(label,Blackbin4, Black_Results)



def find_in_greenbin1(label, Green_Results):
    find_in_bin(label,Greenbin1, Green_Results)
    
def find_in_greenbin2(label, Green_Results):
    find_in_bin(label,Greenbin2, Green_Results)

def find_in_greenbin3(label, Green_Results):
    find_in_bin(label,Greenbin3, Green_Results)
    
    
##def find_in_greenbin(label, Green_Results):
##    find_in_bin(label,GREENBIN, Green_Results)
##
##def find_in_blackbin(label, Black_Results):
##    find_in_bin(label,BLACKBIN, Black_Results)
                
def find_in_all_bins(label, Blue_Results, Green_Results, Black_Results):
    pblue = Process (target=find_in_bluebin(label, Blue_Results))
    pblue.start()

    pblack = Process (target=find_in_blackbin(label, Black_Results))
    pblack.start()

    pgreen = Process (target=find_in_greenbin(label, Green_Results))
    pgreen.start()
    
##    pblue1 = Process (target=find_in_bluebin1(label, Blue_Results))
##    pblue1.start()
##    pblue2 = Process (target=find_in_bluebin2(label, Blue_Results))
##    pblue2.start() 
##    pblue3 = Process (target=find_in_bluebin3(label, Blue_Results))
##    pblue3.start()
##    pblue4 = Process (target=find_in_bluebin4(label, Blue_Results))
##    pblue4.start()
##    pblue5 = Process (target=find_in_bluebin5(label, Blue_Results))
##    pblue5.start()
##    pblue6 = Process (target=find_in_bluebin6(label, Blue_Results))
##    pblue6.start()

##
##    pblack1 = Process (target=find_in_blackbin1(label, Black_Results))
##    pblack1.start()
##    pblack2 = Process (target=find_in_blackbin1(label, Black_Results))
##    pblack2.start()
##    pblack3 = Process (target=find_in_blackbin1(label, Black_Results))
##    pblack3.start()
##    pblack4 = Process (target=find_in_blackbin1(label, Black_Results))
##    pblack4.start()
##
##
##    pgreen1 = Process (target=find_in_greenbin1(label, Green_Results))
##    pgreen1.start()
##    pgreen2 = Process (target=find_in_greenbin2(label, Green_Results))
##    pgreen2.start()
##    pgreen3 = Process (target=find_in_greenbin3(label, Green_Results))
##    pgreen3.start()

    
##    pgreen = Process (target=find_in_greenbin(label, Green_Results))
##    pgreen.start()
##    pblack = Process (target=find_in_blackbin(label, Black_Results))
##    pblack.start()
    pblue.join()
    pblack.join()
    pgreen.join()
##    #pblue1.join()
##    pgreen1.join()
##    pblack1.join()
##
##    #pblue2.join()
##    pgreen2.join()
##    pblack2.join()
##
##    #pblue3.join()
##    pgreen3.join()
##    pblack3.join()
##
##    #pblue4.join()
##    #pblack4.join()
##
##    #pblue5.join()
##    #pblue6.join()
    
        
def get_labels(labels):
    object_detected = 'Unknown'
    object_confidence = 0
    bincolor = 'Unknown'
    Green_entries = 0
    Blue_entries = 0
    Black_entries = 0
    Blue_Results = {}
    Green_Results = {}
    Black_Results = {}
    result_entries = None
    Label_dict_count = None
    
    for label in labels:
            # Goes through the BLUEBIN list
##            print(label)

            find_in_all_bins(label, Blue_Results, Green_Results, Black_Results)

    if 'Napkin' in Green_Results:
        Green_Results['Napkin2'] = 0.9

    elif 'Used Napkin' in Green_Results:
        Green_Results['Used_Napkin2'] = 0.9

    elif 'Foam' in Black_Results:
        Black_Results['Foam2'] = 0.9

    elif 'Styrofoam' in Black_Results:
        Black_Results['Styrofoam2'] = 0.9

    elif 'Polysterene' in Black_Results:
        Black_Results['Polysterene'] = 0.9

        
    Label_dict_count = {'Blue_entries':  len(Blue_Results),
                  'Black_entries': len(Black_Results), 
                  'Green_entries': len(Green_Results)}

    result= max(Label_dict_count.items(), key=operator.itemgetter(1))
    result_entries = result[0]
    count_result = result[1]


##    print('result_entries')
##    print(count_result)
##    print(sorted(Label_dict_count.items(), key=operator.itemgetter(1)))

    
    
    if count_result == 0:
        object_detected = 'Unknown'
        bincolor = None
        object_confidence = 0
        result_entries = None


    else:
        Label_dict = {
              'Blue_entries':  Blue_Results,
              'Black_entries': Black_Results,
              'Green_entries': Green_Results}
            
        x = sorted(Label_dict.get(result_entries).items(), key=operator.itemgetter(1))
        y = x[-1]
        bincolor = result_entries.split("_")[0]
        object_detected, object_confidence = (y)
##        print(str(object_detected) + '    ' + str(object_confidence))

        Label_dict = None
        
##    print(object_detected)
##    print(bincolor)
##    print(object_confidence)
    
    return object_detected, bincolor, object_confidence
