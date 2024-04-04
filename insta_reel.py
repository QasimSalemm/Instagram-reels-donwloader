import os
import requests
import re
from tqdm import tqdm

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_reel(reel_link, directory):
    try:
        # Extract reel ID from the link
        matches = re.findall(r'reels\/(.*?)\/', reel_link)
        if not matches:
            print("No reel ID found in the provided link:", reel_link)
            return
        reel_id = matches[0]

        # Check if the video already exists in the directory
        file_path = os.path.join(directory, f'{reel_id}.mp4')
        if os.path.exists(file_path):
            print(f"Skipping download for {reel_id}.mp4 as it already exists.")
            return

        # Send request to Instagram's API to get video URL
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
        }
        params = {
            'hl': 'en',
            'query_hash': 'b3055c01b4b222b8a47dc12b090e4e64',
            'variables': '{"child_comment_count":3,"fetch_comment_count":40,"has_threaded_comments":true,"parent_comment_count":24,"shortcode":"' + reel_id + '"}'
        }
        response = requests.get("https://www.instagram.com/graphql/query/", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        video_url = data['data']['shortcode_media']['video_url']

        # Download the video with progress bar
        with requests.get(video_url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            with open(file_path, 'wb') as f, tqdm(
                    desc=f"{reel_id}.mp4",
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
            ) as pbar:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Reel downloaded successfully as {}.mp4".format(reel_id))
    except Exception as e:
        print("Failed to download reel:", str(e))

def main():
    # Create directory for storing reels if it doesn't exist
    directory = "Instagram_Reels"
    create_directory_if_not_exists(directory)

    links = []
    while True:
        # Prompt user to enter a reel link or 'd' to start downloading
        user_input = input("Enter Instagram reel link one by one (enter 'd' to start downloading): ").strip()
        if user_input.lower() == 'd':
            break
        elif user_input.lower() == 'n':
            continue
        links.append(user_input)

    # Download all the collected links
    for link in links:
        download_reel(link, directory)

    # Ask user if they want to exit
    while True:
        exit_choice = input("Do you want to exit (y/n)? ").strip().lower()
        if exit_choice == 'y':
            break
        elif exit_choice == 'n':
            main()  # Restart the process for entering more links
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
