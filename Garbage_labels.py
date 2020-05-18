import operator

BLUEBIN = ["Beverage can", "Coca Cola", "Cola", "Drink", "Aluminum can", 'Can', 'Cardboard', 'Box',
           'Bottle', 'Water Bottle', 'Glass Bottle', 'Cup', 'Packaging and labeling', 'Drink',
           'Juice', 'Paper', 'Paper Product', 'Origami', 'Energy drink', 'Carbonated soft drinks',
           'Plastic bottle', 'Coffee cup sleeve', 'Coffee cup', 'Textile', 'Glass', 'Subway', 'Popeyes',
           'Material property', 'Cardboard' ]


BLACKBIN = ['Plastic', 'Candy', 'Snack', 'Energy Bar', 'Tableware', 'Cutlery', 'Spoon', 'Fork', 'Material property',
            'Plastic bag', 'Potato chip', 'Junk food', 'Comfort food', 'Food storage containers', 'Styrofoam',
            'Foam', 'Polystyrene', 'Foam food storage containers']

GREENBIN = ['Orange', 'Apple', 'Corn', 'Banana', 'Banana Family', 'Plant', 'Food', 'Vegetable', 'Fruit',
            'Seafood', 'Napkin', 'Used Napkin']

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
            print(label)
            for bluebin in BLUEBIN:
                if(bluebin in label.description):
                        Blue_Results[label.description] = float(label.score)
                        print('blue')
            # Goes through the GREENBIN list
            for greenbin in GREENBIN:
                if(greenbin in label.description):
                        Green_Results[label.description] = float(label.score)
            # Goes through the BLACKBIN list
            for blackbin in BLACKBIN:
                if(blackbin in label.description):
                        Black_Results[label.description] = float(label.score)


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
        print(str(object_detected) + '    ' + str(object_confidence))

        Label_dict = None
        
##    print(object_detected)
##    print(bincolor)
##    print(object_confidence)
    
    return object_detected, bincolor, object_confidence
