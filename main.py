import asyncio
import sys

from twikit.guest import GuestClient

client = GuestClient("ja-JP")


async def main():
    await client.activate()

    user = await client.get_user_by_screen_name(sys.argv[1] or "r_89er")
    tweets = await user.get_tweets()
    favorites = 0
    for tweet in tweets:
        favorites += int(tweet.favorite_count)
    match int(sys.argv[2]):
        case 1:
            power = favorites / int(user.statuses_count)
        case 2:
            power = favorites
        case 3:
            power = int(user.statuses_count)
        case _:
            power = favorites * int(user.statuses_count)
    print(user.screen_name + "'s power: ", power)


if len(sys.argv) < 2:
    sys.argv.append(None)
if len(sys.argv) < 3:
    sys.argv.append(0)
asyncio.run(main())
