# Download each song in a playlist from youtube and save it to a folder
import os 
import sys
import pytube
from pytube import Playlist
import youtube_dl



// get all the videos in a playlist and store the url's in a list
func getPlaylistVideos(playlistUrl string) []string {
    playlist := Playlist(playlistUrl)
    videoUrls := playlist.VideoURLs
    return videoUrls
}


// using youtube_dl download all the videos in  the list to a folder
func downloadVideos(videoUrls []string, folderName string) {
    for _, url := range videoUrls {
        ydlOpts := map[string]interface{}{
            "format": "best",
            "outtmpl": folderName + "/%(title)s.%(ext)s",
        }
        with youtube_dl.YoutubeDL(ydlOpts) as ydl:
            ydl.download([url])
        }
    }


// use youtube_dl to convert the videos to mp3
func convertToMp3(folderName string) {
    // use youtube_dl to convert the videos to mp3
    convertToMp3(folderName)
    // get the list of mp3 files in the folder
    mp3Files := os.listdir(folderName)
    // use youtube_dl to convert the mp3 files to mp3
    for mp3File := range mp3Files {
        ydlOpts := map[string]interface{}{
            "format": "bestaudio/best",
            "outtmpl": folderName + "/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with youtube_dl.YoutubeDL(ydlOpts) as ydl:
            ydl.download([mp3File])
    }
}


// main function
func main() {
    // get the playlist url from the user
    playlistUrl := os.Args[1]
    // get the folder name from the user
    folderName := os.Args[2]
    // get the list of videos in the playlist
    videoUrls := getPlaylistVideos(playlistUrl)
    // download the videos
    downloadVideos(videoUrls, folderName)
    fmt.Println("Download complete")
}