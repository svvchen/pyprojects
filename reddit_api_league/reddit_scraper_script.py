#!/opt/anaconda3/bin/python

# run
# pip install praw
# pip install fuzzywuzzy
# pip install python-Levenshtein
# before running the script

from os.path import isfile
import praw
import pprint as pp
import pandas as pd
from time import sleep
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

reddit = praw.Reddit()

subreddit = reddit.subreddit('leagueoflegends')

champion_counter_dictionary = { "aatrox": 0,\
"aatrox":[0],\
"ahri":[0],\
"akali":[0],\
"alistar":[0],\
"amumu":[0],\
"anivia":[0],\
"annie":[0],\
"aphelios":[0],\
"ashe":[0],\
"aurelion sol":[0],\
"azir":[0],\
"bard":[0],\
"blitzcrank":[0],\
"brand":[0],\
"braum":[0],\
"caitlyn":[0],\
"camille":[0],\
"cassiopeia":[0],\
"cho'gath":[0],\
"corki":[0],\
"darius":[0],\
"diana":[0],\
"dr. mundo":[0],\
"draven":[0],\
"ekko":[0],\
"elise":[0],\
"evelynn":[0],\
"ezreal":[0],\
"fiddlesticks":[0],\
"fiora":[0],\
"fizz":[0],\
"galio":[0],\
"gangplank":[0],\
"garen":[0],\
"gnar":[0],\
"gragas":[0],\
"graves":[0],\
"hecarim":[0],\
"heimerdinger":[0],\
"illaoi":[0],\
"irelia":[0],\
"ivern":[0],\
"janna":[0],\
"jarvan iv":[0],\
"jax":[0],\
"jayce":[0],\
"jhin":[0],\
"jinx":[0],\
"kai'sa":[0],\
"kalista":[0],\
"karma":[0],\
"karthus":[0],\
"kassadin":[0],\
"katarina":[0],\
"kayle":[0],\
"kayn":[0],\
"kennen":[0],\
"kha'zix":[0],\
"kindred":[0],\
"kled":[0],\
"kog'maw":[0],\
"leblanc":[0],\
"lee sin":[0],\
"leona":[0],\
"lissandra":[0],\
"lucian":[0],\
"lulu":[0],\
"lux":[0],\
"malphite":[0],\
"malzahar":[0],\
"maokai":[0],\
"master yi":[0],\
"miss fortune":[0],\
"mordekaiser":[0],\
"morgana":[0],\
"nami":[0],\
"nasus":[0],\
"nautilus":[0],\
"neeko":[0],\
"nidalee":[0],\
"nocturne":[0],\
"nunu and willump":[0],\
"olaf":[0],\
"orianna":[0],\
"ornn":[0],\
"pantheon":[0],\
"poppy":[0],\
"pyke":[0],\
"qiyana":[0],\
"quinn":[0],\
"rakan":[0],\
"rammus":[0],\
"rek'sai":[0],\
"renekton":[0],\
"rengar":[0],\
"riven":[0],\
"rumble":[0],\
"ryze":[0],\
"sejuani":[0],\
"senna":[0],\
"sett":[0],\
"shaco":[0],\
"shen":[0],\
"shyvana":[0],\
"singed":[0],\
"sion":[0],\
"sivir":[0],\
"skarner":[0],\
"sona":[0],\
"soraka":[0],\
"swain":[0],\
"sylas":[0],\
"syndra":[0],\
"tahm kench":[0],\
"taliyah":[0],\
"talon":[0],\
"taric":[0],\
"teemo":[0],\
"thresh":[0],\
"tristana":[0],\
"trundle":[0],\
"tryndamere":[0],\
"twisted fate":[0],\
"twitch":[0],\
"udyr":[0],\
"urgot":[0],\
"varus":[0],\
"vayne":[0],\
"veigar":[0],\
"vel'koz":[0],\
"vi":[0],\
"viktor":[0],\
"vladimir":[0],\
"volibear":[0],\
"warwick":[0],\
"wukong":[0],\
"xayah":[0],\
"xerath":[0],\
"xin zhao":[0],\
"yasuo":[0],\
"yorick":[0],\
"yuumi":[0],\
"zac":[0],\
"zed":[0],\
"ziggs":[0],\
"zilean":[0],\
"zoe":[0],\
"zyra":[0]}
champion_name_dictionary = {"aatrox":["aatrox"],\
"ahri":["ahri"],\
"akali":["akali"],\
"alistar":["alistar"],\
"amumu":["amumu"],\
"anivia":["anivia"],\
"annie":["annie"],\
"aphelios":["aphelios"],\
"ashe":["ashe"],\
"aurelion sol":["aurelion sol"],\
"azir":["azir"],\
"bard":["bard"],\
"blitzcrank":["blitzcrank"],\
"brand":["brand"],\
"braum":["braum"],\
"caitlyn":["caitlyn", "cait"],\
"camille":["camille"],\
"cassiopeia":["cassiopeia", "cass"],\
"cho'gath":["cho'gath"],\
"corki":["corki"],\
"darius":["darius"],\
"diana":["diana"],\
"dr. mundo":["dr. mundo", "mundo"],\
"draven":["draven"],\
"ekko":["ekko"],\
"elise":["elise"],\
"evelynn":["evelynn"],\
"ezreal":["ezreal"],\
"fiddlesticks":["fiddlesticks", "fiddle"],\
"fiora":["fiora"],\
"fizz":["fizz"],\
"galio":["galio"],\
"gangplank":["gangplank", "gp"],\
"garen":["garen"],\
"gnar":["gnar"],\
"gragas":["gragas"],\
"graves":["graves"],\
"hecarim":["hecarim"],\
"heimerdinger":["heimerdinger", "heimer"],\
"illaoi":["illaoi"],\
"irelia":["irelia"],\
"ivern":["ivern"],\
"janna":["janna"],\
"jarvan iv":["jarvan iv", "j4"],\
"jax":["jax"],\
"jayce":["jayce"],\
"jhin":["jhin"],\
"jinx":["jinx"],\
"kai'sa":["kai'sa"],\
"kalista":["kalista"],\
"karma":["karma"],\
"karthus":["karthus"],\
"kassadin":["kassadin"],\
"katarina":["katarina"],\
"kayle":["kayle"],\
"kayn":["kayn"],\
"kennen":["kennen"],\
"kha'zix":["kha'zix"],\
"kindred":["kindred"],\
"kled":["kled"],\
"kog'maw":["kog'maw"],\
"leblanc":["leblanc"],\
"lee sin":["lee sin"],\
"leona":["leona"],\
"lissandra":["lissandra"],\
"lucian":["lucian"],\
"lulu":["lulu"],\
"lux":["lux"],\
"malphite":["malphite"],\
"malzahar":["malzahar"],\
"maokai":["maokai"],\
"master yi":["master yi"],\
"miss fortune":["miss fortune", "mf"],\
"mordekaiser":["mordekaiser"],\
"morgana":["morgana", "morg"],\
"nami":["nami"],\
"nasus":["nasus"],\
"nautilus":["nautilus"],\
"neeko":["neeko"],\
"nidalee":["nidalee"],\
"nocturne":["nocturne"],\
"nunu and willump":["nunu and willump", "nunu"],\
"olaf":["olaf"],\
"orianna":["orianna"],\
"ornn":["ornn"],\
"pantheon":["pantheon", "panth"],\
"poppy":["poppy"],\
"pyke":["pyke"],\
"qiyana":["qiyana"],\
"quinn":["quinn"],\
"rakan":["rakan"],\
"rammus":["rammus"],\
"rek'sai":["rek'sai"],\
"renekton":["renekton"],\
"rengar":["rengar"],\
"riven":["riven"],\
"rumble":["rumble"],\
"ryze":["ryze"],\
"sejuani":["sejuani", "sej"],\
"senna":["senna"],\
"sett":["sett"],\
"shaco":["shaco"],\
"shen":["shen"],\
"shyvana":["shyvana"],\
"singed":["singed"],\
"sion":["sion"],\
"sivir":["sivir"],\
"skarner":["skarner"],\
"sona":["sona"],\
"soraka":["soraka"],\
"swain":["swain"],\
"sylas":["sylas"],\
"syndra":["syndra"],\
"tahm kench":["tahm kench"],\
"taliyah":["taliyah"],\
"talon":["talon"],\
"taric":["taric"],\
"teemo":["teemo"],\
"thresh":["thresh"],\
"tristana":["tristana"],\
"trundle":["trundle"],\
"tryndamere":["tryndamere"],\
"twisted fate":["twisted fate", "tf"],\
"twitch":["twitch"],\
"udyr":["udyr"],\
"urgot":["urgot"],\
"varus":["varus"],\
"vayne":["vayne"],\
"veigar":["veigar"],\
"vel'koz":["vel'koz"],\
"vi":["vi"],\
"viktor":["viktor"],\
"vladimir":["vladimir"],\
"volibear":["volibear"],\
"warwick":["warwick"],\
"wukong":["wukong", "wu"],\
"xayah":["xayah"],\
"xerath":["xerath"],\
"xin zhao":["xin zhao"],\
"yasuo":["yasuo"],\
"yorick":["yorick"],\
"yuumi":["yuumi"],\
"zac":["zac"],\
"zed":["zed"],\
"ziggs":["ziggs"],\
"zilean":["zilean"],\
"zoe":["zoe"],\
"zyra":["zyra"]}

selftext_list = []
prep_comment_list = []

for submission in subreddit.top(limit=25):
    initial_comment_tree = submission.comments
    initial_selftext = submission.selftext
    selftext_list.append(initial_selftext)
    prep_comment_list.append(initial_comment_tree.list())

# pp.pprint(prep_comment_list)

comment_list = []

for comment_tree in prep_comment_list:
    for element in comment_tree:
        if isinstance(element, praw.models.reddit.comment.Comment):
            comment_list.append(element)

# pp.pprint(comment_list)

comment_body_list = []

for element in comment_list:
    comment_body_list.append(element.body)

for element in selftext_list:
    comment_body_list.append(element)

# pp.pprint(comment_body_list)

split_filtered_list = []

for element in comment_body_list:
    split_filtered_list.append(re.split(r'\W+', element))

split_filtered_list = [item for sublist in split_filtered_list for item in sublist]

# print(split_filtered_list)

# for word in split_filtered_list:
#     for champion in champion_name_list:
#         if fuzz.ratio(word, champion) > 90:
#             champions_dictionary[champion] += 1

# print(split_filtered_list)

for word in split_filtered_list:
    for champ_name_sublist_key in champion_name_dictionary:
        for name in champion_name_dictionary[champ_name_sublist_key]:
            if fuzz.ratio(word, name) > 90:
                champion_counter_dictionary[champ_name_sublist_key][0] += 1

# print(champion_counter_dictionary)

print(sorted(champion_counter_dictionary.items(), key = lambda x: x[1], reverse = True))
