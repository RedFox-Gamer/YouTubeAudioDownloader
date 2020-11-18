#pip install pafy
import pafy

url = "https://youtu.be/jNQXAC9IVRw"
video = pafy.new(url)

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.bitrate, i.extension, i.get_filesize())

audiostreams[3].download()