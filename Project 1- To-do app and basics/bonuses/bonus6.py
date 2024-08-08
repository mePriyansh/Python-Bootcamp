contents=["ABC","DEF","GHI"]

filenames=["file1.txt","file2.txt","file3.txt"]

for content,filename in zip(contents,filenames):
    file=open(f"file/{filename}","w")
    file.write(content)