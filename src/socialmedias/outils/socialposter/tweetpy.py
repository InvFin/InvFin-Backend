import io
import math
import textwrap
import time
from typing import Dict
import urllib

import tweepy

from src.content_creation import constants

from ...constants import TWEET_MAX_LENGTH, TWITTER


class Twitter:
    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        access_token: str,
        access_token_secret: str,
    ) -> None:
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def do_authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        twitter_api = tweepy.API(auth)
        return twitter_api

    def tweet_text(self, twitter_api, status, **kwargs):
        response = twitter_api.update_status(status=status, **kwargs)
        json_response = response._json
        return json_response["id"]

    def tweet_with_media(self, twitter_api, status, media_url):
        data = urllib.request.urlopen(media_url).read()
        file_like_object = io.BytesIO(data)
        response = twitter_api.update_status_with_media(
            status, "fake_name.jpg", file=file_like_object
        )
        json_response = response._json
        return json_response["id"]

    def create_thread(
        self,
        title: str,
        content: str,
        hashtags: str,
        link: str,
        media_url: str,
        post_type: str,
    ):
        twitter_api = self.do_authenticate()
        total_number_parts = int(math.ceil(len(content) / TWEET_MAX_LENGTH))

        initial_tweet = f"{title} [0/{total_number_parts}]"

        if post_type != constants.POST_TYPE_TEXT:
            initial_tweet_response = self.tweet_with_media(
                twitter_api, initial_tweet, media_url
            )
        else:
            initial_tweet_response = self.tweet_text(twitter_api, initial_tweet)

        list_tweets = {
            "post_response": [
                {
                    "social_id": initial_tweet_response,
                    "content": title,
                    "post_type": post_type,
                    "use_hashtags": False,
                    "use_emojis": True,
                    "use_link": False,
                    "use_default_title": True,
                    "use_default_content": False,
                    "platform_shared": TWITTER,
                }
            ]
        }

        for index, part in enumerate(textwrap.wrap(content, TWEET_MAX_LENGTH)):
            if index == 0:
                response = initial_tweet_response
            index += 1
            tweet = f"{part} [{index}/{total_number_parts}]"
            time.sleep(5)
            response = self.tweet_text(
                twitter_api,
                status=tweet,
                in_reply_to_status_id=response,
                auto_populate_reply_metadata=True,
            )
            list_tweets["post_response"].append(
                {
                    "social_id": initial_tweet_response,
                    "content": tweet,
                    "post_type": constants.POST_TYPE_THREAD,
                    "use_hashtags": False,
                    "use_emojis": False,
                    "use_link": False,
                    "use_default_title": False,
                    "use_default_content": True,
                    "platform_shared": TWITTER,
                }
            )

        last_tweet = (
            f"Si este thread te ha gustado no te pierdas el resto en: {link} {hashtags}"
        )
        last_tweet_response = self.tweet_text(twitter_api, last_tweet)
        list_tweets["post_response"].append(
            {
                "social_id": last_tweet_response,
                "content": last_tweet,
                "post_type": constants.POST_TYPE_THREAD,
                "use_hashtags": True,
                "use_link": True,
                "use_emojis": False,
                "use_default_title": False,
                "use_default_content": False,
                "platform_shared": TWITTER,
            }
        )

        return list_tweets

    def post(self, **kwargs) -> Dict:
        media_url = kwargs.get("media", "")
        if not media_url.startswith("http"):
            media_url = f"https://inversionesyfinanzas.xyz{media_url}"

        return self.create_thread(
            kwargs["title"],
            kwargs["content"],
            kwargs["hashtags"],
            kwargs["link"],
            media_url,
            kwargs["post_type"],
        )
