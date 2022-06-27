# Download each song in a playlist from youtube and save it to a folder
# import os 
# import sys
# import pytube
# from pytube import Playlist
# import youtube_dl
# 
# 
# 
// # get all the videos in a playlist and store the url's in a list
// void get_playlist_videos(char* playlist_url, char* video_urls[])
// {
//     Playlist *playlist = Playlist(playlist_url);
//     int i = 0;
//     for (Video* video : playlist.videos)
//     {
//         video_urls[i] = video.url;
//         i++;
//     }
// }
// 
// 
// // using youtube_dl download all the videos in  the list to a folder
// void download_videos(char* video_urls[], char* folder_name)
// {
//     for (int i = 0; i < sizeof(video_urls) / sizeof(char*); i++)
//     {
//         char* url = video_urls[i];
//         char* outtmpl = malloc(strlen(folder_name) + strlen(url) + 5);
//         sprintf(outtmpl, "%s/%s", folder_name, url);
//         youtube_dl_opts = {
//             'format': 'best',
//             'outtmpl': outtmpl
//         };
//         with youtube_dl.YoutubeDL(youtube_dl_opts) as ydl:
//             ydl.download([url]);
//     }
// }
// 
// // use youtube_dl to convert the videos to mp3
// void convert_to_mp3(char* folder_name)
// {
//     // use youtube_dl to convert the videos to mp3
//     char* mp3_files[];
//     for (int i = 0; i < sizeof(mp3_files) / sizeof(char*); i++)
//     {
//         char* mp3_file = mp3_files[i];
//         char* outtmpl = malloc(strlen(folder_name) + strlen(mp3_file) + 5);
//         sprintf(outtmpl, "%s/%s", folder_name, mp3_file);
//         youtube_dl_opts = {
//             'format': 'bestaudio/best',
//             'outtmpl': outtmpl,
//             'postprocessors': [{
//                 'key': 'FFmpegExtractAudio',
//                 'preferredcodec': 'mp3',
//                 'preferredquality': '192',
//             }],
//         };
//         with youtube_dl.YoutubeDL(youtube_dl_opts) as ydl:
//             ydl.download([mp3_file]);
//     }
// }
// 
// // main function
// void main()
// {
//     // get the playlist url from the user
//     char* playlist_url = input("Enter the playlist url: ");
//     // get the folder name from the user
//     char* folder_name = input("Enter the folder name: ");
//     // get the list of videos in the playlist
//     char* video_urls[];
//     get_playlist_videos(playlist_url, video_urls);
//     // download the videos
//     download_videos(video_urls, folder_name);
//     printf("Download complete");
// }