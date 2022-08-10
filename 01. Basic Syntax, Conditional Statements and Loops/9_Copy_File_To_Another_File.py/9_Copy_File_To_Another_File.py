from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} tp {to_file}")

in_file = open(from_file).read()

print(f"The input file is {len(in_file)} bytes long.")

print(f"does the output file exist? {exists(to_file)}")
print("Read, hit RETURN to continue CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done")

out_file.close()


