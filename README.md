# TUGAS BESAR PBO KELOMPOK 9 & HANDS ON DOCKER 2 SISTEM OPERASI

Anggota: <br />
120140127   Dicko Azrinaldi <br />
120140236   Bagasyah Kusetyoutomo Dhonanurhakiim <br />
120140045   Christopher Gilbert Bontor Rumapea <br />
120140232   Aaron Noah Kalalo <br />
120140061   Maura Diviarani <br />
120140165   Dini Safitri <br />

"Snake Game (python) di-wrap dengan Docker" <br />

Snake Game adalah sebuah permainan dimana pemain mengendalikan sebuah garis yang tumbuh memanjang, dengan garis itu sendiri menjadi rintangan utama. Dalam game ini pemain akan mengendalikan sebuah mahluk yang menyerupai ular yang akan bergerak mengitari sebuah bidang berbentuk kotak, dengan tujuan mengambil makanan yang aslinya berbentuk dot atau titik. Selama bermain, si pemain harus berusaha untuk tidak menabrak dinding atau ekornya sendiri dan itu akan semakin susah, karena setiap kali si pemain memakan makanan, ekornya akan bertambah panjang. Kontrol-pun sangat mudah, yakni hanya atas, bawah, kiri dan kanan, ular akan berjalan secara otomatis dan tidak dapat dihentikan.

Snake game dibuat dengan menerapkan prinsip-prinsip dari mata kuliah Pemrograman Berorientasi Objek (PBO) yaitu, enkapkulasi, abstraksi dan inheritance.
Dengan menggunakan docker, kami akan membuat kontainer yang digunakan sebagai wrapper untuk "membungkus" program game Snake.

Identifikasi Kelas dan Objek :
1. CLASS SQUARE
       Class Square berfungsi sebagai pengaturan segala sesuatu yang berhubungan dengan semua elemen pada food  atau makanan untuk ular nanti, seperti pengaturan warna makanan, penempatan lokasi, hingga melakukan pengaturan rumus untuk lokasi makanan agar bisa berpindah pindah. Pada class ini akan menjadi tubuh untuk objek food dan snake.

2. CLASS SNAKE
    Class Snake berfungsi sebagai pengaturan segala sesuatu yang berhubungan dengan semua elemen pada ular, seperti penginput file berupa gambar yang berupa kepala serta badan ular, melakukan pengaturan jika ular tersebut makan maka panjangnya akan bertambah dan juga berfungsi untuk melakukan pengaturan rumus bagaimana ular bergerak di dalam game. Objek dari kelas ini adalah Snake.
    
3. CLASS GAME_PLAY
  Class GamePlay berfungsi sebagai pengaturan yang berhubungan dengan gameplaynya seperti untuk mengidentifikasian font yang digunakan, pengaturan peletakan elemen, pengaturan cara bermain pemain seperti fungsi ke bawah, atas, kanan dan kiri maupun level kesulitannya. Pada class menampilkan hasil point yang didapatkan.
  
4. CLASS POINT
Class Point berfungsi sebaga mengatur perhitungan skor yang didapatkan jika ular telah memakan makanannya. 

Penerapan pada PBO :

Pada game ini akan diterapkan 3 prinsip PBO yaitu:

a) Enkapsulasi adalah metode untuk mengatur struktur sebuah kelas   dengan melakukan penyembunyian atribut dan method. Enkapsulasi digunakan untuk menghindari terjadinya kesalahan manipulasi pada kode program game snake.

b) Abstraksi adalah metode untuk menyembunyikan detail fungsionalitas  dari sebuah fungsi.  Metode ini untuk menyembunyikan kelas maupun method yang tidak perlu ditampilkan kepada pemain.

c) Inheritance adalah metode untuk menurukan atribut dari parent ke child. Metode ini digunakan pada kelas Snake sebagai child dari kelas Square.

Build Docker Image<br />

`docker build -t (nama image)`

Run Docker Image <br />

`docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/snd (nama image)`

Video Demo Kontainer

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/r6xeJqtRL8Y/0.jpg)](https://www.youtube.com/watch?v=r6xeJqtRL8Y)




