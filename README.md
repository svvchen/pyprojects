# :snake: pyprojects

## Table of Contents
- [League of Legends subreddit crawler](#league-of-legends-subreddit-crawler)
  - [Champion results](champion-results)
- [Rhyme highlighter](#rhyme-highlighter)
  - [Poem higlighting results](poem-higlighting-results)
  
## League of Legends subreddit crawler

Project that uses [PRAW](https://praw.readthedocs.io/en/latest/), the Reddit API wrapper, to retrieve and analyze data from [r/leagueoflegends](https://www.reddit.com/r/leagueoflegends/). In the code, I retrieve the top 100 posts from the subreddit, then use PRAW to crawl through all comments and replies. From the text, I then fuzzy match on champion names.

### Champion results

```
('fiddlesticks', [216]), ('twitch', [215]), ('yasuo', [168]), ('teemo', [111]), ('brand', [99]), ('graves', [93]), ('skarner', [88]), ('vayne', [84]), ('ryze', [73]), ('lux', [72]), ('nasus', [71]), ('sion', [67]), ('akali', [65]), ('urgot', [59]), ('thresh', [57]), ('amumu', [56]), ('garen', [56]), ('zilean', [56]), ('jhin', [54]), ('aatrox', [50]), ('galio', [50]), ('pyke', [50]), ('zoe', [47]), ('ezreal', [46]), ("kai'sa", [46]), ('lucian', [46]), ('gragas', [45]), ('riven', [45]), ('xayah', [45]), ('malphite', [40]), ('mordekaiser', [40]), ('varus', [40]), ('heimerdinger', [39]), ('bard', [38]), ('sylas', [37]), ('yuumi', [37]), ('camille', [36]), ('jinx', [36]), ('leblanc', [36]), ('ahri', [35]), ('irelia', [35]), ('lissandra', [35]), ('warwick', [34]), ('alistar', [33]), ('kassadin', [33]), ('draven', [32]), ('sejuani', [32]), ('nunu and willump', [31]), ('dr. mundo', [30]), ('ivern', [30]), ('shaco', [30]), ('singed', [30]), ('syndra', [30]), ('rakan', [29]), ('neeko', [28]), ('vi', [28]), ('zed', [28]), ('poppy', [27]), ('swain', [27]), ('gnar', [26]), ('nocturne', [26]), ('olaf', [26]), ('veigar', [26]), ('viktor', [26]), ('ashe', [25]), ('braum', [25]), ('darius', [24]), ('qiyana', [24]), ('jax', [23]), ('maokai', [23]), ('tristana', [23]), ('fizz', [22]), ('janna', [22]), ('nidalee', [22]), ('shen', [22]), ('sivir', [22]), ('kalista', [21]), ('renekton', [21]), ('taric', [21]), ('twisted fate', [21]), ('ekko', [20]), ('jayce', [20]), ('pantheon', [20]), ('tahm kench', [20]), ('taliyah', [20]), ('zac', [20]), ('caitlyn', [19]), ('soraka', [19]), ('xerath', [19]), ('nautilus', [18]), ('jarvan iv', [17]), ('rengar', [17]), ('sett', [17]), ('talon', [17]), ('aphelios', [16]), ('azir', [16]), ('kennen', [16]), ('leona', [16]), ('kayn', [15]), ('lulu', [15]), ('morgana', [15]), ('orianna', [15]), ("rek'sai", [15]), ('rumble', [15]), ('tryndamere', [15]), ('anivia', [14]), ('elise', [14]), ('gangplank', [14]), ('kled', [14]), ('ornn', [14]), ('blitzcrank', [13]), ('corki', [13]), ('illaoi', [13]), ('kayle', [13]), ("kog'maw", [13]), ('malzahar', [13]), ('sona', [13]), ('zyra', [13]), ('annie', [12]), ('karthus', [12]), ('katarina', [12]), ("vel'koz", [12]), ('diana', [11]), ('kindred', [11]), ('lee sin', [11]), ('nami', [11]), ('senna', [11]), ('shyvana', [11]), ('cassiopeia', [10]), ('trundle', [10]), ('vladimir', [9]), ('ziggs', [9]), ('fiora', [8]), ('karma', [8]), ('udyr', [8]), ('wukong', [8]), ("kha'zix", [7]), ("cho'gath", [6]), ('miss fortune', [6]), ('quinn', [6]), ('rammus', [6]), ('xin zhao', [6]), ('yorick', [6]), ('evelynn', [4]), ('hecarim', [4]), ('volibear', [3]), ('aurelion sol', [0]), ('master yi', [0])]
```

I'm hoping to 1. format into a plot and 2. run at a cadence on inbound posts. My hope in starting this is to get a sense for the most controversial champions in league history. My guess was that Graves and Teemo would be up there, but Fiddlesticks, Twitch, and Yasuo have surprisingly snuck into the top rankings.

**Notes on v1:**

* Added an adjustment ratio to Karma, since Reddit has a karma system on their posts. Did this by analyzing data on Karma (the champion) vs karma (Reddit system) manually to develop a mentiRioton ratio. Was horrible, and data's still really inaccurate, but doesn't matter because nobody cares about the champion Karma.
* Realizing that Twitch has a similar problem (twitch.tv -- league is regularly streamed there). Curse you Riot Games.

## Rhyme highlighter

I got into poetry a while back ago. Here's my attempt at highlighting rhyme schemes, just like Genius does in their [infamous videos](https://www.youtube.com/watch?v=UlCr1Or0He8).

### Poem higlighting results
![Highlighted words](https://github.com/svvchen/pyprojects/blob/master/rhyme_scheme_highlighter/Screen%20Shot%202020-05-03%20at%209.20.33%20AM.png)
