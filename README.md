# Playlist Downloader (m3u8-to-mp4) using ffmpeg
downloader from m3u8 video streaming playlists into mp4 using ffmpeg in linux

USAGE:

  1. put `m3u8` files in a directory
  2. put the script `m3u8-to-mp4.py` into the directory
  3. run the script where the `m3u8` files reside:
     ```
     $> python3 m3u8-to-mp4.py
     ```
     
     
HOW TO GET M3U8 FILES:
- download directly if the `m3u8` file is provided;
- use browser's addon to download the hidden `m3u8` file.

HOW THE DOWNLOADER WORKS:
- `m3u8` files only shows the url of the playlist of a live-streaming video;
- `ffmpeg` opens the url, reads the stream and convert each of it into `mp4`.
