<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/xor-sort">XOR Sort</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given three integers <strong>A</strong>, <strong>B</strong> and <strong>C</strong>, you have to sort them in the order <strong>A ≤ B&nbsp;≤ C</strong>.<br>
For sorting you should choose an integer&nbsp;<strong>X</strong> and take bitwise XOR of <strong>A</strong>, <strong>B</strong> and <strong>C</strong> with <strong>X</strong>. If there are multiple possibilities of choosing <strong>X</strong>, you should choose the smallest one.<br>
If it is impossible to sort them using above operation, print "<strong>-1</strong>" (without quotes).</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains three space-separated integers <strong>A</strong>, <strong>B</strong> and <strong>C</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the answer.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1 ≤ T ≤ 10<sup>5</sup><br>
2. 1&nbsp;≤ A, B, C&nbsp;≤ 10<sup>9</sup></span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2
3 6 4
1 3 3
<strong>Output:</strong>
2
0
<strong>Explanation: </strong>
<strong>Test Case 1 :</strong> 3^2 = 1, 6^2 = 4 and 4^2 = 6.
<strong>Test Case 2 :</strong> A, B and C are already sorted.</span></pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;