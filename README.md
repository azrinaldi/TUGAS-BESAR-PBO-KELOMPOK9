# TUGAS BESAR PBO KELOMPOK 9 & HANDS ON DOCKER 2 SISTEM OPERASI

Anggota: <br />
120140127   Dicko Azrinaldi <br />
120140236   Bagasyah Kusetyoutomo Dhonanur Hakim <br />
120140045   Christopher Gilbert Bontor Rumapea <br />
120140232   Aaron Noah Kalalo <br />
120140061   Maura Diviarani <br />
120140165   Dini Safitri <br />

"Snake Game (python) di-wrap dengan Docker" <br />

Snake Game adalah sebuah permainan dimana pemain mengendalikan sebuah garis yang tumbuh memanjang, dengan garis itu sendiri menjadi rintangan utama. Dalam game ini pemain akan mengendalikan sebuah mahluk yang menyerupai ular yang akan bergerak mengitari sebuah bidang berbentuk kotak, dengan tujuan mengambil makanan yang aslinya berbentuk dot atau titik. Selama bermain, si pemain harus berusaha untuk tidak menabrak dinding atau ekornya sendiri dan itu akan semakin susah, karena setiap kali si pemain memakan makanan, ekornya akan bertambah panjang. Kontrol-pun sangat mudah, yakni hanya atas, bawah, kiri dan kanan, ular akan berjalan secara otomatis dan tidak dapat dihentikan.

Snake game dibuat dengan menerapkan prinsip-prinsip dari mata kuliah Pemrograman Berorientasi Objek (PBO) yaitu, enkapkulasi, abstraksi dan inheritance.
Dengan menggunakan docker, kami akan membuat kontainer yang digunakan sebagai wrapper untuk "membungkus" program game Snake.

Build Docker Image<br />

`docker build -t (nama image)`

Run Docker Image <br />

`docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/snd (nama image)`
