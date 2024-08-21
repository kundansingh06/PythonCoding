from pytube import YouTube
# Where to save
SAVE_PATH = "D:/Bigdata/AWS/AWS Made Easy/AWS Lambda For Beginners- 5 Tutorials"  # to_do

# Links of the videos to be downloaded
links = ["https://www.youtube.com/watch?v=5BrHQRp9VQs&list=PLl8w8gCvr4jKiMpHVqEtFgzaPuQ9SMR5O&index=1"]

for link in links:
    try:
        # Object creation using YouTube which was imported in the beginning
        yt = YouTube(link)
    except:
        # Handle exception
        print("Connection Error")

    # Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4').all()
    # Get the video with the highest resolution
    d_video = mp4_streams[-1]

    try:
        # Download the video
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except:
        print("Some Error!")

print('Task Completed!')