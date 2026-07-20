# Extracted from: hengki26,+237-246+Tarigan.pdf
**Total Pages**: 10
**Extraction Date**: 2026-07-20

---

## Page 1

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
237 
 
Analysis of String Matching Application on Serial Number Using Boyer 
Moore Algorithm 
 
Dede A. Tarigan 1)*, Adiyanto O. Buaton 2), Briyandana 3), Erica R. Safitri 4), Rika Rosnelly 5) 
1,2,3,4,5) Potensi Utama University, Indonesia 
1)dedeardian2402@yahoo.com, 2) adiyantooktavianus7@gmail.com, 3) briyandana07@gmail.com, 4) 
ericariansafitri38@gmail.com, 5)rika@potensi-utama.ac.id 
 
 
ABSTRACT 
Nowadays, technology has become the most important pillar in business management. The rapid development of 
technology has a significant impact on various aspects of business, from operational efficiency to marketing 
strategies. Applications are very important in a company or agency. With an information system, companies and 
agencies can easily guarantee the quality of information that will be presented for decision-making. Now, much 
information can be easily obtained quickly, thanks to information technology. The speed and accuracy of 
information delivery is a challenge for all producers in running their business. Boyer-Moore algorithm is one of 
the algorithms that can be used in the Barcode Generator application to scan barcode product serial numbers. The 
Boyer-Moore algorithm method functions to find sequence numbers. The development process requires several 
stages of investigation in the form of data collection techniques, problem identification, application of the Boyer-
Moore algorithm, implementation, and system testing. This iterative process makes the application of string 
matching with the Boyer-Moore algorithm technique into a very accurate application suitable for text search. This 
process is done by giving a pattern to the text. Therefore, the final result of string matching text search using the 
Boyer-Moore algorithm technique requires nine iterations. In the 9th iteration, the text and pattern conditions are 
matched or sequential. From the results of the manual computational search analysis work of applying the Boyer 
Moore string matching algorithm, several stages of the process are made, namely iterations 1 to 9, as a search step 
to determine string matches. In addition, patterns can be used with the number of shifts of patterns or text up to 13 
times. 
Keywords: Boyer-Moore Algorithm; Barcode Generator; Serial Number; String Matching,; Coway 
International Indonesia; 
 
INTRODUCTION 
In this modern era, technology has become the main pillar in running a business. Rapid developments in 
technology have had a significant impact on various aspects of business life, from operational efficiency to marketing 
strategies. According to (Irawan & Pratama, 2020), speed and accuracy in transferring information is a challenge for 
every manufacturer in running their business. String matching is an algorithm used for matching a text against another 
text also referred to as text search. There are several algorithms that can be used for string matching, including the 
Boyer-Moore algorithm. Boyer-Moore algorithm is one of the string search algorithms published by Robert S. Boyer 
and J. Strother Moore in 1977. According to (Bell, Powell, Mukherjee, & Adjeroh, 2002) Boyer-Moore algorithm is 
considered one of the most efficient algorithms for general pattern-matching applications. It is able to recognize and 
skip certain areas in the text where no match is found. The determination of string matching is based on the reading 
of Serial Number characters. The Serial Number on a product uses a Bar Code often called a Barcode which is a 
collection of optical data that is read by a machine. In general, we cannot read the barcode manually due to the limited 
ability to read machine language so a system is needed to read from a serial number that uses the barcode. 
The role of the string matching method in this research is part of the process of finding strings or text from a 
combination of serial numbers that have been translated from a barcode using an algorithm. According to (Mulyawati, 
Subagio, & Marth, 2017), String matching is a problem-solving approach to get patterns based on the arrangement of 
string characters contained in part of the content of text or other strings. There are many algorithms in search, one of 
which is the Boyer-Moore algorithm, which is a more efficient search algorithm than the binary algorithm and 
Sequential Search. This is because this algorithm does not need to explore every element of the table according to 
(Faqih, Rahmanto, Aldino, & Waluyo, 2022), translation on Barcode serial number by using the Barcode Generator 


---

## Page 2

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
238 
 
application system which is a barcode translator software application, as a graphical representation of a data or serial 
number information on an item code.  
To solve this research problem, the author identifies how the Barcode Generator works by using the Boyer-Moore 
algorithm appropriately and relevantly.  
 
METHOD 
In this research, the author uses the Barcode Generator application as a barcode scanning on the serial number of 
a product, and in this application, there are many other versions. A barcode is a two-dimensional matrix image that 
can store data in it. Barcodes are an evolution of barcodes. A barcode is a real object marking symbol made of a pattern 
of black and white bars to be easily recognized by a computer (Rahayu, Ramadijanti, & Setiowati, 2011). To search 
for the serial number used with the Boyer-Moore algorithm method, the development process takes several stages of 
research carried out in a planned, organized, and systematic manner. From research (Junaidi, Rahman, & Yunita, 
2021), the stages of this research are part of the research that will determine the success of a study. The following are 
the stages of the research to be carried out: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 1. Research Stages 
 
Data Collection Technique 
In this study, data collection was carried out by taking a sample of objects/datasets from PT Coway International 
Indonesia. in the form of 9 images of serial number codes on products related to research. 
 
Problem Identification 
At this stage, problem development is carried out by collecting data on the needs of the existing system. To 
determine this need, it is necessary to identify the problem to be solved first. Based on the issues that have been 
obtained, then an analysis of system requirements is carried out. The main problem in this study is how the current 
system can facilitate the search for Serial Number Codes that have faded in writing on the item so that users can check 
using the Barcode Generator by scanning the Barcode of the Goods Product. So that we easily know the serial number 
code of the goods. 
 
Application of the Boyer-Moore Algorithm 
An algorithm is a structured sequence of steps to solve a problem or achieve a specific goal. Algorithms involve 
solving problems by decomposing the problem into simple steps, identifying conditions and recurrences, and 
organizing the steps in a logical order. One of the examples of issues that can be solved using algorithms is String 
Data Collection 
Issue Identification 
Implementation of Boyer 
Moore algorithm 
Implementation 
Testing the system 


---

## Page 3

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
239 
 
Matching. According to (Khairunnisa, et al., 2023), String Matching is the application of searching for matches of 
specific patterns in a text or string. 
This search algorithm aims to find a particular element in a data set or information space. Similar to looking for a 
"needle in a haystack." An example of an algorithm used is the Boyer Moore Algorithm. 
The Boyer-Moore algorithm is one of the string search algorithms published by Robert S. Boyer and J. Strother 
Moore in 1977. It is considered the most efficient general application algorithm (Faqih, Rahmanto, Aldino, & Waluyo, 
2022). Unlike previously invented string search algorithms, the Boyer-Moore algorithm starts matching characters 
from the right side of the pattern. The idea behind this algorithm is that by beginning character matches from the right 
and not from the left; more information will be gained. Boyer Moore algorithm includes the most efficient string 
matching algorithm compared to other string matching algorithms. According to (Darmawan, Setianingrum, & Arini, 
2018), due to its efficient nature, many string-matching algorithms have been developed based on the concept of Boyer 
Moore's algorithm. 
According to (Kristanto, Santosa, & Rachmat, 2013)  systematically, the steps that the Boyer-Moore algorithm 
performs when matching strings are: 
- 
The Boyer-Moore algorithm matches the pattern at the beginning of the text. 
- 
From right to left, it matches the pattern character by character with the corresponding character in the text 
until one of the following conditions is met: 
a. The characters in the pattern and the compared text do not match (mismatch). 
b. All characters in the pattern match. Then, the algorithm will notify the discovery at this position. 
- 
The algorithm then shifts the pattern by maximizing the value of the good-suffix shift and the bad-character 
shift, then repeats step 2 until the pattern is at the end of the text (Irawan & Pratama, 2020). 
This algorithm is the most efficient string-matching algorithm compared to the other algorithms. A simplified 
version of this algorithm is often applied in text editors for "search" and "replace" commands. In the process, this 
algorithm scans the pattern characters from right to left, starting with the rightmost position. 
 
Implementation 
At this stage, the author implements research using the Barcode Generator Application as a Barcode Serial Number 
detector of an item or product to be detected. 
 
System Testing 
After all the processes are carried out, the next stage is testing. This stage aims to ensure that the search for string 
matching that has been translated by the Barcode Generator Application can be produced in the application of string 
matching patterns or text from a serial number of the item code. 
 
RESULT AND DISCUSSION 
Data collection was used in this study by taking images from cellphone media in the form of Jpeg / Barcode Images 
of the goods. The application for taking the image image is by using the Barcode Generator.Apk.  
 
Here's how the Barcode Generator APK application works, which is attached: 
 
Table 1. How the Barcode Generator Application Works 
No 
Image Description 
Description 
1 
 
 
 
 
 
 
Barcode Generator App Icon View. 


---

## Page 4

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
240 
 
2 
 
 
 
App view when running. 
 
 
3 
 
 
 
Display of Item Barcode Image Capture 
Process. 
4 
 
 
Display of Image Capture Results 
generated in the form of Product Serial 
Number 
 
Barcode Code Classifications on Numeric as follows: 
  
 
 
 
 
 
 


---

## Page 5

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
241 
 
Table 2. Classification of Barcode Codes on Numeric. 
 
Barcode 
Serial Number 
 
 
 
103 02F64 19814 00017 
 
 
 
107 02F63 19712 00134 
101 02F62 19814 00123 
103 02FBJ 21621 00077 
159 02FCV 21811 00250 
 
 
 
411 02F9W 21414 00411 
 
 
151 02F5Z 20123 00118 


---

## Page 6

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
242 
 
 
 
 
159 02F61 20624 00140 
104 02FB3 21729 00229 
 
 
Barcode Classifications on Numeric as follows: 
 
Figure 3. Classification of Barcode Codes on Numeric. 
 
The alphabetical classification of barcode codes is as follows: 
 
   
Figure 4. Classification of Barcode Codes on Alphabet. 
The Boyer-Moore Algorithm works as follows: 
 


---

## Page 7

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
243 
 
 
 
Iteration 1 (Boyer Moore Algorithm). 
 
 
 
 
Iteration 2 (Boyer Moore Algorithm). 
 
 
 
 
Iteration 3 (Boyer Moore Algorithm). 
 
 
Iteration 4 (Boyer Moore Algorithm). 
 
 
 
 
Iteration 5 (Boyer Moore Algorithm). 
 
 
 


---

## Page 8

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
244 
 
 
 
Iteration 6 (Boyer Moore Algorithm). 
 
 
 
 
Iteration 7 (Boyer Moore Algorithm). 
 
 
 
 
Iteration 8 (Boyer Moore Algorithm). 
 
 
 
 
 
Iteration 9 (Boyer Moore Algorithm). 
 
 
- FINISH - 
Boyer Moore Algorithm Analysis produces several stages, namely., Iteration 1 to 9 steps for the search for String 
Matching determination. As well as with patterns that have occurred as many as 13 (5 +5 + 2 + 1 + 0 + 0 + 0 + 0 + 0). 
The explanation of how this iteration process works with the application of string matching using the Boyer-Moore 
Algorithm method is a very fast and efficient text search application. The process takes place by matching the Pattern 
with the Text. When the Pattern and Text do not match in order, the Pattern will shift according to the number of Text 


---

## Page 9

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
245 
 
conditions that do not match. The shifting/matching will continue until the Text and Pattern conditions have been met 
for the match. Therefore, the final result of the search for String Matching text in the Boyer Moore Algorithm Method 
requires a process of up to Iteration 9. Because at Iteration 9, the conditions of the Text and Pattern have been matched 
/ by the order. 
An algorithm will be considered good and reliable when solving problems efficiently. The main objective of algorithm 
analysis is to understand how efficiently the algorithm works regarding execution time and other resource usage, such 
as memory or storage space. By performing algorithm analysis, we can make better decisions in selecting the right 
algorithm for a particular problem and optimize overall system performance. 
 
No 
Iterations 
Number 
character shift 
count 
1 
1st Iteration 
5 
2 
2nd Iteration 
5 
3 
3rd Iteration 
2 
4 
4th Iteration 
1 
5 
5th Iteration 
0 
6 
6th Iteration 
0 
7 
7th Iteration 
0 
8 
8th Iteration 
0 
9 
9th Iteration 
0 
Total 
13 
 
 
 This search can also be implemented into the Programming Language, Pseudocode, or Source Code of the calculation 
of String Matching patterns that occur in the Boyer Moore Algorithm using the C Programming Language, which can 
be accessed on the page https://github.com/adiyanto122/boyen-moore/blob/main/boyer%20moore.txt. 
From the results of the source code output, the search for the calculation of the String Matching pattern that occurs in 
the Boyer Moore Algorithm using the C Programming Language is found to be repeated nine times, and the pattern 
that occurs is 13 shifts in an execution time of 0.774 seconds. 
 
CONCLUSION 
From the work of analyzing the search for manual calculations on the application of the Boyer Moore Algorithm string 
matching, resulting in 9 iteration processes as a search step for determining String Matching with patterns that have 
occurred as many as 13 shifts, which illustrates that the use of the Boyer Moore algorithm is quite efficient in searching 
strings in a machine. 
 
REFERENCES 
Bell, T., Powell, M., Mukherjee, A., & Adjeroh, D. A. (2002). Searching BWT compressed text with the Boyer-Moore 
algorithm and binary search. Data Compression Conf. Proc. , 112–121. DOI: 10.1109/DCC.2002.999949. 
Darmawan, R. I., Setianingrum, A. H., & Arini. (2018). Implementasi Algoritma Boyer Moore Pada Aplikasi Kamus 
Istilah Kebidanan Berbasis Web. JURNAL SISTEM INFORMASI, 2(1). 
Faqih, Y., Rahmanto, Y., Aldino, A. A., & Waluyo, B. (2022). Penerapan String Matching Menggunakan Algoritma 
Boyer-Moore Pada Pengembangan Sistem Pencarian Buku Online. Bulletin of Computer Science Research, 
2(3).100-106 DOI:10.47065/bulletincsr.v2i3.172. 
Irawan, C., & Pratama, M. R. (2020). Perbandingan Algoritma Boyer-Moore dan Brute Force pada Pencarian Kamus 
Besar Bahasa Indonesia Berbasis Android. BIOS : Jurnal Teknologi Informasi dan Rekayasa Komputer, 1(2), 
DOI: https://doi.org/10.37148/bios.v1i2.13. 
Junaidi, A., Rahman, A., & Yunita, Y. (2021). Prediksi Persediaan Bahan Baku untuk Produksi Percetakan 
Menggunakan 
Metode 
Asosiasi. 
Paradigma 
- 
Jurnal 
Komputer 
dan 
Informatika, 
23(1) 
DOI:10.31294/p.v23i1.9597. 


---

## Page 10

Journal of Computer Networks, Architecture and  
High Performance Computing 
Volume 6, Number 1, January 2024 
https://doi.org/10.47709/cnahpc.v6i1.3410 
 
Submitted : Jan 6, 2024 
Accepted   : Jan 13, 2024 
Published  : Jan 16, 2024 
 
 
* Corresponding author 
  
This is an Creative Commons License This work is licensed under a Creative 
Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC 
BY-NC-SA 4.0). 
246 
 
Khairunnisa, Nurhadi, Jatmiko, A. R., Legito, Saputra, E. A., Syafa'at, F., et al. (2023). Buku Ajar Logika & Algoritma. 
Jambi: PT. Sonpedia Publishing Indonesia. 
Kristanto, S. G., Santosa, G., & Rachmat, A. (2013). Implementasi Algoritma Boyer-Moore Pada Permainan Word 
Search Puzzle. Proceedings of KNASTIK (Konferensi Nasional Teknologi Informasi dan Komunikasi). 
Mulyawati, I., Subagio, R. T., & Marth, D. (2017). Implementasi Metode String Matching Untuk Aplikasi Pengarsipan 
Dokumen (Studi Kasus : Smpn 3 Sumber Kab. Cirebon). JURNAL DIGIT, 7(1). 50-61. 
Rahayu, Y. D., Ramadijanti, N., & Setiowati, Y. (2011). Pembuatan Aplikasi Pembacaan Quick Response Code 
Menggunakan Perangkat Mobile Berbasis J2ME Untuk Identifikasi Suatu Barang. Politeknik Elektronika 
Negeri Surabaya Institut Teknologi Sepuluh Nopember. 
Syafarina, G. A. (2016). Perancangan Aplikasi Inventory Barang Materials Dan Product. Technol. J. Ilm, 7(1). 25–33. 
 


---

