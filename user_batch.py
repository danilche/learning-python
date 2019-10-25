def main():
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    import tkinter
    root = tkinter.Tk()
    root.withdraw()
    inputFileName = askopenfilename()
    outFileName = asksaveasfilename()
    inFile = open(inputFileName, "r")
    outFile = open(outFileName, "w")
    for line in inFile:
        first, last = line.split()
        uname = (first[0]+last).lower()
        print(uname, file=outFile)
    inFile.close()
    outFile.close()
    

main()