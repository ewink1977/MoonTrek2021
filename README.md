<h1>Moon Trek: The Website 2021</h1>
<h4><em>"Never has so much effort been put in to things no one will ever care about..."</em></h4>
<h6>-Erin Michael Winking</h6>
<img src = "http://moontrek.douglasavenue.com/img/titlebg.jpg" alt = "The Moon Trek Logo">
<h2>What The Hell Is Moon Trek?</h2>
<p>Moon Trek is a fan fiction setting I created back in the late '90s that puts some of the characters from the anime Ranma ½ and 
Sailor Moon in the post Dominion War Star Trek universe.</p>
<p>As of right now, there are 10 full 'novels' (I use that word quite liberally) and two published short stories.</p>
<h2>So... What Is This?</h2>
<p>So, at <a href="https://moontrek.douglasavenue.com" target="_blank">moontrek.douglasavenue.com</a> I currently have a static website
that allows you to view or download the stories. There is also an incomplete 'Wannabe-Wiki' static site that allows you to get some
information on the characters, settings, and whatnot.</p>
<p>This project is an attempt to rebuild the site using Django ORM to place everything in a database, make pages searchable, connect characters, ships, etc. 
to the stories with O2M and M2M relationships, and in general turn the site from your average, everyday static site to a web application.
<h2>Okay... But Why?</h2>
<p>The primary reason is to use the project as a proof of concept that I can build this kind of web app, even if the content is worthless junk.</p>
<p>Plus I do, occassionally, still work on the stories and have been working on rewriting them in general to fix my early 2000's bad writing and 
replace it with my early 2020's bad writing. It's pretty much the same bad writing only with less profanity and sex.</p>
<h2>How Are You Going To Do It?</h2>
<p>The plan right now is to use Django for the backend, creating at least two apps, once that contains the stories, and one that contains the database.</p>
<p>The basic wireframe can be viewed <a href="https://drive.google.com/file/d/1o-2x3ulULSogPf0Zfhd6dcabhv_4SSl-/view?usp=sharing" target="_blank">here</a>. The 
waire frame is not complete at this point, but gives a basic idea of what I am going for. I am hoping to set up an Amazon S3 Bucket to serve the files, and 
host the site on an Amazon EC2 instance.</p>
<h2>Need Any Help?</h2>
<p>Once I get the basics done and enough coded to get something online, I will update with the public URL for 'alpha' and 'beta' versions of the site. Yeah, I know
I am acting like this is a real software development repo, but that's how I learn how to do real versioning and stuff.</p>
<p>You can also feel free to go through the code on here and let me know if you think I am doing something in an inefficiant manner, or in a stupid way that will
cause me issues down the line. Smoochies!</p>
<hr>
<small><strong>current website version: <em>a.0.0</em></strong></small><br />

<a href="https://www.python.org/" target="_blank"><img src="http://ForTheBadge.com/images/badges/made-with-python.svg"></a>
<br />
<a href="http://ForTheBadge.com"><img src="http://ForTheBadge.com/images/badges/uses-html.svg">
<img src="http://ForTheBadge.com/images/badges/uses-css.svg">
<img src="http://ForTheBadge.com/images/badges/uses-js.svg"></a>