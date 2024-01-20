<h2><a href="https://www.geeksforgeeks.org/batch/competitive-programming/track/cp-math-bitMasking/problem/xor-on-array">XOR on Array</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek has an array of <strong>N</strong> elements <strong>a[]</strong>.<br>
He wants to do following operations <strong>N -1</strong> times on array -<br>
1.&nbsp;Remove two elements from the array .<br>
2. Take Bitwise XOR of the removed elements and insert them into the array.<br>
In the end only one element will remain in the array. Geek wants this element to be minimum possible. You have to find the minimum possible element which will be left in the array.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
1.&nbsp;The first line of the input contains a single integer<em> </em> <strong>T</strong> denoting the number of test cases. The description of&nbsp;<strong>T</strong> test cases follows.<br>
2.&nbsp;The first line of each test case contains one integer&nbsp;<strong>N</strong>.<br>
3.&nbsp;The second line of each test case&nbsp;contains <strong>N</strong> space-separated integers which represents <strong>a[]</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong> For each test case, print the answer.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1. 1 ≤&nbsp;T ≤ 100<br>
2. 2&nbsp;≤&nbsp;N&nbsp;≤&nbsp;10<sup>5</sup><br>
3. 1&nbsp;≤&nbsp;a[i]&nbsp;≤&nbsp;10<sup>9</sup></span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2
3 
3 1 2
2 
1 1000000000
<strong>Output:</strong>
0
1000000001
<strong>Explanation:</strong>
<strong>Test Case 1 :</strong> At first Geek will remove 
3 and 2 and insert 3 ^ 2 = 1 into the array. 
Array will become {1, 1}, then Geek will 
remove 1 and 1 and insert 1 ^ 1 = 0 into 
the array,&nbsp;which is minimum possible.
<strong>Test Case 2 :</strong> Geek has only one option 
Geek will remove 1 and 1000000000 and 
insert 1 ^ 1000000000 = 1000000001 into the
array&nbsp;which is minimum possible.</span></pre>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Algorithms</code>&nbsp;