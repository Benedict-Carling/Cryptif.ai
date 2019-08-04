from flask import Flask, session, redirect, url_for, escape, request, render_template
import string
from DecryptionFunctions import *
from ALL_ENCRYPTION import *

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#############################   ALL DECRYPTION VARIABLES #################################


#############################   ALL DECRYPTION VARIABLE END ##############################

#############################   Routing   ################################################

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/ceaser', methods=['GET', 'POST'])
def ceaser():
    if request.method == 'POST':
        C_text = request.form['C_text']
        return render_template('ceaser.html', Cipher_text = dec_ceaser(C_text))
    return render_template('ceaser.html')

@app.route('/vignere', methods=['GET', 'POST'])
def vignere():
    if request.method == 'POST':
        C_text = request.form['C_text']
        kw_len = keyword_length(C_text)
        kw = find_keyword(C_text, kw_len)
        Output = crypt(C_text, kw, -1)
        return render_template('vignere.html', Cipher_text = Output, Key_length = str(kw_len), Key_text = correct_keyword(kw) )
    return render_template('vignere.html')

@app.route('/rot13', methods=['GET', 'POST'])
def rot13():
    if request.method == 'POST':
        C_text = request.form['C_text']
        return render_template('rot13.html', Cipher_text = dec_rot13(C_text))
    return render_template('rot13.html')

@app.route('/format', methods=['GET', 'POST'])
def format():
    if request.method == 'POST':
        method = request.form['format']
        C_text = request.form['C_text']
        if method == 'LowerCase':
            return render_template('format.html', Cipher_text = C_text.lower())
        if method == 'RemoveSpaces':
            return render_template('format.html', Cipher_text = C_text.replace(" ", ""))
        if method == 'RemovePunctuation':
            return render_template('format.html', Cipher_text = C_text.translate(str.maketrans('', '', string.punctuation)))
        if method == 'CompleteFormat':
            return render_template('format.html', Cipher_text = scrub_string(C_text))
        
        return render_template('format.html', Cipher_text = dec_rot13(C_text))
    return render_template('format.html')

@app.route('/cryptanalysis', methods=['GET', 'POST'])
def cryptanalysis():
    if request.method == 'POST':
        C_text = scrub_string(request.form['C_text'])
        return render_template('cryptanalysis.html', Frequency = frequency_list_generate(C_text), IOC = str(IC(C_text,1)))
    return render_template('cryptanalysis.html', Frequency = frequency_list_generate(''))

@app.route('/deepLearning', methods=['GET', 'POST'])
def deepLearning():
    return render_template('deepLearning.html')

@app.route('/encryption', methods=['GET', 'POST'])
def encryption():
    return render_template('encryption.html', )

@app.route('/decryption', methods=['GET', 'POST'])
def decryption():
    return render_template('decryption.html')

@app.route('/keylessdecryption', methods=['GET', 'POST'])
def keylessdecryption():
    return render_template('keylessdecryption.html')

#############################   Encryption       ########################################

@app.route('/ENC_Caeser', methods=['GET', 'POST'])
def ENC_Caeser():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_number = int(request.form['Key_number'])
        return render_template('ENC_Caeser.html', Cipher_text = Caesar_Enc(plaintext,Key_number))
    return render_template('ENC_Caeser.html')

@app.route('/ENC_Rot13', methods=['GET', 'POST'])
def ENC_Rot13():
    if request.method == 'POST':
        C_text = request.form['C_text']
        return render_template('ENC_Rot13.html', Cipher_text = dec_rot13(C_text))
    return render_template('ENC_Rot13.html')

@app.route('/ENC_Atbash', methods=['GET', 'POST'])
def ENC_Atbash():
    if request.method == 'POST':
        C_text = request.form['C_text']
        return render_template('ENC_Atbash.html', Cipher_text = ATBASH_Enc_Dec(C_text))
    return render_template('ENC_Atbash.html')

@app.route('/ENC_Affine', methods=['GET', 'POST'])
def ENC_Affine():
    if request.method == 'POST':
        C_text = request.form['C_text']
        key1 =  int(request.form['key1'])
        key2 =  int(request.form['key2'])
        return render_template('ENC_Affine.html', Cipher_text = AFFINE_Enc(C_text,key1,key2))
    return render_template('ENC_Affine.html')

@app.route('/ENC_Vigenere', methods=['GET', 'POST'])
def ENC_Vigenere():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('ENC_Vigenere.html', Cipher_text = VIGENERE_Enc(plaintext,Key_phrase))
    return render_template('ENC_Vigenere.html')

@app.route('/ENC_Autokey', methods=['GET', 'POST'])
def ENC_Autokey():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('ENC_Autokey.html', Cipher_text = AUTOKEY_Enc(plaintext,Key_phrase))
    return render_template('ENC_Autokey.html')

@app.route('/ENC_Beaufort', methods=['GET', 'POST'])
def ENC_Beaufort():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('ENC_Beaufort.html', Cipher_text = BEAUFORT_Enc(plaintext,Key_phrase))
    return render_template('ENC_Beaufort.html')

@app.route('/ENC_Coltrans', methods=['GET', 'POST'])
def ENC_Coltrans():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('ENC_Coltrans.html', Cipher_text = COLTRANS_Enc(plaintext,Key_phrase))
    return render_template('ENC_Coltrans.html')

@app.route('/ENC_Bifid', methods=['GET', 'POST'])
def ENC_Bifid():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        key_matrix = str(request.form['key_matrix'])
        key_integer = int(request.form['key_integer'])
        return render_template('ENC_Bifid.html', Cipher_text = BIFID_Enc(plaintext,key_matrix,key_integer))
    return render_template('ENC_Bifid.html')

@app.route('/ENC_Porta', methods=['GET', 'POST'])
def ENC_Porta():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('ENC_Porta.html', Cipher_text = PORTA_Enc(plaintext,Key_phrase))
    return render_template('ENC_Porta.html')

@app.route('/ENC_ADFGX', methods=['GET', 'POST'])
def ENC_ADFGX():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        key_matrix = str(request.form['key_matrix'])
        key_word = str(request.form['key_word'])
        return render_template('ENC_ADFGX.html', Cipher_text = BIFID_Enc(plaintext,key_matrix,key_word))
    return render_template('ENC_ADFGX.html')

#############################  END OF ENCRYPTION ########################################

#############################  START OF DECRYPTION  #####################################

@app.route('/DEC_Caeser', methods=['GET', 'POST'])
def DEC_Caeser():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_number = int(request.form['Key_number'])
        return render_template('DEC_Caeser.html', Cipher_text = Caesar_Dec(plaintext,Key_number))
    return render_template('DEC_Caeser.html')

@app.route('/DEC_Rot13', methods=['GET', 'POST'])
def DEC_Rot13():
    if request.method == 'POST':
        C_text = request.form['C_text']
        return render_template('DEC_Rot13.html', Cipher_text = dec_rot13(C_text))
    return render_template('DEC_Rot13.html')

@app.route('/DEC_Atbash', methods=['GET', 'POST'])
def DEC_Atbash():
    if request.method == 'POST':
        C_text = request.form['C_text']
        return render_template('DEC_Atbash.html', Cipher_text = ATBASH_Enc_Dec(C_text))
    return render_template('DEC_Atbash.html')

@app.route('/DEC_Affine', methods=['GET', 'POST'])
def DEC_Affine():
    if request.method == 'POST':
        C_text = request.form['C_text']
        key1 =  int(request.form['key1'])
        key2 =  int(request.form['key2'])
        return render_template('DEC_Affine.html', Cipher_text = AFFINE_Dec(C_text,key1,key2))
    return render_template('DEC_Affine.html')

@app.route('/DEC_Vigenere', methods=['GET', 'POST'])
def DEC_Vigenere():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('DEC_Vigenere.html', Cipher_text = VIGENERE_Dec(plaintext,Key_phrase))
    return render_template('DEC_Vigenere.html')

@app.route('/DEC_Autokey', methods=['GET', 'POST'])
def DEC_Autokey():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('DEC_Autokey.html', Cipher_text = AUTOKEY_Dec(plaintext,Key_phrase))
    return render_template('DEC_Autokey.html')

@app.route('/DEC_Beaufort', methods=['GET', 'POST'])
def DEC_Beaufort():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('DEC_Beaufort.html', Cipher_text = BEAUFORT_Dec(plaintext,Key_phrase))
    return render_template('DEC_Beaufort.html')

@app.route('/DEC_Coltrans', methods=['GET', 'POST'])
def DEC_Coltrans():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('ENC_Coltrans.html', Cipher_text = COLTRANS_Dec(plaintext,Key_phrase))
    return render_template('DEC_Coltrans.html')

@app.route('/DEC_Bifid', methods=['GET', 'POST'])
def DEC_Bifid():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        key_matrix = str(request.form['key_matrix'])
        key_integer = int(request.form['key_integer'])
        return render_template('DEC_Bifid.html', Cipher_text = BIFID_Dec(plaintext,key_matrix,key_integer))
    return render_template('DEC_Bifid.html')

@app.route('/DEC_Porta', methods=['GET', 'POST'])
def DEC_Porta():
    if request.method == 'POST':
        plaintext = request.form['C_text']
        Key_phrase = request.form['Key_phrase']
        return render_template('DEC_Porta.html', Cipher_text = PORTA_Dec(plaintext,Key_phrase))
    return render_template('DEC_Porta.html')

############################ END OF DECRYPTION  ########################################




#############################   End of Routing   ########################################