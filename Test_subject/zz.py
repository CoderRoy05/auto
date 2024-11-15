# # first, letting the proxy_list be in the main.py



# import requests
# import random
# import time

# # List of proxies for IP rotation
# proxy_list = [
#     "http://proxy1.example.com:8080",
#     "http://proxy2.example.com:8080",
#     "http://proxy3.example.com:8080",
#     # Add more proxies as needed
# ]

# # List of User-Agent headers for spoofing different devices
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
#     "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
#     # Add more User-Agents as needed
# ]

# # TTV platform endpoints
# VIEW_URL = "https://www.ttv.com/watch/"
# SUBSCRIBE_URL = "https://www.ttv.com/subscribe/"

# # Functions to get a random proxy and user-agent
# def get_random_proxy():
#     return {"http": proxy_list[random.randint(0, len(proxy_list) - 1)]}

# def get_random_user_agent():
#     return user_agents[random.randint(0, len(user_agents) - 1)]

# # Function to increase view with randomized settings
# def increase_view(video_id):
#     session = requests.Session()  # Using a session for cookie handling
#     proxy = get_random_proxy()
#     user_agent = get_random_user_agent()
    
#     headers = {"User-Agent": user_agent}
#     url = f"{VIEW_URL}{video_id}"

#     try:
#         response = session.get(url, headers=headers, proxies=proxy)
#         if response.status_code == 200:
#             print(f"View added to video {video_id} using {proxy} with User-Agent {user_agent}")
#         else:
#             print(f"Failed to add view: {response.status_code}")
#     except Exception as e:
#         print(f"Error during view addition: {e}")

# # Function to increase subscriber count with randomized settings
# def increase_subscriber(channel_id):
#     session = requests.Session()  # Maintain session for cookie handling
#     proxy = get_random_proxy()
#     user_agent = get_random_user_agent()

#     headers = {"User-Agent": user_agent}
#     url = f"{SUBSCRIBE_URL}{channel_id}"

#     try:
#         response = session.post(url, headers=headers, proxies=proxy, data={"action": "subscribe"})
#         if response.status_code == 200:
#             print(f"Subscriber added to channel {channel_id} using {proxy} with User-Agent {user_agent}")
#         else:
#             print(f"Failed to add subscriber: {response.status_code}")
#     except Exception as e:
#         print(f"Error during subscription addition: {e}")

# # Main script to run view and subscriber increase for testing
# def run_bot(video_id, channel_id, view_target=50, sub_target=50):
#     for _ in range(view_target):
#         increase_view(video_id)
#         time.sleep(random.uniform(5, 15))  # Random delay between requests

#     for _ in range(sub_target):
#         increase_subscriber(channel_id)
#         time.sleep(random.uniform(5, 15))  # Random delay between requests

# # Sample video and channel IDs
# video_id = "sample_video_id"
# channel_id = "sample_channel_id"

# # Run the bot for testing
# run_bot(video_id, channel_id)
