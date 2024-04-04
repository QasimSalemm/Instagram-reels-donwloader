# Instagram-reels-donwloader
 download Instagram reels by giving reels URLs
This Python script is designed to download videos from URLs using the `yt-dlp` library. It prompts the user to enter video URLs one by one, downloads them, and saves them in a specified output directory.

Here's a breakdown of how it works:

1. The `download_video` function takes a video URL and an output directory as input parameters. It uses `subprocess.Popen` to run `yt-dlp` with the specified arguments to download the video.
2. The `main` function is the entry point of the script. It repeatedly prompts the user to enter video URLs until they choose to exit.
3. Inside the main loop:
   - It creates an output directory named "Facebook_Reels" if it doesn't exist.
   - It prompts the user to enter video URLs one by one until the user enters 'd' to finish.
   - For each entered URL, it calls the `download_video` function to download the video to the output directory.
   - After downloading all videos, it asks the user if they want to exit. If the user enters 'y', the loop breaks, and the script ends.

To use this script, you need to have Python installed along with the `yt-dlp` library. You can install `yt-dlp` using pip:

```
pip install yt-dlp
```

After installing `yt-dlp`, you can run the script, and it will guide you through the process of downloading videos.
