from base64 import standard_b64decode , standard_b64encode
import hashlib
from colorama import init, Fore
import os
#CIPHY MERCAD (@Sadult) Edition / Github.com/Sadult
#Code By why-py | Design by Sadult
# Colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


help_message = f'''{GREEN}

~[ HELP ]
{GRAY}
*CIPHY ENCODING/DECODING/HASHING TOOL version(1.1.0)*

ciphy is an open source simple but powerful tool for encoding, decoding and hashing data.
it's written by why-py(Mobin).

[+] Github.com/why-py/
[+] t.me/unicpython

{GREEN}
~[ COMMANDS ]

   {GRAY} ======================================================{GREEN}
     *encoding and decoding commmands*
  {GREEN}
        > Base64{GRAY}
            Encoding:                b64 -encode [text]
            Decoding:                b64 -decode [ciphertext]
        {GREEN}> ROT-13 (shift value = 13){GRAY}
            Encoding & Decoding:             rot13 [text]
  ======================================================   {GREEN}
     *Hashing commands*
	 {GRAY}
           {GREEN}SHA1{GRAY}      >     sha1 [text
           {GREEN}SHA256{GRAY}    >     sha256 [text]
           {GREEN}MD5 {GRAY}      >     md5 [text]
  ======================================================   {GREEN}
     *other options*
     
     -so  [path]{GRAY}                  (SaveOutput)saves only output into the given .txt file path.

     {GREEN}-sa  [path]{GRAY}                  (SaveAll)saves all the i/o into the given .txt file path.

     example:
                md5 -sa C:/users/mobin/Desktop/output.txt hello
                
{RESET}'''


def rot13(str_in : str):

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    shift = 13

    n = len(str_in)

    str_out = ''

    for i in range(n):

        c = str_in[i]

        if c not in alpha:
            str_out += c

        else:

            loc = alpha.find(c)

            new_loc = (loc + shift) % 26 

            str_out += alpha[new_loc]

    return str_out




def main():
    
    

    

    stdin = input('CIPHY>>>')

    if stdin == '--help' or stdin == '--Help' or stdin =='--HELP' or stdin =='-h' or stdin =='-H':

        print(help_message)
        
        

    elif stdin[0:3] == 'md5' or stdin[0:3] == 'Md5' or stdin[0:3] == 'MD5': #MD5
        

        if '-so' in stdin:
            
            try:

                text = stdin.split('.txt')[1].replace(' ','')

                cipher = hashlib.md5(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-so')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')

            try:
                with open(file_name,'w') as f:
                    f.write('md5 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')
            

        elif '-sa' in stdin:
            try:

                text = stdin.split('.txt')[1].replace(' ','')

                cipher = hashlib.md5(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-sa')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')


            try:
                with open(file_name,'w') as f:
                    f.write('input : '+text+'\nmd5 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')
            
        else:
            try:
                text = stdin.split(stdin[0:3])[1].replace(' ','')

                cipher = hashlib.md5(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

            except:
                print('something is wrong !')


        
        





    elif stdin[0:6] == 'sha256' or stdin[0:6] == 'Sha256' or stdin[0:6] == 'SHA256':#sha256
       

        if '-so' in stdin:
            
            try:

                text = stdin.split('.txt')[1].replace(' ','')

                cipher = hashlib.sha256(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-so')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')

            try:
                with open(file_name,'w') as f:
                    f.write('sha256 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')




        elif '-sa' in stdin:
            try:

                text = stdin.split('.txt')[1].replace(' ','')

                cipher = hashlib.sha256(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-sa')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')


            try:
                with open(file_name,'w') as f:
                    f.write('input : '+text+'\nsha256 output : '+cipher)

            except:
                print('could not create the output file;check the entered path and try again.\n')
            
        else:
            try:
                text = stdin.split(stdin[0:6])[1].replace(' ','')

                cipher = hashlib.sha256(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

            except:
                print('something is wrong !')
        



    elif stdin[0:4] == 'sha1' or stdin[0:3] == 'Sha1' or stdin[0:3] == 'SHA1':



        if '-so' in stdin:
            
            try:

                text = stdin.split('.txt')[1].replace(' ','')
                print(text)

                cipher = hashlib.sha1(text.encode()).hexdigest()


                file_name = stdin.split('-so')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')

            try:
                with open(file_name,'w') as f:
                    f.write('sha1 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')
            

        elif '-sa' in stdin:
            try:

                text = stdin.split('.txt')[1].replace(' ','')

                cipher = hashlib.sha1(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-sa')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')


            try:
                with open(file_name,'w') as f:
                    f.write('input : '+text+'\nsha1 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')
            
        else:
            try:
                text = stdin.split(stdin[0:4])[1].replace(' ','')
                print(text)

                cipher = hashlib.sha1(text.encode()).hexdigest()

                print('Output:\n\n'+cipher)

            except:
                print('something is wrong !')


        



    elif stdin[0:5] == 'rot13' or stdin[0:5] == 'Rot13' or stdin[0:5] == 'ROT13': #ROT-13


        if '-so' in stdin:
            
            try:
                
                text = stdin.split('.txt')[1].replace(' ','')

                cipher = rot13(text.upper())

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-so')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')

            try:
                with open(file_name,'w') as f:
                    f.write('ROT-13 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')
            

        elif '-sa' in stdin:
            try:

                text = stdin.split('.txt')[1].replace(' ','')

                cipher = rot13(text.upper())

                print('Output:\n\n'+cipher)

                file_name = stdin.split('-sa')[1].replace(text,'')
                file_name = file_name.replace(' ','')

            except:
                print('something is wrong !')


            try:
                with open(file_name,'w') as f:
                    f.write('input : '+text+'\nROT-13 output : '+cipher)
            except:
                print('could not create the output file;check the entered path and try again.\n')
            
        else:
            try:
                text = stdin.split(stdin[0:5])[1].replace(' ','')

                cipher = rot13(text.upper())

                print('Output:\n\n'+cipher)

            except:
                print('something is wrong !')


               






    elif stdin[0:3] == 'b64' or stdin[0:3] == 'B64' :#BASE64
        


        if '-encode' in stdin:

            if '-so' in stdin:
                try:
                
                    text = stdin.split('-so')[1].replace(' ','')

                    cipher = standard_b64encode(text.encode()).decode()

                    print('Output:\n\n'+cipher)

                    file_name = stdin.split('-so')[1].replace(text,'')
                    file_name = file_name.replace(' ','')
                except:
                    print('something is wrong !')

                try:
                    with open(file_name,'w') as f:
                        f.write('Base64 encoded output : '+cipher)
                except:
                    print('could not create the output file;check the entered path and try again.\n')




            elif '-sa' in stdin:

                try:
                
                    text = stdin.split('-sa')[1].replace(' ','')

                    cipher = standard_b64encode(text.encode()).decode()

                    print('Output:\n\n'+cipher)

                    file_name = stdin.split('-sa')[1].replace(text,'')
                    file_name = file_name.replace(' ','')
                except:
                    print('something is wrong !')

                try:
                    with open(file_name,'w') as f:
                        f.write('input : '+text+'\nBase64 encoded output : '+cipher)
                except:
                    print('could not create the output file;check the entered path and try again.\n')
            

            else:
                try:
                    text = stdin.split('encode')[1].replace(' ','')

                    cipher = standard_b64encode(text.encode()).decode()

                    print('Output:\n\n'+cipher)

                except:
                    print('something is wrong !')





                
        elif '-decode' in stdin:

            if '-so' in stdin:
                try:
                
                    cipher = stdin.split('-so')[1].replace(' ','')

                    text = standard_b64decode(cipher.encode()).decode()

                    print('Output:\n\n'+text)

                    file_name = stdin.split('-so')[1].replace(cipher,'')
                    file_name = file_name.replace(' ','')
                except:
                    print('something is wrong !')

                try:
                    with open(file_name,'w') as f:
                        f.write('Base64 decoded output : '+text)
                except:
                    print('could not create the output file;check the entered path and try again.\n')




            elif '-sa' in stdin:

                try:
                
                    cipher = stdin.split('-sa')[1].replace(' ','')

                    text = standard_b64decode(cipher.encode()).decode()

                    print('Output:\n\n'+text)

                    file_name = stdin.split('-so')[1].replace(cipher,'')
                    file_name = file_name.replace(' ','')
                except:
                    print('something is wrong !')

                try:
                    with open(file_name,'w') as f:
                        f.write('input : '+cipher+'\nBase64 decoded output : '+text)
                except:
                    print('could not create the output file;check the entered path and try again.\n')
            

            else:
                try:
                    cipher = stdin.split('decode')[1].replace(' ','')
                    

                    text = standard_b64decode(cipher.encode()).decode()
                    
                    print('Output:\n\n'+text)

                except:
                    print('something is wrong !')



        else:
            print('something is wrong !')
        

    else:
        print('Wrong Command.\n\n')




    main()   
os.system('clear')
print(f'''{GREEN}

 _____ ___________ _   ___   __
/  __ \_   _| ___ \ | | \ \ / /
| /  \/ | | | |_/ / |_| |\ V / 
| |     | | |  __/|  _  | \ /  
| \__/\_| |_| |   | | | | | |  
 \____/\___/\_|   \_| |_/ \_/  
                               
''')
print(f'''{GRAY}					   


CIPHY v1.1 
  ├ Coded By:
  ┊   ├ Design : T.me/Sadult + Github.com/Sadult
  ┊   └ CODE : T.me/unicpython + Github.com/why-py
  ┊   
  └ INFO:
	   [+]  simple text encoding/decoding/Hashing tool.
	   [+]  type -h or --help for help and more info. 
		

{RESET}''')

if __name__ == '__main__':

    main()
