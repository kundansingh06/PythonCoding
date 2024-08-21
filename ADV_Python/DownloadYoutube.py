from pytube import YouTube
SAVE_PATH = "C:/Users/kunda/Downloads"
def Download(link, path='.'):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        print(f"Downloading '{youtubeObject.title}'...")
        youtubeObject.download(output_path=SAVE_PATH)
        #youtubeObject.download(output_path=path)
        print('ALL Video downloaded successfully!')
    except Exception as e:
        print(f"Error: {e}")

link = input("Enter the YouTube video URL: ")
#Download("https://www.youtube.com/watch?v=5BrHQRp9VQs&list=PLl8w8gCvr4jKiMpHVqEtFgzaPuQ9SMR5O&index=1")
Download(link)