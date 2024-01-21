<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/array-conversion">Array Conversion</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek has an array <strong>a[]</strong>, he wants to convert this array to <strong>b[]</strong> using only XOR operation. He will choose an index<strong> i</strong> and a value <strong>x</strong> such that <strong>a[i] ^ x = b[i]</strong>.<br>
Help him find suitable value of <strong>x</strong> for every index <strong>i </strong>from <strong>1</strong> to <strong>N</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains one&nbsp;integer&nbsp;<strong>N</strong>.<br>
3.&nbsp;The second line of each test case&nbsp;contains <strong>N</strong> space-separated integers which represents <strong>a[]</strong>.</span><br>
<span style="font-size:18px">4.&nbsp;The third line of each test case&nbsp;contains <strong>N</strong> space-separated integers which represents <strong>b[]</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the <strong>N</strong> space-separated integers which represents value of <strong>x</strong> for<strong> i<sup>th</sup></strong> index from <strong>1</strong> to <strong>N&nbsp;</strong>on a new line.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1 ≤&nbsp;T ≤ 100<br>
2. 1&nbsp;≤&nbsp;N&nbsp;≤&nbsp;10<sup>5</sup><br>
3. 1&nbsp;≤&nbsp;a[i], b[i]&nbsp;≤&nbsp;10<sup>9</sup></span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2</span>
<span style="font-size:18px">3</span>
<span style="font-size:18px">7 2 2</span>
<span style="font-size:18px">3 4 2
1
1000000000
3762893
<strong>Output:</strong>
4 6 0
1000579277
<strong>Explanation:</strong>
<strong>Test Case 1 :</strong> 7^4 = 3, 2^6 = 4 and 2^0 = 2.
<strong>Test Case 2 :</strong> 1000000000^1000579277 = 3762893.</span></pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;