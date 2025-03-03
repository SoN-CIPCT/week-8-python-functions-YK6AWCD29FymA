def make_sandwitch(*ingredients):
        """I want these things on my sandwitch!"""
        print("\nGive me a moment bro")
        for ingredient in ingredients:
            print(f" - {ingredient} onto your sandwitch")
        print("Your sandwitch is done")

make_sandwitch("cheese", "chicken")
make_sandwitch("corn", "oysters")