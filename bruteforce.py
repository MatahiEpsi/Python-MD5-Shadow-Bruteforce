import multiprocessing as mp
import hashlib
import itertools
import time




#possible characters in user password
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.;#@")
#minimum password value
CharLength = 6

#getting passwords and username from shadow file
with open("shadow_test", "r") as ins:
    array = []
    users = []
    passwd = []
    #getting everyline from shadow file into an array
    for line in ins:
        array.append(line)
    #saving only username and passwords
    for pw in array:
        str(pw)
        r= pw.split(":")
        users.append(r[0])
        passwd.append(r[1])
    # print(users)
    # print(passwd)

    list = []
    #removing passowrd with * or !
    for mdp in passwd:
        start = time.time()
        if mdp != '*' and mdp != '!':
            str(mdp)
            list.append(mdp)
            # trying to Bruteforce
            for _ in range(12):
                passwords = (''.join(word) for word in itertools.product(Alphabet, repeat=CharLength))

                #print(*passwords)
                for pswd in passwords:
                    hash_object = hashlib.md5(str.encode(pswd)).hexdigest()
                    # hash_object.update(*passwords.encode('utf-8'))
                    generatedpassword = '$1$' + hash_object
                    # print(generatedpassword)

                    for compare in list:
                        for user in users:
                            #print('on cherche le Mot de passe : ' + compare +' pour ' +user)
                            #print('mot de passe MD5 généré : ' +generatedpassword)
                            #print('mot de passe clair généré : ' +pswd)


                            if generatedpassword == compare:
                                end = time.time()
                                print('Le Mot de passe pour ' + user + ' est : ' + pswd )
                                print(print(end - start))


    #print(list)

