# Submission Akhir: Proyek Analisis Data

## Kelas Dicoding: **Belajar Analisis Data dengan Python**
by:
- Muhammad Arfani Asra
- arfani152@gmail.com

## Petunjuk Menggunakan Proyek
- Clone repository ini: ```git clone ```
- Untuk menjalankan file `.ipynb` maupun file `.py`, pastikan dependensi yang dibutuhkan sudah tersedia (lihat `requirements.txt` untuk mengetahui depensensi yang dibutuhkan).

## Petunjuk Melihat Hasil Analisis Data
- Buka file `Submission_analisis_data_dengan_python.ipynb` menggunakan Google Colab/Jupyter Notebook. Output dari masing-masing cell seharusnya sudah terlihat karena file sudah dijalankan sebelumnya.

## Petunjuk Menjalankan Dashboard Streamlit

### Menjalankan Streamlit Dashboard secara Local
- Buka file `dashboard.py` menggunakan code editor atau IDE (seperti Visual Studio Code)
- Buka shell/terminal
- Install Library yang dibutuhkan dengan perintah:
  ```sh
  pip install streamlit pandas matplotlib seaborn babel
  ```
- Jalankan perintah berikut di shell/termial:
  ```sh
  streamlit run dashboard.py
  ```
- Dashboard dapat diakses melalui browser di alamat: ```http://localhost:8501```

### Menjalankan Streamlit Dashboard menggunakan ngrok
- Pastikan Anda mempunyai akun ngrok ([daftar disini](https://dashboard.ngrok.com/signup)) dan dapatkan **Authtoken** ngrok Anda.
- Buka file `Submission_analisis_data_dengan_python.ipynb`
- Jalankan seluruh kode dari awal hingga selesai. Pastikan dependensi dan library untuk menggunakan ngrok sudah dijalankan. Contoh: pastikan `pip install pyngrok` sudah dijalankan.
- Tambahkan Authtoken Anda sendiri pada konfigurasi bagian ini:
  ```py
  ngrok config add-authtoken YOUR_AUTHTOKEN
  ```
- Jalankan Streamlit dan ngrok dengan running kode bagian berikut:
  ```py
  from ngrok import ngrok
  !streamlit run dashboard.py &> /dev/null &
  public_url = ngrok.connect(port=8501)
  print(f"Streamlit dashboard is available at: {public_url}")
  ```
- Akses Dashboard menggunakan URL yang diberikan oleh ngrok (contoh: `https://xxxx-xxxx.ngrok.io`)
