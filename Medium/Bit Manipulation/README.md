<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/bit-manipulation">Bit Manipulation</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an integer <strong>N</strong>, find the minimum number of&nbsp;rounds required to convert its binary representation to zero.<br>
In one round you can perform any one of the following operations :<br>
1. Change <strong>i<sup>th</sup></strong> bit if <strong>(i+1)<sup>th</sup></strong> bit is ON, and every bit from <strong>(i+2)</strong> to the right end are OFF.<br>
2. Change the rightmost bit.<br>
<strong>Note:</strong> Rightmost bit is the least significant bit&nbsp;<em>i.e.</em> binary representation of 6 would be 110.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains one&nbsp;integer&nbsp;<strong>N</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the answer.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1 ≤ T ≤ 10<sup>4</sup><br>
2. 1&nbsp;≤ N&nbsp;≤ 10<sup>9</sup></span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
3
3
4
786437641
<strong>Output:</strong>
2
7
884990990
<strong>Explanation:</strong>
<strong>Test Case 1 :</strong> We will do following 
sequence of operations : 11 -&gt; 01 -&gt; 00.
<strong>Test Case 2 :</strong> We will do following 
sequence of operations : 100 -&gt; 101 -&gt; 111 
-&gt; 110 -&gt; 10 -&gt; 11 -&gt; 01 -&gt; 00.</span>
</pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;