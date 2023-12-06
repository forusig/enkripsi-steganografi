from stegano import lsb

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

plaintext = input("Plaintext: ")
key = input("Kunci: ")

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
lsb.hide("./bird.jpg", encrypted_text).save("./new_bird.png")

# Reveal message from image
clear_message = lsb.reveal("./new_bird.png")

# Dekripsi hasil steganografi menggunakan XOR
clear_text_biner = konversibiner(konversiascii(clear_message))
decrypted_result = xor_biner(clear_text_biner, keyb)
hasil_deskripsi_karakter = [kodeascii(biner_ke_desimal(biner)) for biner in decrypted_result]

print("Hasil enkripsi:", encrypted_text)
print("Hasil Dekripsi:", "".join(hasil_deskripsi_karakter))
