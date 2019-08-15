#####  <<<------------------------- TO DO LIST  --------------------------------------->>>  ###########
#####  <<<------------------------- DELETE ONCE DONE ---------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<------------------------- Make AI page functional(scroll/background) -------->>>  ###########
#####  <<<------------------------- find a logo online add to corners!!!!!!!! --------->>>  ###########
#####  <<<------------------------- to create keyless we need a summation counter!!!!!->>>  ###########
#####  <<<------------------------- create keyless pages (most probable keys/try again)>>>  ###########
#####  <<<------------------------- create AI for encyption type detection ------------>>>  ###########
#####  <<<------------------------- clean all pages to add commenting ----------------->>>  ###########

#####  <<<------------------------- refactor deep learning and index ------------------>>>  ###########

#####  <<<------------------------- Main file  ---------------------------------------->>>  ###########
#####  <<<------------------------- with app routing ---------------------------------->>>  ###########
#####  <<<------------------------- controls redirection ------------------------------>>>  ###########
#####  <<<------------------------- and which pages exist ----------------------------->>>  ###########


#####  <<<------------------------- Importing ----------------------------------------->>>  ###########

from flask import Flask, session, redirect, url_for, escape, request, render_template
import string as stringFuncs
from decryptionFunctions import *
from ALL_ENCRYPTION import *
from cryptanalysis import *
from keyless import *
from pycipher import *

from knnpractice import knn_my_text_please
#####  <<<------------------------- initial setup ------------------------------------->>>  ###########
#####  <<<------------------------- and secret key ------------------------------------>>>  ###########

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#####  <<<------------------------- Rounting ------------------------------------------>>>  ###########

#####  <<<------------------------- Main pages routing -------------------------------->>>  ###########

#####  <<<------------------------- Index to home ------------------------------------->>>  ###########


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


#####  <<<------------------------- Format Page --------------------------------------->>>  ###########
#####  <<<------------------------- Fully functional and finished --------------------->>>  ###########


@app.route("/format", methods=["GET", "POST"])
def format():
    if request.method == "POST":
        method = request.form["format"]
        C_text = request.form["C_text"]
        if method == "LowerCase":
            return render_template("format.html", Cipher_text=C_text.lower())
        if method == "RemoveSpaces":
            return render_template("format.html", Cipher_text=C_text.replace(" ", ""))
        if method == "RemovePunctuation":
            return render_template(
                "format.html",
                Cipher_text=C_text.translate(str.maketrans("", "", stringFuncs.punctuation)),
            )
        if method == "CompleteFormat":
            return render_template(
                "format.html", Cipher_text=scrub_string(C_text), C_text=C_text
            )

        return render_template("format.html", Cipher_text=dec_rot13(C_text))
    return render_template("format.html")


#####  <<<------------------------- Cryptanalysis Page -------------------------------->>>  ###########
#####  <<<------------------------- Fully functional and finished --------------------->>>  ###########


@app.route("/cryptanalysis", methods=["GET", "POST"])
def cryptanalysis():
    if request.method == "POST":
        Cb_text = scrub_string(request.form["C_text"])
        Ch_text = Cb_text.lower()
        C_text = ''.join([i for i in Ch_text if not i.isdigit()])
        if len(C_text)<2:
            return render_template("cryptanalysis.html", Frequency=frequency_list_generate(""), show_error=1)
        else:
            chi_squared_1 = "{0:.4f}".format(
                chi_square(C_text)
            )
            bhat_1 = "{0:.4f}".format(bhattacharyya(C_text))
            chi_squared_2 = "{0:.2f}".format(
                chi_square_of_bigrams(find_bigrams(C_text))
            )
            bhat_2 = "{0:.2f}".format(
                bhattacharyya_for_bigram(find_bigrams(C_text))
            )
            chi_squared_3 = "{0:.2f}".format(
                chi_square_of_trigrams(find_trigrams(C_text))
            )
            bhat_3 = "{0:.2f}".format(
                bhattacharyya_for_trigram(
                    find_trigrams(C_text))
                )
            

            return render_template(
                "cryptanalysis.html",
                Frequency=frequency_list_generate(C_text),
                IOC=str(IC(C_text, 1)),
                chi_squared_1=chi_squared_1,
                bhat_1=bhat_1,
                chi_squared_2=chi_squared_2,
                bhat_2=bhat_2,
                chi_squared_3=chi_squared_3,
                bhat_3=bhat_3,
            )
    return render_template("cryptanalysis.html", Frequency=frequency_list_generate(""))


#####  <<<------------------------- Deep Learning Home page --------------------------->>>  ###########
#####  <<<------------------------- Still in development with background/scroll ------->>>  ###########


@app.route("/deepLearning", methods=["GET", "POST"])
def deepLearning():
    return render_template("deepLearning1.html")

@app.route("/deepLearningknn", methods=["GET", "POST"])
def deepLearningknn():
    if request.method == "POST":
        C_text = request.form["C_text"]
        return render_template(
            "deepLearningknn.html", Cipher_text=knn_my_text_please(C_text)
        )
    return render_template("deepLearningknn.html")


#####  <<<------------------------- Encyption Home page ------------------------------->>>  ###########
#####  <<<------------------------- finished ------------------------------------------>>>  ###########


@app.route("/encryption", methods=["GET", "POST"])
def encryption():
    return render_template("encryption.html")


#####  <<<------------------------- Decyption Home page ------------------------------->>>  ###########
#####  <<<------------------------- finished ------------------------------------------>>>  ###########


@app.route("/decryption", methods=["GET", "POST"])
def decryption():
    return render_template("decryption.html")


#####  <<<------------------------- Keyless Home page ------------------------------->>>  ###########
#####  <<<------------------------- finished ------------------------------------------>>>  ###########


@app.route("/keyless", methods=["GET", "POST"])
def keyless():
    return render_template("keyless.html")


#####  <<<------------------------- Keyless Decryption home page ---------------------->>>  ###########
#####  <<<------------------------- needs creating with same background as AI --------->>>  ###########


@app.route("/keylessdecryption", methods=["GET", "POST"])
def keylessdecryption():
    return render_template("keylessdecryption.html")


#####  <<<------------------------- ENCYPTION ----------------------------------------->>>  ###########
#####  <<<------------------------- BEGINNING ----------------------------------------->>>  ###########
#####  <<<------------------------- HERE ---------------------------------------------->>>  ###########
#####  <<<------------------------- ALL INSIDE ENCYPTION FOLDER ----------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########

#####  <<<------------------------- Caeser -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/encryption/caeser", methods=["GET", "POST"])
def ENC_Caeser():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_number = (request.form["Key_number"])
        if ((Key_number.isdigit()==False)or(int(Key_number)<0)or(int(Key_number)>26)or(len(Key_number)==0)):
            return render_template("encryption/caeser.html", show_error=1)
        else:
            return render_template(
                "encryption/caeser.html", Cipher_text=Caesar_Enc(plaintext, int(Key_number))
            )
    return render_template("encryption/caeser.html")


#####  <<<------------------------- ROT13 --------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/encryption/rot13", methods=["GET", "POST"])
def ENC_Rot13():
    if request.method == "POST":
        C_text = request.form["C_text"]
        return render_template("encryption/rot13.html", Cipher_text=dec_rot13(C_text))
    return render_template("encryption/rot13.html")


#####  <<<------------------------- ATBASH -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/encryption/atbash", methods=["GET", "POST"])
def ENC_Atbash():
    if request.method == "POST":
        C_text = request.form["C_text"]
        return render_template(
            "encryption/atbash.html", Cipher_text=ATBASH_Enc_Dec(C_text)
        )
    return render_template("encryption/atbash.html")


#####  <<<------------------------- Affine -------------------------------------------->>>  ###########
#####  <<<------------------------- need to implent odd fix on multiplier ------------->>>  ###########


@app.route("/encryption/affine", methods=["GET", "POST"])
def ENC_Affine():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        key1 = request.form["key1"]
        key2 = request.form["key2"]
        if ((key1.isdigit()==False)or(key2.isdigit()==False)or((int(key1))%2==0)or(len(key1)==0)):
            return render_template("encryption/affine.html", show_error=1)
        else:
            return render_template(
            "encryption/affine.html", Cipher_text=(Affine(int(key1),int(key2)).encipher(plaintext))
            )
    return render_template("encryption/affine.html")


#####  <<<------------------------- Vigenere -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished -------------------------------------------->>>  ###########


@app.route("/encryption/vigenere", methods=["GET", "POST"])
def ENC_Vigenere():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "encryption/vigenere.html", Cipher_text=VIGENERE_Enc(plaintext, Key_phrase3)
            )
    return render_template("encryption/vigenere.html")


#####  <<<------------------------- AutoKey -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished -------------------------------------------->>>  ###########


@app.route("/encryption/autokey", methods=["GET", "POST"])
def ENC_Autokey():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 =''.join([i for i in Key_phrase0 if not i.isdigit()])
        Key_phrase2 = scrub_string(Key_phrase1)
        if len(Key_phrase2)!=0:
            return render_template(
                "encryption/autokey.html", Cipher_text=AUTOKEY_Enc(plaintext, Key_phrase2)
            )
    return render_template("encryption/autokey.html")


#####  <<<------------------------- Beaufort -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished -------------------------------------------->>>  ###########


@app.route("/encryption/beaufort", methods=["GET", "POST"])
def ENC_Beaufort():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "encryption/beaufort.html", Cipher_text=BEAUFORT_Enc(plaintext, Key_phrase3)
            )
    return render_template("encryption/beaufort.html")


#####  <<<------------------------- COLTRANS -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished -------------------------------------------->>>  ###########


@app.route("/encryption/coltrans", methods=["GET", "POST"])
def ENC_Coltrans():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "encryption/coltrans.html", Cipher_text=COLTRANS_Enc(plaintext, Key_phrase3)
            )
    return render_template("encryption/coltrans.html")


#####  <<<------------------------- BIFID ----------------------------------------------->>>  ###########
#####  <<<------------------------- Finished -------------------------------------------->>>  ###########


@app.route("/encryption/bifid", methods=["GET", "POST"])
def ENC_Bifid():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        key_matrix = str(request.form["key_matrix"])
        key_integer = request.form["key_integer"]
        if ((len(key_matrix)!=25)or(key_matrix.isalpha()==False)or(str(key_integer).isdigit()==False)or(len(plaintext)%int(key_integer)!=0)):
            return render_template("encryption/bifid.html",show_error=1)
        else:
            return render_template(
                "encryption/bifid.html",
                Cipher_text=Bifid(str(key_matrix),int(key_integer)).encipher(plaintext),
            )
    return render_template("encryption/bifid.html")





#####  <<<------------------------- PORTA ----------------------------------------------->>>  ###########
#####  <<<------------------------- Finished -------------------------------------------->>>  ###########


@app.route("/encryption/porta", methods=["GET", "POST"])
def ENC_Porta():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "encryption/porta.html", Cipher_text=PORTA_Enc(plaintext, Key_phrase3)
            )
    return render_template("encryption/porta.html")


#####  <<<------------------------- ADGFX ----------------------------------------------->>>  ###########
#####  <<<------------------------- Needs building -------------------------------------->>>  ###########



@app.route("/encryption/ADFGX", methods=["GET", "POST"])
def ENC_ADFGX():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        key_matrix = str(request.form["key_matrix"])
        Key_phrase0 = request.form["key_integer"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if ((len(key_matrix)!=25)or(key_matrix.isalpha()==False)or(Key_phrase3.isalpha()==False)or(len(plaintext)%len(Key_phrase3)!=0)):
            return render_template("encryption/ADFGX.html",show_error=1)
        else:
            return render_template(
                "encryption/ADFGX.html",
                Cipher_text=ADFGX(str(key_matrix),str(Key_phrase3)).encipher(plaintext) ,
            )
    return render_template("encryption/ADFGX.html")

@app.route("/encryption/ADFGVX", methods=["GET", "POST"])
def ENC_ADFGVX():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        key_matrix = str(request.form["key_matrix"])
        Key_phrase0 = request.form["key_integer"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if ((len(key_matrix)!=36)or(Key_phrase3.isalpha()==False)or(len(plaintext)%len(Key_phrase3)!=0)):
            return render_template("encryption/ADFGVX.html",show_error=1)
        else:
            return render_template(
                "encryption/ADFGVX.html",
                Cipher_text=ADFGVX(str(key_matrix),str(Key_phrase3)).encipher(plaintext) ,
            )
    return render_template("encryption/ADFGVX.html")


#####  <<<------------------------- ENCYPTION ENDS HERE ------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########

#####  <<<------------------------- DENCYPTION ---------------------------------------->>>  ###########
#####  <<<------------------------- BEGINNING ----------------------------------------->>>  ###########
#####  <<<------------------------- HERE ---------------------------------------------->>>  ###########
#####  <<<------------------------- ALL INSIDE DECRYPTION FOLDER ---------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########

#####  <<<------------------------- Caeser -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/caeser", methods=["GET", "POST"])
def DEC_Caeser():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_number = (request.form["Key_number"])
        if ((Key_number.isdigit()==False)or(int(Key_number)<0)or(int(Key_number)>26)or(len(Key_number)==0)):
            return render_template("decryption/caeser.html", show_error=1)
        else:
            return render_template(
                "decryption/caeser.html", Cipher_text=Caesar_Dec(plaintext, int(Key_number))
            )
    return render_template("decryption/caeser.html")


#####  <<<------------------------- ROT13 --------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/rot13", methods=["GET", "POST"])
def DEC_Rot13():
    if request.method == "POST":
        C_text = request.form["C_text"]
        return render_template("decryption/rot13.html", Cipher_text=dec_rot13(C_text))
    return render_template("decryption/rot13.html")


#####  <<<------------------------- ATBASH -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/atbash", methods=["GET", "POST"])
def DEC_Atbash():
    if request.method == "POST":
        C_text = request.form["C_text"]
        return render_template(
            "decryption/atbash.html", Cipher_text=ATBASH_Enc_Dec(C_text)
        )
    return render_template("decryption/atbash.html")


#####  <<<------------------------- AFFINE -------------------------------------------->>>  ###########
#####  <<<------------------------- needs odd lock for multiplier --------------------->>>  ###########


@app.route("/decryption/affine", methods=["GET", "POST"])
def DEC_Affine():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        key1 = request.form["key1"]
        key2 = request.form["key2"]
        if ((key1.isdigit()==False)or(key2.isdigit()==False)or((int(key1))%2==0)or(len(key1)==0)):
            return render_template("decryption/affine.html", show_error=1)
        else:
            return render_template(
            "decryption/affine.html", Cipher_text=(Affine(int(key1),int(key2)).decipher(plaintext))
            )
    return render_template("decryption/affine.html")


#####  <<<------------------------- Vigenere -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/vigenere", methods=["GET", "POST"])
def DEC_Vigenere():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "decryption/vigenere.html", Cipher_text=VIGENERE_Dec(plaintext, Key_phrase3)
            )
    return render_template("decryption/vigenere.html")


#####  <<<------------------------- Autokey ------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/autokey", methods=["GET", "POST"])
def DEC_Autokey():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "decryption/autokey.html", Cipher_text=AUTOKEY_Dec(plaintext, Key_phrase3)
            )
    return render_template("decryption/autokey.html")


#####  <<<------------------------- Beaufort ------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/beaufort", methods=["GET", "POST"])
def DEC_Beaufort():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "decryption/beaufort.html", Cipher_text=BEAUFORT_Dec(plaintext, Key_phrase3)
            )
    return render_template("decryption/beaufort.html")


#####  <<<------------------------- Coltrans ------------------------------------------>>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/coltrans", methods=["GET", "POST"])
def DEC_Coltrans():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "decryption/coltrans.html", Cipher_text=COLTRANS_Dec(plaintext, Key_phrase3)
            )
    return render_template("decryption/coltrans.html")


#####  <<<------------------------- Bifid --------------------------------------------->>>  ###########
#####  <<<------------------------- add rules to every page of valid keys ------------->>>  ###########


@app.route("/decryption/bifid", methods=["GET", "POST"])
def DEC_Bifid():
    if request.method == "POST":
        plaintext = scrub_string(request.form["C_text"])
        key_matrix = str(request.form["key_matrix"])
        key_integer = request.form["key_integer"]
        if ((len(key_matrix)!=25)or(key_matrix.isalpha()==False)or(str(key_integer).isdigit()==False)or(len(plaintext)%int(key_integer)!=0)):
            return render_template("decryption/bifid.html",show_error=1)
        else:
            return render_template(
                "decryption/bifid.html",
                Cipher_text=Bifid(str(key_matrix),int(key_integer)).decipher(plaintext),
            )
    return render_template("decryption/bifid.html")


#####  <<<------------------------- Porta -------------------------------------------->>>  ###########
#####  <<<------------------------- Finished ------------------------------------------>>>  ###########


@app.route("/decryption/porta", methods=["GET", "POST"])
def DEC_Porta():
    if request.method == "POST":
        plaintext = request.form["C_text"]
        Key_phrase0 = request.form["Key_phrase"]
        Key_phrase1 = Key_phrase0.replace(" ", "")
        Key_phrase2 =''.join([i for i in Key_phrase1 if not i.isdigit()])
        Key_phrase3 = scrub_string(Key_phrase2)
        if len(Key_phrase3)!=0:
            return render_template(
                "decryption/porta.html", Cipher_text=PORTA_Dec(plaintext, Key_phrase3)
            )
    return render_template("decryption/porta.html")


#####  <<<------------------------- DECRYPTION ENDS HERE ------------------------------>>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########

#####  <<<------------------------- KEYLESS ------------------------------------------->>>  ###########
#####  <<<------------------------- BEGINNING ----------------------------------------->>>  ###########
#####  <<<------------------------- HERE ---------------------------------------------->>>  ###########
#####  <<<------------------------- ALL INSIDE KEYLESS FOLDER ------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########

#####  <<<------------------------- Ceaser ----------------------------------------------->>>  ###########
#####  <<<------------------------- Needs to be made a keyless version ------------------->>>  ###########


@app.route("/keyless/caeser", methods=["GET", "POST"])
def KEY_Ceaser():
    if request.method == "POST":
        method = request.form["format"]
        C_text = request.form["C_text"]
        prob_key = key_ceaser(C_text)
        if method == "LowerCase":
            return render_template(
                "keyless/caeser.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key0":
            Key_number = int(prob_key[0])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key1":
            Key_number = int(prob_key[1])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key2":
            Key_number = int(prob_key[2])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key3":
            Key_number = int(prob_key[3])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key4":
            Key_number = int(prob_key[4])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key5":
            Key_number = int(prob_key[5])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key6":
            Key_number = int(prob_key[6])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key7":
            Key_number = int(prob_key[7])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )
        if method == "key8":
            Key_number = int(prob_key[8])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            return render_template(
                "keyless/caeser.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=1,
                prob_key=prob_key,
            )

        return render_template("keyless/caeser.html", Cipher_text=dec_rot13(C_text))
    return render_template("keyless/caeser.html")


@app.context_processor
def context_processor():
    return dict(count_number=0)


#####  <<<------------------------- Vignere ---------------------------------------------->>>  ###########
#####  <<<------------------------- Needs to be made a keyless version ------------------->>>  ###########


@app.route("/keyless/vigenere", methods=["GET", "POST"])
def KEY_Vigenere():
    if request.method == "POST":
        method = request.form["format"]
        C_text = request.form["C_text"]
        prob_key_len = probable_key_length(C_text)
        prob_key_word = 0
        if method == "LowerCase":
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=1,
                prob_key_len=prob_key_len,
            )
        if method == "key0":
            Key_number = int(prob_key_len[0])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[0])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key1":
            Key_number = int(prob_key_len[1])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[1])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key2":
            Key_number = int(prob_key_len[2])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[2])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key3":
            Key_number = int(prob_key_len[3])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[3])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key4":
            Key_number = int(prob_key_len[4])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[4])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key5":
            Key_number = int(prob_key_len[5])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[5])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key6":
            Key_number = int(prob_key_len[6])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[6])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key7":
            Key_number = int(prob_key_len[7])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[7])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key8":
            Key_number = int(prob_key_len[8])
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[8])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=C_text.lower(),
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
                previous=8
            )

        if method == "key00":
            plaintext = C_text
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[0])
            Output = VIGENERE_Dec(plaintext,prob_key_word[0])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key10":
            Key_number = int(prob_key_len[1])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[1])
            Output = VIGENERE_Dec(plaintext,prob_key_word[1])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key20":
            Key_number = int(prob_key_len[2])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[2])
            Output = VIGENERE_Dec(plaintext,prob_key_word[2])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key30":
            Key_number = int(prob_key_len[3])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[3])
            Output = VIGENERE_Dec(plaintext,prob_key_word[3])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key40":
            Key_number = int(prob_key_len[4])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[4])
            Output = VIGENERE_Dec(plaintext,prob_key_word[4])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key50":
            Key_number = int(prob_key_len[5])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[5])
            Output = VIGENERE_Dec(plaintext,prob_key_word[5])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key60":
            Key_number = int(prob_key_len[6])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[6])
            Output = VIGENERE_Dec(plaintext,prob_key_word[6])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key70":
            Key_number = int(prob_key_len[7])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[7])
            Output = VIGENERE_Dec(plaintext,prob_key_word[7])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )
        if method == "key80":
            Key_number = int(prob_key_len[8])
            plaintext = C_text
            Output = Caesar_Dec(plaintext, Key_number)
            prob_key_word = get_vigenere_keys(C_text,prob_key_len[8])
            Output = VIGENERE_Dec(plaintext,prob_key_word[8])
            return render_template(
                "keyless/vigenere.html",
                Cipher_text=Output,
                C_text=C_text,
                show_results=2,
                prob_key_len=prob_key_len,
                prob_key_word=prob_key_word,
            )


        return render_template("keyless/vigenere.html", Cipher_text=dec_rot13(C_text))
    return render_template("keyless/vigenere.html")


#####  <<<------------------------- KEYLESS ENDS HERE --------------------------------->>>  ###########
#####  <<<----------------------------------------------------------------------------->>>  ###########
