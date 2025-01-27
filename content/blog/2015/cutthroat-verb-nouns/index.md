---
title: "Cutthroat verb-nouns"
date: "2015-05-26T12:54:38Z"
tags: ["twitter", "words"]
---

<p><a href="http://thelifeofwords.uwaterloo.ca/catchall-for-cutthroats/">David-Antoine Williams</a> writes:</p>
<blockquote>
<p>What is the difference between a <em>catch-all</em> and a <em>catch-phrase</em>? Both are compounds formed as Verb+Noun, but in <em>catch-all</em>, the noun is the direct object of the verb, whereas in <em>catch-phrase</em> it is the subject. That is, a <em>catch-all</em> is something that catches all things, whereas a <em>catch-phrase</em> is not something that catches phrases – it is a phrase that catches something. Get it?</p>
<p>Recently there has been some discussion of <em>catch-all</em> type compounds, which <a href="http://tankhughes.com/?p=1050">Brianne Hughes</a> has named “cutthroat compounds,” after one of the more suggestive of these. Apparently they’re rare, because they violate a general tendency for compounds in English to put the ‘head’ (e.g. <em>phrase</em>) on the right (‘right-headedness’). Compare F. <em>ouvre-bouteille</em> to E. <em>bottle-opener</em> (not <em>open-bottle</em>), which follows the most common English productive pattern, Object-Verb+er. If <em>catch-all</em> had followed the normal pattern, we’d be talking about an <em>all-catcher</em>, as we talk about <em>dog-catchers</em> and <em>wind-catchers</em>.</p>
</blockquote>
<p>D-AW went on to write a script that unlurked some cutthroats, searching for verbs with left-headed combinations recorded in the entry. I decided to write a script to try another approach -- look for hyphenated nouns where the first part can a verb and the second a noun.</p>
<p>A WordNet list of 117,953 nouns was reduced to just 3,937 hyphenated words, then further reduced to 916 verb-nouns (i.e. a single hyphen, no spaces) via the <a href="http://developer.wordnik.com/docs.html">Wordnik API</a>, then manually whittled down. Of these potential cutthroats, the following <a href="http://www.encyclopediabriannica.com/?p=23">aren't yet on Brianne's list</a>:</p>
<ol>
<li>be-all</li>
<li>cease-fire</li>
<li>counter-revolution</li>
<li>counter-sabotage</li>
<li>cross-classification</li>
<li>cross-division</li>
<li>cross-eye</li>
<li>cross-purpose</li>
<li>cross-question</li>
<li>cross-stitch</li>
<li>dangle-berry</li>
<li>dash-pot</li>
<li>do-good</li>
<li>drop-leaf</li>
<li>end-all</li>
<li>fuss-budget</li>
<li>knock-knee</li>
<li>make-work</li>
<li>squint-eye</li>
<li>sweep-second</li>
</ol>
<p>I've been generous with some of these, some might originally be adjective-noun but can also be seen as verb-noun: it can be argued counter-revolutions are things that counters revolutions, cross-questions are things (also questions) that cross other questions (there are more counter- and cross- words like this). Some might just be wrong, but here they are.</p>
<p>Here's the ones it found that are already on Brianne's list:</p>
<ol>
<li>break-axe</li>
<li>cure-all</li>
<li>do-nothing</li>
<li>drop-seed</li>
<li>know-all</li>
<li>make-peace</li>
<li>rest-harrow</li>
<li>save-all</li>
<li>shove-ha'penny, shove-halfpenny</li>
<li>shut-eye</li>
<li>spend-all</li>
</ol>
<p>And in case I missed any, the full list of 916 verb-nouns is <a href="https://gist.github.com/hugovk/5bdd19859c1bd7d7f7b0#file-wordnet-cutthroats1-txt">here</a> alongside the <a href="https://gist.github.com/hugovk/5bdd19859c1bd7d7f7b0#file-cutthroat-py">Python script</a>.</p>
