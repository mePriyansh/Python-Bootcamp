filenames=["1.Raw.txt","2.Data.txt","3.Clean.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)