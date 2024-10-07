from pyrogram import Client, filters
import requests  # Import requests to make API calls


API_URL = 'https://realism-img.codesearch.workers.dev'

# Command to fetch anime image based on prompt
@Client.on_message(filters.command(["gen"]))
def fetch_anime_image(client, message):
    # Get the prompt from the message, joining everything after /anime
    prompt = " ".join(message.command[1:])
    
    if not prompt:
        message.reply("Please provide a prompt, like this: /image cute girl")
        return

    # Construct the API request URL
    request_url = f"{API_URL}/prompt={prompt.replace(' ', '%20')}"  # Encode spaces for the URL

    try:
        # Make a request to the API to fetch the image
        response = requests.get(request_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            image_url = response.json().get('image_url')  # Assuming the API returns a JSON with 'image_url'
            if image_url:
                # Reply with the anime image link
                message.reply_photo(image_url, caption=f" image for prompt: {prompt}")
            else:
                message.reply("Could not fetch an image. Please try again.")
        else:
            message.reply("Error fetching image from the API. Please try again later.")
    except Exception as e:
        message.reply(f"An error occurred: {str(e)}")
        
