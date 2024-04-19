filenames=['file1.txt','file2.txt','file3.txt']

filenames=[filenames.replace('.','-')+'.txt' for filenames in filenames]

print(filenames)