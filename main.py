import asyncio

from twikit.guest import GuestClient

client = GuestClient("ja-JP")


async def main():
    await client.activate()

    tweets = await (await client.get_user_by_screen_name("r_89er")).get_tweets()
    for tweet in tweets:
        print(tweet.favorite_count)
    print("tweets count:", len(tweets))


asyncio.run(main())
