from pytube import YouTube
print(" ")
print("--------------------------WELCOME TO IGNES_YT_DOWNLOADER-----------------------------")

print(" ")
#taking url from users....
url=input("paste your url to download a video  :")
#creating obj for youtube class
obj=YouTube(url)
print(" -----------------------------------------------------")
print(f"title of your video is :: {obj.title}")
print("|-----------------------------------------------------|")

#function to download a video
def downloader():
    a=["","240p","360p","480p","720p"]

    for i in range(1,len(a)):
        print(f"select {i} for {a[i]}")

    print("--------------------------------------------------------")
    quality=int(input("enter your choice here :"))
    print("--------------------------------------------------------")

    print(f"you are selected {a[quality]} wait some time ..........")
#assighning video quality  as per user input
    if a[quality]=="240p":
        yt=obj.streams.get_by_resolution(a[quality])
        print(f"File size: {round(yt.filesize * 0.000001, 2)} MegaBytes\n")
        yt.download()

    elif a[quality]=="360p":
        yt=obj.streams.get_by_resolution(a[quality])
        print(f"File size: {round(yt.filesize * 0.000001, 2)} MegaBytes\n")
        yt.download()

    elif a[quality]=="480p":
        yt=obj.streams.get_by_resolution(a[quality])
        print(f"File size: {round(yt.filesize * 0.000001, 2)} MegaBytes\n")
        yt.download()

    elif a[quality]=="720p":
        yt=obj.streams.get_by_resolution(a[quality])
        print(f"File size: {round(yt.filesize * 0.000001, 2)} MegaBytes\n")
        yt.download()

#eception handling
try:
    downloader()
except:
    print("--------------------------------------------------------")
    print("sorry ::)--that format  is not available select another")
    print("--------------------------------------------------------")
    downloader()

print("--------------------------------------------------------")
print(" thank you for using ignes_yt_downloader ")
print("--------------------------------------------------------")
