# :snake: pyprojects

## Table of Contents
- [League of Legends subreddit crawler](#league-of-legends-subreddit-crawler)
  - [Champion results](champion-results)
- [Rhyme highlighter](#rhyme-highlighter)
  - [Poem higlighting results](poem-higlighting-results)
  
## League of Legends subreddit crawler

Project that uses [PRAW](https://praw.readthedocs.io/en/latest/), the reddit API wrapper, to retrieve and analyze data from [r/leagueoflegends](https://www.reddit.com/r/leagueoflegends/). In the code, I retrieve the top 50 posts from the subreddit, then use PRAW to crawl through all comments and replies. From the text, I then fuzzy match on champion names.

### Champion results

```
[('karma', [359]), ('yasuo', [98]), ('twitch', [92]), ('graves', [78]), ('fiddlesticks', [55]), ('zilean', [53]), ('ryze', [38]), ('akali', [36]), ('galio', [36]), ('lucian', [36]), ('amumu', [35]), ("kai'sa", [35]), ('xayah', [35]), ('vayne', [32]), ('gragas', [31]), ('jhin', [31]), ('thresh', [30]), ('leblanc', [29]), ('alistar', [27]), ('riven', [27]), ('brand', [26]), ('camille', [26]), ('heimerdinger', [26]), ('lux', [26]), ('urgot', [26]), ('sion', [25]), ('varus', [24]), ('sylas', [22]), ('syndra', [22]), ('irelia', [21]), ('lissandra', [21]), ('rakan', [20]), ('viktor', [20]), ('aatrox', [18]), ('braum', [18]), ('draven', [18]), ('nocturne', [18]), ('olaf', [18]), ('sivir', [18]), ('tahm kench', [18]), ('malphite', [17]), ('qiyana', [17]), ('garen', [16]), ('neeko', [16]), ('teemo', [16]), ('dr. mundo', [13]), ('jax', [13]), ('mordekaiser', [13]), ('pantheon', [13]), ("rek'sai", [13]), ('nunu and willump', [12]), ('vi', [12]), ('corki', [11]), ('ezreal', [11]), ('fizz', [11]), ('gnar', [11]), ('nautilus', [11]), ('renekton', [11]), ('shen', [11]), ('gangplank', [10]), ('jayce', [10]), ('kalista', [10]), ('maokai', [10]), ('orianna', [10]), ('ornn', [10]), ('poppy', [10]), ('taric', [10]), ('xerath', [10]), ('kennen', [9]), ('morgana', [9]), ('nami', [9]), ('shaco', [9]), ('singed', [9]), ('twisted fate', [9]), ('zac', [9]), ('zoe', [9]), ('ashe', [8]), ('elise', [8]), ('jinx', [8]), ('kayle', [8]), ("kog'maw", [8]), ('lee sin', [8]), ('rengar', [8]), ('taliyah', [8]), ('tristana', [8]), ('yuumi', [8]), ('zed', [8]), ('aphelios', [7]), ('jarvan iv', [7]), ('kassadin', [7]), ('pyke', [7]), ('skarner', [7]), ('talon', [7]), ('tryndamere', [7]), ("vel'koz", [7]), ('anivia', [6]), ('cassiopeia', [6]), ('darius', [6]), ('janna', [6]), ("kha'zix", [6]), ('leona', [6]), ('nidalee', [6]), ('rumble', [6]), ('veigar', [6]), ('warwick', [6]), ('xin zhao', [6]), ('ahri', [5]), ('azir', [5]), ('caitlyn', [5]), ('ivern', [5]), ('kled', [5]), ('sejuani', [5]), ('swain', [5]), ('annie', [4]), ('ekko', [4]), ('evelynn', [4]), ('karthus', [4]), ('katarina', [4]), ('kindred', [4]), ('lulu', [4]), ('shyvana', [4]), ('udyr', [4]), ('blitzcrank', [3]), ('nasus', [3]), ('sona', [3]), ('trundle', [3]), ('ziggs', [3]), ('fiora', [2]), ('quinn', [2]), ('senna', [2]), ('vladimir', [2]), ('zyra', [2]), ('bard', [1]), ('illaoi', [1]), ('kayn', [1]), ('malzahar', [1]), ('miss fortune', [1]), ('rammus', [1]), ('sett', [1]), ('yorick', [1]), ('aurelion sol', [0]), ("cho'gath", [0]), ('diana', [0]), ('hecarim', [0]), ('master yi', [0]), ('soraka', [0]), ('volibear', [0]), ('wukong', [0])]
```

I'm hoping to 1. format into a plot and 2. run at a cadence on inbound posts. My hope in starting this is to get a sense for the most controversial champions in league history. My guess was that Graves and Teemo would be up there, but Yasuo has surprisingly snuck into the top rankings. As expected -- he's a pretty abusive champion.

Notes on v1:

* Karma is the most popular champion, but just because reddit has a “karma” system. Trying to find a way to get around this.
* Code sucks, I know. I'll get to it.

## Rhyme highlighter

I got into poetry a while back ago. Here's my attempt at highlighting rhyme schemes, just like Genius does in their [infamous videos](https://www.youtube.com/watch?v=UlCr1Or0He8).

### Poem higlighting results
![Highlighted words](https://github.com/svvchen/pyprojects/blob/master/rhyme_scheme_highlighter/Screen%20Shot%202020-05-03%20at%209.20.33%20AM.png)
