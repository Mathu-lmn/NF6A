Video1 = {
    "VID" : 1,
    "Title" : "The Sun is closer than you think",
    "Channel" : "The Matrix",
    "Length" : 245,
    "Views" : 1450002,
    "Likes" : 55009,
    "Tags" : "Music",
    "Watched" : "False"
}
Video2 = {
    "VID" : 2,
    "Title" : "I built my own house",
    "Channel" : "Mr Feast",
    "Length" : 668,
    "Views" : 4645985,
    "Likes" : 1331251,
    "Tags" : "Lifestyle, Home",
    "Watched" : "False"
}
Video3 = {
    "VID" : 3,
    "Title" : "Despacito",
    "Channel" : "Luis Fonsi",
    "Length" : 258,
    "Views" : 7876121794,
    "Likes" : 48000000,
    "Tags" : "Music, Dance",
    "Watched" : "False"
}
Video4 = {
    "VID" : 4,
    "Title" : "The best of me",
    "Channel" : "The Weeknd",
    "Length" : 208,
    "Views" : 8085268,
    "Likes" : 5802307,
    "Tags" : "Music, Dance",
    "Watched" : "False"
}
Video5 = {
    "VID" : 5,
    "Title" : "Youtube Rewind 2020",
    "Channel" : "Youtube Rewind",
    "Length" : 1294,
    "Views" : 1736894,
    "Likes" : 149532,
    "Tags" : "Rewind, Trending",
    "Watched" : "False"
}

videos_list = [Video1, Video2, Video3, Video4, Video5]

def add_video(title, channel, length, views, likes, tags, watched):
    new_video = {
        "VID" : str(len(videos_list)+1),
        "Title" : title,
        "Channel" : channel,
        "Length" : length,
        "Views" : views,
        "Likes" : likes,
        "Tags" : tags,
        "Watched" : watched
    }
    videos_list.append(new_video)

add_video("Take on Me", "Ace of Base", 197, 12495823, 149532, "Music, Dance", "False")
add_video("Set Fire to the Rain", "Adele", 258, 1294813, 124920, "Music, Dance", "False")
add_video("Age of Empires 3 Trailer", "Age of Empires 3", 63, 120598832, 19249248, "Video Games, Trailer", "True")
add_video("The Last of us Part II", "The Last of us", 158, 59302928, 36344783, "Video Games, Action", "False")
add_video("GTA VI Trailer", "GTA VI", 158, 85302928, 362383, "Video Games, Action, Trailer", "True")

def watch_video(VID):
    for video in videos_list:
        if video["VID"] == VID:
            video["Watched"] = "True"

watch_video("1")
watch_video("2")
watch_video("5")
watch_video("6")

def sort_videos():
    print("\nBy which parameter you want to sort the videos:")
    print("1. Title")
    print("2. Channel")
    print("3. Length")
    print("4. Views")
    print("5. Likes")
    sort_by = input("Please enter the number of the parameter you want to sort by: ")
    if sort_by == "1":
        videos_list.sort(key=lambda x: x["Title"])
        print("\nThe videos are sorted by title")
    elif sort_by == "2":
        videos_list.sort(key=lambda x: x["Channel"])
        print("\nThe videos are sorted by channel")
    elif sort_by == "3":
        videos_list.sort(key=lambda x: x["Length"])
        print("\nThe videos are sorted by length")
    elif sort_by == "4":
        videos_list.sort(key=lambda x: x["Views"])
        print("\nThe videos are sorted by views")
    elif sort_by == "5":
        videos_list.sort(key=lambda x: x["Likes"])
        print("\nThe videos are sorted by likes")
    else:
        print("Invalid input")

sort_videos()
# print videos ID after sorting
# for video in videos_list:
#     print(video["VID"])

print("\nThe 3 most liked videos are:")
likes_sorted = sorted(videos_list, key=lambda x: x["Likes"], reverse=True)
for i in range(3):
    print(likes_sorted[i]["VID"] , likes_sorted[i]["Title"])

def tag_statistics():
    # returns the number of video the user watched for each tag
    tags_dict = {}
    for video in videos_list:
        for tag in video["Tags"].split(","):
            if tag in tags_dict:
                tags_dict[tag] += 1
            else:
                tags_dict[tag] = 1
    return sorted(tags_dict.items(), key=lambda x: x[1], reverse=True)

print("\nThe most used tags are:")
for tag in tag_statistics():
    print(tag[0].replace(" ", ""), "=" , tag[1],"videos")

def suggest_videos():
    tags_dict = tag_statistics()
    most_watched_tag = tags_dict[0][0]
    most_watched_videos = []
    for video in videos_list:
        if most_watched_tag in video["Tags"].split(","):
            most_watched_videos.append(video)
    most_watched_videos.sort(key=lambda x: x["Views"], reverse=True)
    for video in most_watched_videos:
        if video["Watched"] == "False":
            print("\nThe video", video["VID"], "is the most watched video for the tag", most_watched_tag, "and it has", video["Views"], "views")
            break

suggest_videos()
