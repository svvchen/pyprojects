# :snake: pyprojects

## Table of Contents
- [League of Legends subreddit crawler](#league-of-legends-subreddit-crawler)
  - [Champion results](champion-results)
  - [To do](to-do)
  - [Notes on v2](notes-on-v2)
- [Rhyme highlighter](#rhyme-highlighter)
  - [Poem higlighting results](poem-higlighting-results)

## League of Legends subreddit crawler

Project that uses [PRAW](https://praw.readthedocs.io/en/latest/), the Reddit API wrapper, to retrieve and analyze data from [r/leagueoflegends](https://www.reddit.com/r/leagueoflegends/). In the code, I retrieve the top 150 posts from the subreddit, then crawl/clean through all post details, comments, and replies. Then, I then fuzzy match on champion names to obtain data on how often a champion is mentioned.

### Champion results

**Raw results:**
```
[('yasuo', [235]), ('fiddlesticks', [227]), ('brand', [162]), ('teemo', [159]), ('thresh', [146]), ('vayne', [128]), ('graves', [116]), ('singed', [110]), ('lux', [109]), ('ryze', [108]), ('skarner', [105]), ('garen', [99]), ('akali', [97]), ("kai'sa", [95]), ('sion', [92]), ('dr. mundo', [86]), ('galio', [86]), ('xayah', [82]), ('mordekaiser', [80]), ('nasus', [80]), ('pyke', [78]), ('aatrox', [74]), ('urgot', [74]), ('nunu and willump', [71]), ('aphelios', [70]), ('heimerdinger', [70]), ('lucian', [70]), ('jhin', [69]), ('amumu', [66]), ('gragas', [66]), ('ezreal', [62]), ('riven', [62]), ('zilean', [62]), ('senna', [61]), ('irelia', [58]), ('zoe', [58]), ('sejuani', [57]), ('ahri', [56]), ('ivern', [56]), ('jinx', [56]), ('shaco', [56]), ('sylas', [54]), ('swain', [53]), ('malphite', [52]), ('veigar', [52]), ('draven', [51]), ('neeko', [50]), ('yuumi', [50]), ('leblanc', [49]), ('rakan', [49]), ('varus', [49]), ('zed', [48]), ('bard', [47]), ('tristana', [47]), ('syndra', [46]), ('leona', [45]), ('sett', [45]), ('braum', [43]), ('alistar', [42]), ('kassadin', [42]), ('warwick', [42]), ('ashe', [41]), ('darius', [41]), ('kalista', [41]), ('lissandra', [41]), ('lulu', [41]), ('caitlyn', [39]), ('pantheon', [39]), ('taric', [39]), ('twisted fate', [39]), ('camille', [38]), ('janna', [38]), ('nocturne', [38]), ('qiyana', [38]), ('taliyah', [38]), ('olaf', [37]), ('rengar', [37]), ('shen', [37]), ('jax', [36]), ('orianna', [36]), ('renekton', [36]), ('ekko', [35]), ('ornn', [35]), ('fizz', [34]), ('gangplank', [34]), ('jayce', [34]), ('soraka', [34]), ('nautilus', [33]), ('poppy', [32]), ('gnar', [31]), ('annie', [30]), ('blitzcrank', [30]), ('karthus', [30]), ('vi', [30]), ('zac', [30]), ('sivir', [29]), ('anivia', [28]), ('maokai', [28]), ('nidalee', [28]), ('rumble', [28]), ('sona', [28]), ('viktor', [28]), ("rek'sai", [27]), ('morgana', [26]), ('malzahar', [25]), ('tryndamere', [25]), ('jarvan iv', [24]), ('tahm kench', [24]), ('talon', [23]), ('ziggs', [23]), ('azir', [22]), ("kog'maw", [22]), ('wukong', [22]), ('xerath', [22]), ('illaoi', [21]), ('cassiopeia', [20]), ('elise', [20]), ('kayle', [20]), ('kayn', [20]), ('kled', [20]), ('shyvana', [20]), ('udyr', [20]), ('zyra', [20]), ('corki', [19]), ('katarina', [19]), ('kindred', [19]), ('trundle', [19]), ("cho'gath", [18]), ('diana', [17]), ('fiora', [17]), ('kennen', [17]), ('lee sin', [17]), ("vel'koz", [16]), ('quinn', [14]), ('rammus', [13]), ("kha'zix", [12]), ('miss fortune', [12]), ('nami', [12]), ('vladimir', [10]), ('yorick', [9]), ('evelynn', [8]), ('hecarim', [8]), ('karma', [8]), ('volibear', [8]), ('xin zhao', [6]), ('twitch', [3]), ('aurelion sol', [0]), ('master yi', [0])]
```
**Plot:**
![Plotted_champion_mentions](https://github.com/svvchen/pyprojects/blob/master/reddit_api_league/champion_popularity_contest.png)

### To Do

* Run this script at a cadence on inbound posts. Start goal was to get data on most controversial champions in league history (apparently, Yasuo!), but would love to extend this functionality to create a "trending champions" feed. 
* Generalize this script to search any subreddit with an input of a list of names and an output of mentions.

### Notes on v2

* Champion name matching is hard, even with fuzzy matching.
  * Added an adjustment ratio to Karma and Twitch. Karma, since Reddit has a karma system on their posts. I did this by analyzing data on Karma (the champion) vs karma (Reddit system) manually to develop a mention ratio. The data is still really inaccurate, but doesn't matter because nobody cares about the champion Karma. Twitch has a similar problem (twitch.tv – league is regularly streamed there).
* Realizing that I should add more name alternatives in my name dictionary. Example: nobody types "Master Yi" – I should be searching on Yi as well. It'd be even better if I could tighten fuzz.ratio for that name (don't want to match on things like "yee" or "yo").

## Rhyme highlighter

I got into poetry a while back ago. Here's my attempt at highlighting rhyme schemes, just like Genius does in their [infamous videos](https://www.youtube.com/watch?v=UlCr1Or0He8).

### Poem higlighting results
![Highlighted words](https://github.com/svvchen/pyprojects/blob/master/rhyme_scheme_highlighter/Screen%20Shot%202020-05-03%20at%209.20.33%20AM.png)

I'm hoping to make this more intelligent so it can start interpreting rhymes within the verse as well.
