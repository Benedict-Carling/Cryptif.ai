from pycipher import Caesar


######################################### Caeser Cipher Encryption  ###################################

def Caesar_Enc(plaintext,key):
    ciphertext = Caesar(key).encipher(plaintext)
    return ciphertext



######################################### ROT13 ENCRYPTION & DECRYPTION ###############################

def ROT13_Enc_Dec(plaintext):
    ciphertext = Caesar(13).encipher(plaintext)
    return ciphertext


######################################## ATBASH ENC & DEC  ############################################
from pycipher import Atbash

def ATBASH_Enc_Dec(plaintext):
    ciphertext = Atbash().encipher(plaintext)
    return ciphertext


######################################### AFFINE ENCRYPTION  ##########################################
from pycipher import Affine

def AFFINE_Enc(plaintext,key_mult,key_add):
    ciphertext = Affine(key_mult,key_add).encipher(plaintext)
    return ciphertext


########################################## VIGENERE ENCRYPTION  #######################################
from pycipher import Vigenere

def VIGENERE_Enc(plaintext,key_phrase):
    ciphertext = Vigenere(key_phrase).encipher(plaintext)
    return ciphertext


########################################### AUTOKEY ENCRYPTION  #######################################
from pycipher import Autokey

def AUTOKEY_Enc(plaintext,key_phrase):
    ciphertext = Autokey(key_phrase).encipher(plaintext)
    return ciphertext


############################################ BEAUFORT ENCRYPTION  ######################################
from pycipher import Beaufort

def BEAUFORT_Enc(plaintext,key_phrase):
    ciphertext = Beaufort(key_phrase).encipher(plaintext)
    return ciphertext

############################################## ADFGX ENCYPTION  ########################################
from pycipher import ADFGX

#Key is a 5x5 grid of all letter excluding j
#keyword is any keyphrase

def ADFGX_Enc(plaintext,key_matrix,key_phrase):
    ciphertext = ADFGX(key_matrix,key_phrase).encipher(plaintext)
    return ciphertext


############################################## ADFGVX ENCYPTION  ########################################
from pycipher import ADFGVX

#Key is a 6x6 of exclusively a-z & 0-9
#keyword is any keyphrase

def ADFGVX_Enc(plaintext,key_matrix,key_phrase):
    ciphertext = ADFGVX(key_matrix,key_phrase).encipher(plaintext)
    return ciphertext


############################################## BIFID ENCYPTION  ########################################
from pycipher import Bifid

#fractionating key cipher

#Key is a 5x5 of all alphabet without j
#key_period a single integer

def BIFID_Enc(plaintext,key_matrix,key_integer):
    ciphertext = Bifid(key_matrix,key_integer).encipher(plaintext)
    return ciphertext

############################################## COLUMNAR TRANSPOSITIONAL ENCYPTION  ########################################
from pycipher import ColTrans

#transpositional cipher
#Key_word is any string

def COLTRANS_Enc(plaintext,key_word):
    ciphertext = ColTrans(key_word).encipher(plaintext)
    return ciphertext

#print (COLTRANS_Enc(plaintext,'gio'))

############################################## 4 SQUARE ENCYPTION  ########################################

############################################## RAILFENCE ENCYPTION  ########################################
from pycipher import Railfence

def RAILFENCE_Enc(plaintext,key_int):
    ciphertext = Railfence(key_int).encipher(plaintext)
    return ciphertext

#print (RAILFENCE_Enc(plaintext,3))

############################################### PORTA ENCRYPTION  ###########################################
from pycipher import Porta

def PORTA_Enc(plaintext,key_phrase):
    ciphertext = Porta(key_phrase).encipher(plaintext)
    return ciphertext

#print (PORTA_Enc(plaintext,'gio'))

############################################### POLYBIUS SQUARE ENCRYPTION  ###########################################
#needs the fixings




