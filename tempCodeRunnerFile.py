import asyncio

async def play_with_toy(toy):
    await asyncio.sleep(5)  # Simulate playing with the toy for 5 seconds
    print(f"Finished playing with {toy}")

async def main():
    await asyncio.gather(
        play_with_toy("car"),
        play_with_toy("dinosaur"),
        play_with_toy("puzzle")
    )

asyncio.run(main())