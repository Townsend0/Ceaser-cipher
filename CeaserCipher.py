logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
f=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def crypt(a,b,f,c):
    g=""
    for d in b:
        if d in f:
            if a=='encode':
                g+=f[(f.index(d)+c)%26]
            else:
                g+=f[(f.index(d)-c+26)%26]
        else:
            g+=d
    print(f'\nhere is the {a}d messege: {g}')
e='y'
print(logo)
while e=='y':
    b=[]
    a=input('\ntype "encode" to encrypte, type "decode" to decrypte: ').lower()
    while a!='encode' and a!='decode':
        a=input('\n( Invalid input! ) type "encode" to encrypte, type "decode" to decrypte: ').lower()
    b+=input('\ntype your messege: ').lower()
    c=input('\nType the shift number: ')
    while not c.isnumeric():
        c=input('\n( Invalid input shift number must be a positive integer ) enter the shift number: ')
    crypt(a,b,f,int(c))
    e=input('\nPress y if you want to enter another messege: ').lower()