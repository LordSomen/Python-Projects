'''in this project I am opening a text file which contain
several int numbers , using regex we are adding those num. 
The file can also be find in the repository .....'''

import re


if __name__  == '__main__':
    fpen  =  open("SUM: 445833","r");
    temp  = []
    for line in fpen:
        numlist  =  re.findall("[0-9]+",line);
        if(len(numlist)  !=  0):
            for i in numlist:
                temp.append(int(i))
    print(sum(temp));
        
    fpen.close();

