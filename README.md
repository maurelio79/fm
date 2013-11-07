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

<h3>readF function - read file</h3>

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
Now passing the param <a href="http://docs.python.org/3/tutorial/introduction.html#lists">'list'</a>
<pre>
text = fm.readF("file.txt", param=['list']
print text
</pre>
Output:
<pre>
['server1,server1.domain.com,192.168.1.2\n', 'server2,server2.domain.com,192.168.1.3\n', 'server3,server3.domain.com,192.168.1.4\n', 'server4,server4.domain.com,192.168.1.5\n', 'server5,server5.domain.com,192.168.1.6\n', 'server6,server6.domain.com,192.168.1.7\n']
</pre>
So, for example, adding a simple cycle
<pre>
text = fm.readF("file.txt", param=['list'])
for i in text:
        line_split = i.split(",")
        print "Hostname is %s" % (line_split[0])
        print "Alias is %s" % (line_split[1])
        print "Ip is %s" % (line_split[2])

</pre>
we can get the following output
<pre>
Hostname is server1
Alias is server1.domain.com
Ip is 192.168.1.2

Hostname is server2
Alias is server2.domain.com
Ip is 192.168.1.3

Hostname is server3
Alias is server3.domain.com
Ip is 192.168.1.4

Hostname is server4
Alias is server4.domain.com
Ip is 192.168.1.5

Hostname is server5
Alias is server5.domain.com
Ip is 192.168.1.6

Hostname is server6
Alias is server6.domain.com
Ip is 192.168.1.7

</pre>

<h3>writeF function - write text in file</h3>
Ok, this is simple
<pre>
fm.writeF("file.txt", "w", "New text file")
</pre>
or
<pre>
fm.writeF("file.txt", "a", "new text in append")
</pre>

<h3>prependF function - prepend text in file</h3>
<pre>
fm.prependF("file.txt", "# This is my server list")
</pre>
The result will be the following file:
<pre>
# This is my server list
server1,server1.domain.com,192.168.1.2
server2,server2.domain.com,192.168.1.3
server3,server3.domain.com,192.168.1.4
server4,server4.domain.com,192.168.1.5
server5,server5.domain.com,192.168.1.6
server6,server6.domain.com,192.168.1.7
</pre>

<h3>substrF function - find & replace string or more strings in file</h3>
String to find and string to replace need to be passed as python <a href="http://docs.python.org/3/tutorial/datastructures.html#dictionaries">dictionary</a>.
<pre>
dic = {",":"-","com":"org"}
fm.substrF("file.txt", dic)
</pre>
The result will be the following file
<pre>
server1-server1.domain.org-192.168.1.2
server2-server2.domain.org-192.168.1.3
server3-server3.domain.org-192.168.1.4
server4-server4.domain.org-192.168.1.5
server5-server5.domain.org-192.168.1.6
server6-server6.domain.org-192.168.1.7
</pre>
As you can see, we change every occurence of ',' to '-' and every occurence of 'com' to 'org'
You can add as many string as you want.
