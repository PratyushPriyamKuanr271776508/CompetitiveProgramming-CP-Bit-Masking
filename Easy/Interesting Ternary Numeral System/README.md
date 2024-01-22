<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/interesting-ternary-numeral-system">Interesting Ternary Numeral System</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">The Ternary numeral system is a numeral system in which base is 3 and value of every digit is either 0, 1 or 2.<br>
According to Geek Interesting Ternary numeral system is a numeral system in which base is 3 and every digit is represented by either '<strong>z</strong>', '<strong>n</strong>' or '<strong>p</strong>' where '<strong>z</strong>' corresponds to value 0, '<strong>p</strong>'&nbsp;corresponds to value 1&nbsp;and '<strong>n</strong>'&nbsp;corresponds to value -1.<br>
You are given a normal ternary number in the form of&nbsp;string <strong>s</strong> as input, you have to find its corresponding interesting ternary number.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains <strong>s</strong> denoting ternary number.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the answer.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1 ≤ T ≤ 10<sup>4</sup><br>
2. 1&nbsp;≤ |s|&nbsp;≤ 100</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2
11
102
<strong>Output:</strong>
pp
ppn
<strong>Explanation:</strong>
<strong>Test Case 1 :</strong> Value of 11<sub>3</sub> = 4<sub>10</sub> as 
1*3 + 1*1 = 4 and value of pp<sub>3</sub> = 4<sub>10 </sub>as 
1*3 + 1*1 = 4.
<strong>Test Case 2 :</strong> Value of 102<sub>3 </sub>= 11<sub>10</sub> as 
1*9 + 0*3 + 2*1 = 11 and value of ppn<sub>3</sub> = 
11<sub>10 </sub>as 1*9 + 1*3 + (-1)*1 =11.</span></pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;