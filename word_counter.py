#chars, words and lines counter from a file

from tkinter.filedialog import askopenfilename
import tkinter
def main():
    
    #This section counts number of all characters in a file, 
    #including spaces.
    
    root = tkinter.Tk()
    root.withdraw()
    file1 = askopenfilename()
    with open(file1) as path1:
        my_file1 = path1.read()
    my_list1 = []
    
  
    for line in my_file1:
        my_list1.append(line)
    lgt1 = len(my_list1)
    print("Your file has {} characters".format(lgt1))
    
    #This section counts number of all words in a file
    
    file2 = askopenfilename()
    with open(file2) as path2:
        my_file2 = path2.read()
    my_list2 = []
    
  
    for j in my_file2:
        my_list2 = my_file2.split()
    lgt2 = len(my_list2)
    
    print("Your file has {} words".format(lgt2))
    
    #This section counts number of all lines in a file
    
    file3 = askopenfilename()
    with open(file3) as path3:
        my_file3 = path3.readlines()
        
    for x, line in enumerate(my_file3):
        pass
        
    print("Your file has {} lines".format(x + 1))
    
    
    
main()