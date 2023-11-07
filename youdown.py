from pytube import YouTube

# create a YouTube object and get the video
url = 'https://www.youtube.com/watch?v=9DLtzc9KLiw&list=RDMM9DLtzc9KLiw&start_radio=1'
yt = YouTube(url)

# get the first stream (highest resolution)
stream = yt.streams.first()

# download the video to a file
stream.download(output_path='downloads/', filename='video')
