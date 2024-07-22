# Pegasus-judi-online

Pegasus-judi-online adalah alat pemantauan jaringan yang dirancang untuk mendeteksi akses ke situs judi online yang dikenal. Alat ini menggunakan `scapy` untuk menangkap lalu lintas DNS dan memeriksa apakah domain yang diminta termasuk dalam daftar situs judi online yang telah ditentukan.

## Fitur

- Menangkap paket DNS di jaringan lokal.
- Memeriksa domain yang diminta terhadap daftar situs judi online yang dikenal.
- Mencetak peringatan setiap kali akses ke situs judi online terdeteksi.

## Persyaratan

- Python 3.x
- scapy

## Instalasi

1. Clone repositori ini:
    ```bash
    git clone https://github.com/username/Pegasus-judi-online.git
    cd Pegasus-judi-online
    ```

2. Install `scapy`:
    ```bash
    pip install scapy
    ```

## Penggunaan

1. Edit daftar situs judi online yang dikenal di dalam file `Pegasus-judi-online.py`:
    ```python
    known_gambling_sites = [
        "examplecasino.com",
        "onlineslots.net",
        "pokerworld.com"
    ]
    ```

2. Jalankan skrip:
    ```bash
    sudo python Pegasus-judi-online.py
    ```

   **Catatan**: Menjalankan `scapy` untuk menangkap paket jaringan mungkin memerlukan hak akses superuser.

3. Monitor output di terminal. Setiap kali domain yang diminta termasuk dalam daftar situs judi online, Anda akan melihat pesan peringatan:
    ```
    [!] Detected gambling site access: examplecasino.com
    ```

## Catatan Penting

- **Legalitas**: Pastikan bahwa tindakan Anda sesuai dengan hukum yang berlaku di negara Anda. Memantau aktivitas online seseorang tanpa izin adalah ilegal di banyak negara.
- **Etika**: Pertimbangkan etika dalam memantau aktivitas online orang lain.
- **Keamanan Data**: Pastikan data yang Anda kumpulkan diamankan dengan baik untuk menghindari penyalahgunaan.
- **Privasi Pengguna**: Hormati privasi pengguna jaringan Anda dan pastikan mereka mengetahui bahwa aktivitas mereka dipantau jika ini adalah jaringan publik.

## Kontribusi

Kontribusi sangat diterima! Silakan buat issue atau pull request jika Anda memiliki saran perbaikan atau fitur tambahan.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT.

## Author
dr. Muhammad Sobri Maulana
