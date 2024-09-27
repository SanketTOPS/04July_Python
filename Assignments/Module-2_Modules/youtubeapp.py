from pytubefix import YouTube

url="https://www.youtube.com/watch?v=X7phS7CyRQk"

YouTube(url).streams.get_highest_resolution().download()
