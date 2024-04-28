import argparse, datetime

parser = argparse.ArgumentParser(description= "testarg",add_help = True)
parser.add_argument('filename',nargs='?',default='file.txt', help="File name of the file ")
#parser.add_argument('-c','--copy',dest='nes_dest', metavar="N",
                   # type=datetime.date.fromisoformat,action= 'store',help='Make N copy')
parser.add_argument('-c','--copy',dest='nes_dest', metavar="N",
                    type=int,action= 'store',help='Make N copy')
#parser.add_argument('-s','--something',action='store_const',const=15)
parser.add_argument('-f','--flag',action='store_false')
parser.add_argument('-v','--version',action='version',version='programParser v1.0')
parser.add_argument('-n','--name',default='file_copy',choices=['name1','name2'])
arguments = parser.parse_args()
#print(arguments.filename)
print(arguments)
