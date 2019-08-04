from flask import Flask, session, redirect, url_for, escape, request, render_template
import string
from DecryptionFunctions import *

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

#############################   End of Routing   ########################################