<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/kth-bit">Kth Bit</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given a <strong>M</strong> bit non negative integer <strong>N</strong>. You can perform compliment operation on this integer any arbitrary number of times. You have to ON the <strong>K<sup>th</sup></strong> bit in the integer from the right end.&nbsp;Print the integer after turning&nbsp;ON the <strong>K<sup>th</sup></strong> bit.</span></p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains three space-separated integers&nbsp;integers&nbsp;<strong>N, M&nbsp;</strong>and<strong> K</strong>.</span></p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the answer.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1&nbsp;≤&nbsp;T ≤ 10<sup>5</sup><br>
2. 1&nbsp;≤ K&nbsp;≤ M ≤ 30<br>
3. 0&nbsp;≤ N &lt; 2<sup>M</sup></span></p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2
3 2 2
1 2 2
<strong>Output:</strong>
3
2
<strong>Explanation:</strong>
<strong>Test Case 1 :</strong> Binary representation of 3 is 
11, where 2nd bit is already ON.
<strong>Test Case 2 :</strong> Binary representation of 1 is 
01, we will take compliment of this integer 
to turn on the 2nd bit.</span></pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Bit Magic</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;