import pyperclip

lista = []

with open('origin.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        # Exemplu de ce facem rstirp:
        # >>> 'test string\n'.rstrip() => 'test string'
        lista.append(line.rstrip())


lista_txt = str(lista)
pyperclip.copy(lista_txt)

# try:		
# 	with open("z_new_list.txt", "a") as myfile:
# 	    myfile.write(list(lista))
# except:
# 	print(fail)
