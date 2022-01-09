<h1>OUTDATED, update to v2.0 soon</h1>
<h1>FLYING TIME BAR - Twitter Bot</h1>

<p align="center">
  <img src="/images/timefliesbg.jpg"/>
</p>

<h2>Purpose</h2>
<p>This is my first project featuring Python3 and Twitter APIs. Also is kind of a reflection.
(Merely made with educational purposes).</p>

<h2> How it works </h2>
<p>It all focuses on a Twitter automatized account <a href="https://twitter.com/timefliesbar">@timefliesbar</a> whose philosophy is "Time flies, make the most of it".</p>
<p>Every day, at 12 o'clock in the morning, this profile shows us the percentage of the year that has elapsed in the shape of a reverse progress bar, unless that day is one of the symbolic moments in the course of the year (25%, 50%, 75%, 99%, 0%) when it shows a short message with no progress bar.</p>
<p>This project was developed with the intention to show how fast time goes, and trying to give the sensation of "lost" while showing a regresive bar instead a regular one. Everything to try to help us to relativize and understand the course of life a little bit better.</p>
<p><i>This is quite an early version, and will support some interactions and/or better, more interesting facts or events.</i></p>

<h2>Index</h2>

<h3>tfb.py</h3>
<p>Main routine. Here This file is the one that calls the different functions when executed (according to a pre-established schedule) and converts the results in tweets. (Eventually, this functions will collapse in one single module)</p>
<h3>tfb_numbers.py</h3>
<p>This function calcultes necessary numbers related to dates, days, hours, minutes, etc. As well as conversions needed.</p>
<h3>tfb_progressbar.py</h3>
<p>This function generates the graphic representation of the progressbar.</p>
<h3>tfb_milestones.py</h3>
<p>This function gives information about representative numeric moments in the year progress.</p>
<h3>tfb_funfacts.py</h3>
<p>This last function expresses some interesting numbers, like the minutes that are left in a year. (Currently not used)</p>
 
<br/>
<p align="center">
  <img src="/images/timeflieslogo.jpg"/>
</p>
