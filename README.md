# enkripsi-steganografi
menyisipkan enkripsi one time pad ke dalam image 

<table>
<th>nama</th>
<th>prodi</th>
<th>kelas</th>
<tr>
<th>Ade Maulani Bilgis</th>
<th>Teknik Informatika</th>
<th>TI.21.A1</th>
</tr>
</table>

## steganografi
- Steganografi adalah seni dan ilmu menulis pesan tersembunyi atau menyembunyikan pesan dengan cara tertentu sehingga selain si pengirim dan si penerima, tidak ada seorang pun yang mengetahui atau menyadari bahwa ada suatu pesan rahasia.
- LSB adalah singkatan dari "Least Significant Bit". LSB adalah teknik yang umum digunakan dalam enkripsi dan dekripsi informasi rahasia. Cara kerja metode LSB yaitu mengubah bit redundan cover image yang tidak berpengaruh signifikan dengan bit dari pesan rahasia.

## Daftar Isi

1. [Implementasi Steganografi Metode LSB](#implementasi-steganografi-metode-lsb)
   - [Contoh Implementasi](#contoh-implementasi)
   - [Hasil](#hasil)
2.  [menggabungkan enkripsi one time pad dengan steganografi metode lsb](#menggabungkan-enkripsi-one-time-pad-dengan-steganografi-metode-lsb)
    - [hasil penggabungan](#hasil-penggabungan)


# implementasi steganografi metode lsb
- pastikan anda sudah menginstall library stegano terlebih dahulu :
``` pip install stegano ```
- lalu buatlah file untuk menyimpan foto dan program
- Mulailah dengan mengimpor library ke dalam program python
  ``` from stegano import lsb ```
- lalu tambahkan fungsi ``` secret = lsb.hide("./masukan gambar.png", "tulis text disini") ``` untuk menyembunyikan pesan ke dalam gambar ``` ("./masukan gambar.png") ``` menggunakan metode lsb, dan hasilnya akan disimpan ke dalam ``` secret ```
- lalu tambahkan fungsi ``` secret.save("./image_secret.png") ``` agar objek ``` secret ``` yang berisi gambar dengan pesan tersembunyi disimpan dalam file baru bernama ```apapun.png```
Jika ingin melakukan deskripsi pesan pada gambar yang sudah terenkripsi anda bisa menuliskan kode berikut:
- lsb.reveal``("./apapun.png")``: Fungsi ini digunakan untuk mengungkap enkripsi dalam gambar yang telah disimpan ```(apapun.png)```. Hasilnya adalah pesan yang tersembunyi.
- gambar yang sudah ter encrypt kemudian di tampilkan menggunakan ``print(clear_message)``
  
  ### contoh implementasi
  gambar awal
  
  ![wonu](https://github.com/forusig/enkripsi-steganografi/assets/92717505/79ae890c-1d3b-44af-9ff6-c16e58440956)
   
   ```
   from stegano import lsb

   secret = lsb.hide("./wonu.png", "Hello Wonwoo")
  secret.save("./new_wonu.png")

  clear_message = lsb.reveal("./new_wonu.png")
  print(clear_message)
  ```
### hasil
![new_wonu](https://github.com/forusig/enkripsi-steganografi/assets/92717505/6dc10845-9fca-4b5b-914e-29fc9123ad0e)

![Screenshot 2023-12-06 103538](https://github.com/forusig/enkripsi-steganografi/assets/92717505/ab53766b-cd25-47fe-a70c-b81636196374)


# menggabungkan enkripsi one time pad dengan steganografi metode lsb
siapkan program one time pad nya terlebih dahulu, yang menggunakan alur algoritma seperti 
1.	Tentukan plainteks
2.	Tentukan kunci
   ```
plaintext = input("Plaintext: ")
key = input("kunci: ")
```
3.	Ubahk plainteks ke ascii
4.	Ubah kunci ke ascii
```
asci = konversiascii(text)
key_A = konversiascii(key)
```  
5.	Ubah planinteks ascii (Desimal) ke biner
6.	Ubah Kunci ascii (Desimal) ke biner
```
textb = konversibiner(asci)
keyb = konversibiner(key_A)
```
7.	Lakukan Xor hasil biner Plainteks dan Kunci
    ```
    result = xor_biner(textb, keyb)
    ```
12.	Hasil XOR kembalikan ke decimal
13.	Desimal hasil Xor ambil kode asciinya jadilah Eckeripsi OTP

```
decrypted_result = xor_biner(result, keyb)
hasil_deskripsi_karakter = [kodeascii(biner_ke_desimal(biner)) for biner in decrypted_result]
decimal_results = [biner_ke_desimal(b) for b in result]
ascii_results = [kodeascii(d) for d in decimal_results]
```
- lalu gabungkan program one time pad dengan stegano yang sudah di buat
gambar awal

 ![bird](https://github.com/forusig/enkripsi-steganografi/assets/92717505/4b39ab57-0f19-4d47-9e28-d3deb1fcd0c3)
 
### hasil penggabungan
![new_bird](https://github.com/forusig/enkripsi-steganografi/assets/92717505/fedd158d-c89a-4e38-863f-fc56fd2f1d6e)
![Screenshot 2023-12-06 110257](https://github.com/forusig/enkripsi-steganografi/assets/92717505/7bdd8feb-b2f8-4d99-a69a-af68019c1cfc)

# mengimplementasikannya ke dalam web 
![Screenshot 2023-12-06 112158](https://github.com/forusig/enkripsi-steganografi/assets/92717505/d2d385f1-807d-436a-aeaa-4b9076b3297f)

gambar awal

![wonu](https://github.com/forusig/enkripsi-steganografi/assets/92717505/dfc69d30-4847-4c74-bdae-3d816e11809f)

### hasil dalam web
hasil dalam web akan di simpan dengan format date 
```
uploaded_file = request.files['image']
    if uploaded_file.filename != '':
        import datetime
        unique_filename = f"image_secret_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

        uploaded_file.save(file_path)
```
![Screenshot 2023-12-06 112406](https://github.com/forusig/enkripsi-steganografi/assets/92717505/e57e0a57-a891-4658-8b7d-07783a2a1fd3)

jika membukanya dengan terminal 

![Screenshot 2023-12-06 113053](https://github.com/forusig/enkripsi-steganografi/assets/92717505/e847fc08-99c3-4c05-9b6c-843913548af3)

hasil foto nya

![image_secret_20231206112357](https://github.com/forusig/enkripsi-steganografi/assets/92717505/b35fc55d-b197-41a5-9a20-c99c5f6d8f92)

