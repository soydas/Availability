Mevcudiyet Kontrolü (Availability Check)
Bu basit Python betiği, bir dosyadaki URL'leri kontrol ederek mevcudiyet durumlarını belirler. Belirtilen URL'lere HTTP istekleri gönderir ve yanıtları kontrol eder. Ayrıca, mevcudiyet kontrolünü gerçekleştirilen URL'lerin durumlarını tablo halinde ekrana basar ve aynı zamanda bir log dosyasına hatalı durumları kaydeder.
Kullanım
1.	list.txt adlı bir dosya oluşturun ve kontrol etmek istediğiniz URL'leri bu dosyaya ekleyin. Dosya, her satırda bir URL içermelidir.
2.	Python betiğini çalıştırın: python Availability.py
3.	Kontrol sonuçlarını ekranda ve log dosyasında gözlemleyin.
Gereksinimler
•	Python 3
•	colorama
•	tabulate
Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:
pip install colorama tabulate 
________________________________________________________________________________
Availability Check
This simple Python script checks the availability status of URLs listed in a file. It sends HTTP requests to the specified URLs and checks their responses. It also prints the statuses of the URLs in a tabular format and logs any errors to a log file.
Usage
1.	Create a file named list.txt and add the URLs you want to check into this file. The file should contain one URL per line.
2.	Run the Python script: python Availability.py
3.	Observe the check results on the screen and in the log file.
Requirements
•	Python 3
•	colorama
•	tabulate
You can install the required libraries using the following commands:
pip install colorama tabulate 

