<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/xor-operation">XOR Operation</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek loves <a href="https://en.wikipedia.org/wiki/Exclusive_or">XOR</a> operation. He wants to solve a problem related to&nbsp;XOR operation but his algorithm is taking exponential time, so he needs your help.&nbsp;<br>
Given an array <strong>a[]</strong> of <strong>N</strong> elements, you have to partition the array into two non-empty parts<em> i.e.</em> partition at <strong>i</strong> will divide the array into two arrays - one consisting elements&nbsp;from index <strong>1</strong> to <strong>i</strong> and other consisting elements&nbsp;from index <strong>(i + 1)</strong> to <strong>N</strong>. You want to divide the array in such a way that XOR of sum of elements of first array and sum of elements of second array is minimum.<br>
You have to find the&nbsp;minimum XOR value.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains one&nbsp;integer&nbsp;<strong>N</strong>.<br>
3.&nbsp;The second line of each test case&nbsp;contains <strong>N</strong> space-separated integers which represents <strong>a[]</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the answer.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1&nbsp;≤&nbsp;T ≤ 10<br>
2. 2&nbsp;≤&nbsp;N&nbsp;≤&nbsp;10<sup>5</sup></span><br>
<span style="font-size:18px">3. 1&nbsp;≤&nbsp;a[i]&nbsp;≤&nbsp;10</span><sup>9</sup><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2
5
1 2 5 9 3
4
1 2 4 8
<strong>Output:</strong>
4
15
<strong>Explanation:</strong>
<strong>Test Case 1 :</strong> We will partition the array 
at index 3 which will give us two arrays - 
{1, 2, 5} and {9, 3} and minimum value of 
XOR of sum of elements of first array 
and sum of elements of second array = 
(1 + 2 + 5) ^ (9 + 3) = 8 ^ 12 = 4. Any 
other partition will give a larger XOR value.
<strong>Test Case 2 :</strong> We can partition the array at 
any index. Every partition will give us 
XOR value of 15.</span>
</pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>prefix-sum</code>&nbsp;<code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;