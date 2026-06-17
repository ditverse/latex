---
title: "
Fast string matching algorithm
"
source_pdf: "
Faststringmatchingalgorithm.pdf
"
citation_short: "
Al-Howaide dkk. (2010)
"
topic: "
Perbandingan algoritma string matching, termasuk Naive, Rabin-Karp, KMP, dan Wu-Manber
"
---

# 
Fast string matching algorithm

## Metadata Singkat

- File sumber: `
Faststringmatchingalgorithm.pdf
`
- Sitasi singkat: 
Al-Howaide dkk. (2010)
- Relevansi: 
Perbandingan algoritma string matching, termasuk Naive, Rabin-Karp, KMP, dan Wu-Manber

## Teks Hasil Konversi
                                  Fast string matching algorithm
                          Alaâ€™a Al-Howaide, Wail Mardini*, Yaser Khamayseh, Muneer Bani Yasin

                                                   Department of Computer Science
                                              Jordan University of science and Technology
                                                             Irbid, Jordan
                                                        * mardini@just.edu.jo

          Abstractâ€” String matching refers to find all or some of                 To avoid the quadratic number of character
the occurrences of a text (usually called a pattern) in another text.   comparisons performed by the naÃ¯ve algorithm, hashing
Many fields depend on string matching algorithms to extract,            usually used to reduce the cost of comparison.
retrieve, categorize â€¦etc documents as a backbone of the                          The idea is to check only if the contents of the
information system such as information retrieval, data mining,
                                                                        window â€œlook likeâ€ the pattern. So a hashing function is used
text categorization â€¦etc. We propose a fast string matching
algorithm that reduces the effect of the pattern length on the          to check the similarity between these two texts; the pattern
search time. Our algorithm can beat the best know algorithm             P=P[m] and the text T[s+1â€¦s+m]. This idea was first
(Wu-Manber) in some cases. The running complexity of the                introduced by Rabin-Karp (RK). This algorithm computes the
algorithm is O(n/m).                                                    hash value of the next substring in constant time O(1) which
                                                                        can be accomplished by using the advantage of a modulo
          Index Termsâ€”String matching, algorithms, searching,           operation. The hash value of the pattern is computed once as a
design of algorithms.                                                   preprocessing step. When equality between the hash value of
                                                                        the pattern and the hash value of the current substring is found,
                        I. INTRODUCTION                                 then it is necessary to perform an exact match check because
String matching [1] consists in finding one/all the occurrences         hash value equality does not mean exact match. This has the
of a string (more generally called a pattern) in a text. The            cost of Ó©(m) [4]. The running time of this algorithm is also
pattern P consists of m characters is denoted by P=P[1 .. m].           O(m(n-m+1)) since at the worst case a hashing value would be
Similarly, the text is denoted by T=T[1 .. n] with length of n          equal and an exact match check should be performed.
characters. Both strings are built over a finite set of character                 The Knuth Morris Pratt (KMP) algorithm makes use
called an alphabet.                                                     of the information gained by previous symbol comparisons. It
          Most of the string matching algorithms perform a              never re-compares a text symbol that has matched a pattern
preprocessing phase on the pattern to reduce the time needed            symbol. As a result, the complexity of the searching phase is
later to match.                                                         O(n). However, a preprocessing on the pattern is necessary in
          String-matching algorithms have the following                 order to analyze its structure. The preprocessing phase has a
general procedure. It starts by scanning the text using a               complexity of O(m). Since m n, the overall complexity of
window size equal to m. At the beginning it aligns the left             the Knuth-Morris-Pratt algorithm is in O(n) [1].
ends of the window and the text, and then it compares the                         Wu and Manber (WM) [3] introduced an algorithm
characters of the window with the characters of the pattern.            for multi pattern searching, which was enhanced to work with
After a whole match (valid shift) or a mismatch (invalid shift)         single pattern searching by Lecroq [2]. The idea was to hash
of the pattern with the text, it shifts the window to the right. It     the pattern by hashing |P|/q of substrings each of size q in a
repeats the previous procedure again until the left end of the          cumulative manner using a hashing function which produces
window at the position n-m of the text which is the last                values within 0 and 255. Then it uses a function to determine
possible index for matching.                                            the shift amount. This is the preprocessing phase required by
          Different algorithms differ in the comparison step to         this algorithm and it costs O(m/q). In the searching phase if the
find the valid on invalid shifts.                                       shift value of a textâ€™s substringâ€™s hash value>0, the shift
          The rest of the paper is organized as follows. The            amount is applied else an exact match is performed. The
next section presents related works on string matching                  running time of this algorithm is O(n/q).
algorithms. Section III introduces the idea and pseudo-code of
our new algorithm. Performance comparison results are                                       III. THE NEW ALGORITHM
presented in section IV. Section V presents conclusion and              The idea of the new algorithm is to search for the first
future works.                                                           patternâ€™s character within the text. If it was found then it
                                                                        checks the character at distance m if it was also equal to the
                       II. RELATED WORK                                 last patternâ€™s character then it checks the rest of the characters
The naÃ¯ve algorithm [1], which is a single pattern string-              within the substring naively. If a full match was found then it
matching algorithm, finds all valid shifts using a loop to check        will shift the window m characters to the right. Considering
the condition P[1..m]=T[s+1...s+m] for each n-m+1 possible              that all the shifts values from s+1 to s+m-1 are invalid shifts.
shifts. The running time of this algorithm is O(m(n-m+1)).              For example, if P=aaab, T=aaabcdf, and we found that when
the shift amount equal 1 is valid then none of the shifts 2, 3, or        A. Algorithms and environment
4 are valid, since T[4]=b. But if we consider the example            We conducted our experiments of the following four
where p=â€aaaâ€ T=â€aaaaaaaâ€. The suggested algorithm will              algorithms:
find two valid shifts values at 1 and 4 while there are 5 valid      â— The naÃ¯ve algorithm.
shifts values at 1, 2, 3, 4 and 5, this case happen only when the    â— Rabin-Karp algorithm.
text is constructed of repeating the same pattern. Notice this is    â— KMP algorithm.
not the case in the natural English and it is not a very common      â— The enhanced Wu-Manber algorithm for single string
case in other datasets such as DNA sequences and binary.             matching.
          The algorithm is presented in Figure 1. It assumes                   The last algorithm has been tested with another 17
that patternâ€™s characters are mutually independent (doesnâ€™t          different algorithms (BF, BM2Fast, TBM, SSABS, ZT, FS,
account for characters dependences). By this the occurrence of       BOM2, BNDM, FAOSO, SBNDM, SBNDM2, â€¦ etc) in [2].
any character will not effect or give an evidence of another         The results show that the enhanced Wu-Manber was the best
character occurrence. So all characters within the pattern and       in most of the cases. For example, in short pattern length
the text have the same weight and appear to be random. Then          experiments it outperforms all the algorithms over the binary,
selecting any pair of characters will results in average the         the E.coli, and the small alphabet size. For long pattern length
same results and there will be m-2 characters to be checked if       experiments it outperforms all the algorithms over the binary
the two conditions has been satisfied.                               alphabet (at lengths 32, 64, 128, and 256), the E.coli (at
          Selecting the first and the last patternâ€™s characters to   lengths 32-128), the small alphabet, and the English text.
give an evidence of a match allows the usage of a simple loop                  In this paper, the four previously mentioned
for checking the remaining m-2 characters.                           algorithms have been implemented and tested in C++ on
          This algorithm performs in worst case as KMP               different data sets (explained in the next subsection). The
algorithm and it is very simple to implement where there is no       experiments have been ran on a Pentium(R) 4 CPU 3.20 GHz,
preprocessing phase such as most of the algorithms.                  1MG cache and 2 GB of RAM running MS windows XP
 Algorithm NEW(T,P,m,n)                                              professional V.2 service pack 2. Number of runs was chosen
 for sâ†0 to n-m                                                      to satisfy a 95% confidence level [5].
  if P[0]=T[s] and P[m-1]=T[s+m-1]
         j â† 1                                                       Number of runs = ((z*pi*(1-pi))-1/2)2*z
         while j<m-1 do
            if P[j]=T[s+j]                                           where z is a constant equal 1.96 and pi is the correctness
               if j=m-2 then
                        print â€œPattern    occurs                     probability parameter which is usually used to 0.5.
                        with shiftâ€ s
                        s+=m-1
                                                                              The searchâ€™s running time has been measured using
                  j++                                                the clock function in C++ [6].
               else
                  j=m                                                     B. Data sets
   s++                                                               We performed our experiments on different types of text: text
            Figure 1. The new string matching algorithm.             consists of a binary alphabet, text consists of an alphabet of
                                                                     size 12, text consists of a genome contents, and text consists of
          The running time for the for loop is O (n-m) when          an English language alphabet:
there is no matches at either or both of the two characters (first        â— Binary alphabet and alphabet of size 12: the texts are
and last characters). And it will perform n/m steps when there            constructed of 4,000,000 randomly built characters.
is a match at each s+m shift value, so the running time in this           â— Genome: is a DNA sequence composed of the four
case will be O (n/m), Notice that the algorithm doesnâ€™t go                nucleotides bases A, C, G, and T, Adenine, Cytosine,
upon any character more than once.                                        Guanine, and Thymine respectively. We used the file
          It worth noting that the worst case would result in             E.coli of the Large Canterbury Corpus [7], which is
similar performance of the naÃ¯ve algorithm however the case               constructed of 4,638,690 bases.
is not applicable in the typical string matching applications.            â— Natural language: We used the file world192.txt of the
An example for the worst case would occur when                            Large Canterbury Corpus, which constructed of
P=â€aaaaabaâ€ and T=â€aaaaaaaaâ€¦â€. Here, the algorithm will                   2,473,400 of 94 different characters.
predict a match by matching the first and last characters, so it               We take into account both the short patterns (sizes 5,
is going to check the rest of the characters naively. This will      10, 20, and 30 characters) and long patterns (sizes 25 to 210) for
cause a running time O (nm).                                         each pattern length. We repeated the experiments until we
                                                                     reach the 95% of confidence interval as explained before. The
                  IV. EXPERIMENT RESULTS                             results were then averaged and explained in the next
To measure the efficiency of our string matching algorithm we        subsection.
perform several experiments with the previously discussed
algorithms on different data sets.
     C. Results                                                                        8
                                                                                                         naÃ¯ve
To study the effect of the short and long pattern on the                               7                 Rabin-Karp

performance of the string matching algorithm, we have                                  6
                                                                                                         KM P
                                                                                                         Wu-M anber
conducted two main sets of experiments. Figures 2 to 5 show                            5                 new




                                                                                   e
the short pattern results and Figures 6 to 9 shows the long




                                                                                Tim
                                                                                       4
pattern results.                                                                       3
          For short patterns, Figure 2 presents the results on the
                                                                                       2
E.coli genome data set for different pattern sizes. The new
                                                                                       1
algorithm outperforms the KMP for pattern sizes 20 and 30.
                                                                                       0
The new algorithm overcome WM at pattern size of 5 and it
                                                                                            0               10             20             30             40
overcomes the KMP at pattern size of 30 on the English data                                                        Pa tte rn size
set, as shown in Figure 3. Figure 4 shows that the new                                     Figure 5. Results for short pattern on alphabet of size 12.
algorithm performs nearly similar to KMP with a slightly
overcome at pattern sizes 10, 20, and 30 on the binary                                  For long patterns, Figure 6 and Figure 7 show that the
alphabet. For alphabets of size 12, the new algorithm                         new algorithm outperform completely the KMP for all pattern
overcomes WM at pattern size 20 and 30, as shown in Figure                    size on E.coli genome data set and English data set,
5. Notice that WM was not able to find all the occurrences of                 consecutively. The new algorithm was the fastest on the binary
patterns of length 5 and 10 for most of the tests at q=3 (nearly              alphabet data set for pattern sizes from 64 to 1024 and on the
the half of occurrences were missed).                                         alphabet of size 12 data set for all pattern lengths it was the
                                                                              fastest, as shown in Figure 8 and Figure 9 consecutively.
         10
                          naÃ¯ve                                                      300                   naÃ¯ve
                          Rabin-Karp                                                                       Rabin-Karp
          8                                                                          250
                          KMP                                                                              KMP
          6               Wu-Manber                                                  200                   Wu-Manber
  Time




                                                                              Time
                          new                                                                              new
          4                                                                          150
                                                                                     100
          2
                                                                                       50
          0
                                                                                           0
                0            10             20             30            40                      0       200       400        600        800      1000
                                       Pattern size
                                                                                                                  Pattern size
               Figure 2. Results for short pattern on E.coli genome.
                                                                                                Figure 6. Results for long pattern on E.coli genome.
         4.5
                          naÃ¯ve
          4               R abin-Karp
                                                                                     160                   naÃ¯ve
         3.5              KM P                                                       140                   Rabin-Karp
                          Wu-M anber
                                                                                     120                   KMP
          3               new                                                                              Wu-Manber
                                                                                     100
  Time




                                                                              Time




         2.5                                                                                               new
          2                                                                           80
         1.5                                                                          60
          1                                                                           40
         0.5                                                                          20
          0                                                                            0
                0           10            20          30           40                           0        200       400        600       800       1000
                                   Pa ttern size
                                                                                                                   Pattern size
               Figure 3. Results for short pattern on an English text.                         Figure 7. Results for long pattern on an English text.
          9                  naÃ¯ve
          8                  Rabin-Karp                                              300                     naÃ¯ve
          7                  KM P
                                                                                     250                     Rabin-Karp
          6                  Wu-M anber                                                                      KMP
                                                                                     200                     Wu-Manber
  Time




                             new
          5
                                                                              Time




                                                                                                             new
          4                                                                          150
          3
                                                                                     100
          2
          1                                                                            50
          0                                                                                0
                0            10             20             30            40                     0        200       400        600        800      1000
                                    Pa ttern size
                                                                                                                  Pattern size
              Figure 4. Results for short pattern on Binary alphabet.
                                                                                               Figure 8. Results for long pattern on Binary alphabet.
                                                                      searching for long patterns as it doesnâ€™t uses either any extra
       300              naÃ¯ve                                         memory space or massive CPU operations.
       250              Rabin-Karp                                             This algorithm has potential applications when
                        KMP
       200              Wu-Manber
                                                                      resources such as memory and CPU are very limited on the
Time




                        new                                           running machine. Our future work includes improving the
       150
                                                                      algorithm to handle the case where the text is structured of a
       100                                                            repeated pattern. And also extending it by adapting the rule of
        50                                                            distinguishing patternâ€™s characters. by making it more
                                                                      dynamic which will give it an advantage over repeated pattern
         0
                                                                      structure texts.
             0      200        400        600        800      1000
                               Pattern size
         Figure 9. Results for long pattern on alphabet of size 12.                                 REFERENECES
                                                                      [1] T.Cormen, C.Leiserson, R.Rivest and C.Stein "Introduction To Algorithms
                                                                      ", Second edition, 2007.
              V. CONCLUSION AND FUTUR WORK                            [2] T.Lecroq "Fast Exact String Matching Algorithms", vol. 102, pp.229-235,
In this paper, we propose a new string matching algorithm for         2007, Elsevier.
single pattern matching. In our algorithm, the first and last         [3] S.Wu and U.Manber "A Fast Algorithm For Multi-Pattern Searching",
                                                                      1994, NSF.
characters of the pattern were used as matching predictors for
                                                                      [4] C.Charras and T.Lecroq "Exact String Matching Algorithms". http://www-
a pattern match within a text. It is simple where no needs for        igm.univ-mlv.fr/~lecroq/string/
preprocessing phase or complicated calculations. Also the             [5] D.Wackerly, W.Mendenhall and R.Scheaffer "Mathematical Statistics
results show that it is efficient where it overcomes one of the       With Applications", Fifth Edition, 1996.
                                                                      [6] H.M.Deitel and P.J.Deitle "C++ How To Program", Fourth Edition, 2003.
fastest known algorithms in single string matching, WM, when
                                                                      [7]http://www.data-compression.info/Corpora/CanterburyCorpus/,         2010.

