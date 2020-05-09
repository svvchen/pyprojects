# pyprojects

**League of Legends subreddit crawler:**

Project that uses PRAW, the reddit API wrapper, to retrieve and analyze data from r/leagueoflegends.

In the code, I retrieve the top 50 posts from the subreddit, then use PRAW to crawl through all comments and replies. From the text, I then fuzzy match on champion names.

My hope in starting this is to get a sense for the most controversial champions in league history. My guess was that Graves and Teemo would be up there, but Yasuo has surprisingly snuck into the top rankings. As expected...he's a pretty abusive champion.

Notes on v1: Karma is the most popular champion, but just because reddit has a “karma” system.


**Rhyme highlighter:**

I got into poetry a while back ago. Here's my attempt at highlighting rhyme schemes, just like Genius does in their [infamous videos](https://www.youtube.com/watch?v=UlCr1Or0He8).

![Highlighted words](https://github.com/svvchen/pyprojects/blob/master/rhyme_scheme_highlighter/Screen%20Shot%202020-05-03%20at%209.20.33%20AM.png)
