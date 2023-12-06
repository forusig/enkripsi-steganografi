from flask import Flask, render_template, request
from stegano import lsb
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def konversiascii(text):
    ascii_values = []
    for char in text:
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values

def konversibiner(text):
    binary_values = []
    for char in text:
        binary_value = bin(char)[2:]
        binary_values.append(binary_value)
    return binary_values

def xor_biner(textb, keyb):
    xor_values = []
    for t, k in zip(textb, keyb):
        result = int(t, 2) ^ int(k, 2)
        result_biner = bin(result)[2:].zfill(7)  
        xor_values.append(result_biner)
    return xor_values

def biner_ke_desimal(biner):
    return int(biner, 2)

def kodeascii(ascii_code):
    return chr(ascii_code)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enkripsi', methods=['POST'])
def enkripsi():
    plaintext = request.form['plaintext']
    key = request.form['key']

    # Handle file upload
    uploaded_file = request.files['image']
    if uploaded_file.filename != '':
        import datetime
        unique_filename = f"image_secret_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

        uploaded_file.save(file_path)

        # Enkripsi menggunakan XOR
        asci = konversiascii(plaintext)
        key_A = konversiascii(key)
        textb = konversibiner(asci)
        keyb = konversibiner(key_A)
        result = xor_biner(textb, keyb)

        # Konversi hasil XOR ke string ASCII
        decimal_results = [biner_ke_desimal(b) for b in result]
        ascii_results = [kodeascii(d) for d in decimal_results]
        encrypted_text = ''.join(ascii_results)

        # Simpan hasil enkripsi dalam gambar menggunakan steganografi LSB
        lsb.hide(file_path, encrypted_text).save(file_path)

        # Reveal message from image
        clear_message = lsb.reveal(file_path)

        # Dekripsi hasil steganografi menggunakan XOR
        clear_text_biner = konversibiner(konversiascii(clear_message))
        decrypted_result = xor_biner(clear_text_biner, keyb)
        hasil_deskripsi_karakter = [kodeascii(biner_ke_desimal(biner)) for biner in decrypted_result]

        # Gabungkan karakter hasil dekripsi menjadi teks
        hasil_deskripsi = ''.join(hasil_deskripsi_karakter)

        print("Hasil Dekripsi:", hasil_deskripsi)


        return render_template('result.html', encrypted_text=encrypted_text, image_path=file_path)
    else:
        return render_template('result.html', error='No file uploaded')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
