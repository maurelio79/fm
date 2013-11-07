fm
==

A small python module

Just an exercise, nothing more.

Intent of this module is to help programmer to quickly work with text file:
read, write, append, prepend, string substitution, ecc.

To use this module just write in your python script

<pre>
from fm import Fm

fm = Fm()
</pre>

Then to call function inside module just use fm as prefix, so for example to call readF function

<pre>
fm.readF()
</pre>

Examples are better than hundreds words ;-)
In examples below, assume that we have a file named <pre>file.txt</pre> with following content:
<pre>
server1,server1.domain.com,192.168.1.2
server2,server2.domain.com,192.168.1.3
server3,server3.domain.com,192.168.1.4
server4,server4.domain.com,192.168.1.5
server5,server5.domain.com,192.168.1.6
server6,server6.domain.com,192.168.1.7
</pre>

<b>readF function - read file</b>

<pre>
text = fm.readF("file.txt")
print text
</pre>
Output:
<pre>
server1,server1.domain.com,192.168.1.2
server2,server2.domain.com,192.168.1.3
server3,server3.domain.com,192.168.1.4
server4,server4.domain.com,192.168.1.5
server5,server5.domain.com,192.168.1.6
server6,server6.domain.com,192.168.1.7
</pre>

<pre>
text = fm.readF("file.txt", param=['list']
print text
</pre>
Output:
<pre>
['server1,server1.domain.com,192.168.1.2\n', 'server2,server2.domain.com,192.168.1.3\n', 'server3,server3.domain.com,192.168.1.4\n', 'server4,server4.domain.com,192.168.1.5\n', 'server5,server5.domain.com,192.168.1.6\n', 'server6,server6.domain.com,192.168.1.7\n']
</pre>
