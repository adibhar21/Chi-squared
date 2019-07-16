#Purpose:   This program is used to test the chi-square test of independence between two languages - french and english.


import codecs
import sys
import math
if len(sys.argv)>3 or len(sys.argv)<3:
    print('ERROR : Two parameters are required, please enter two parameters') #accepts only two arguments error handling
    sys.exit()
else:
    file_1 = sys.argv[1] #equating parameter to variables
    file_2 = sys.argv[2]
    file_list = [file_1,file_2]    #list of name of files
    list_of_values = []
    vowels = ['a','e','i','o','u','é','â','ê','î','ô','û','à','è','ù','ë','ï','ü'] # english/french vowels list (python3 accepts this)

def function():
    list = []     # list of values to be returned to the function call
    total_letters = 0
    percent_vowels = 0
    print('\nbook 1 :',file_1,'\n\nbook 2 : ',file_2)
    for file in file_list:                          # reading each file from file_list
        no_of_vowels=0                              # initializing varaiables
        no_of_consonants=0
        no_of_lines=0
        total_characters = 0
        with codecs.open( file_2, "r", "ISO-8859-1" ) as f:    #using codecs library
          for line in f:                                 #reading each line
            lower_line = line.lower()                   #converting each line to lower case
            for character in range(len(line)):           #reading each character
                     if lower_line[character].isalpha():  #checking if each character is an alphabet
                        flag = 0   #this flag variable is used to identify vowels and consonants in control structure                        
                        for char_vowels in vowels:
                            if char_vowels in lower_line[character]: #comparing if each vowel is equal to each character in the line
                               flag = 1       #flag set to one if vowel
                               no_of_vowels+=1 #counting vowels
                        if flag!=1:
                           no_of_consonants+=1 #counting consonants
            total_characters+=character      
            no_of_lines+=1 #counting lines
             #counting characters
            
        total_letters = no_of_vowels + no_of_consonants
        percent_vowels = (no_of_vowels/total_letters)*100 #percentage of vowels present
        list.extend([no_of_vowels,no_of_consonants,no_of_lines,total_letters,percent_vowels,total_characters+1]) #list of all relevant values to be returned 
    
    return(list)   #returnign the list of values
    
list_of_values = function()
list_expected =[]
matrix_result = (list_of_values[0]+list_of_values[6])+(list_of_values[1]+list_of_values[7])
expected_1 = ((list_of_values[0]+list_of_values[6])/matrix_result)*(list_of_values[0]+list_of_values[1]) #calculating all expected values of chi-square
expected_2 = ((list_of_values[0]+list_of_values[6])/matrix_result)*(list_of_values[6]+list_of_values[7])
expected_3 = ((list_of_values[1]+list_of_values[7])/matrix_result)*(list_of_values[0]+list_of_values[1])
expected_4 = ((list_of_values[1]+list_of_values[7])/matrix_result)*(list_of_values[6]+list_of_values[7])
print("\nbook 1:")
print("\nTotal vowels - ",list_of_values[0],"\nTotal consonants - ",list_of_values[1],"\nTotal letters - ",list_of_values[3],"\nPercent of vowels - {0:.2f}".format(list_of_values[4]),"\nTotal characters - ",list_of_values[5],"\nTotal lines - ",list_of_values[2])
print("\nbook 2:")
print("\nTotal vowels - ",list_of_values[6],"\nTotal consonants - ",list_of_values[7],"\nTotal letters - ",list_of_values[9],"\nPercent of vowels - {0:.2f}".format(list_of_values[10]),"\nTotal characters - ",list_of_values[11],"\nTotal lines - ",list_of_values[8])
print("\nSystem utilities used : wc -m, wc -l, wc")
print("\n\nObserved values:\n")
print("          Vowels"+"     Consonants")
print("book 1 : ",list_of_values[0],"   ",list_of_values[1])
print("book 2 : ",list_of_values[6],"   ",list_of_values[7],"\n\n")
print("Expected values:\n")
print("         Vowels"+"      Consonants")
print("book 1 : "+"{0:.2f}".format(expected_1)+"   {0:.2f}".format(expected_3))
print("book 2 : "+"{0:.2f}".format(expected_2)+"   {0:.2f}\n\n".format(expected_4))
chi_square = (math.pow((list_of_values[0]-expected_1), 2)/expected_1) + (math.pow((list_of_values[6]-expected_2), 2)/expected_2) + (math.pow((list_of_values[1]-expected_3), 2)/expected_3) + (math.pow((list_of_values[7]-expected_4), 2)/expected_4) 
print("Chi-square test : {0:.2f}".format(chi_square))
print('\nConclusion : The result is significant and we are dealing with dependent variables. The p-value is < 0.00001,hence the null hypothesis is rejected.')