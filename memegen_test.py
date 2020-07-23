# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('drake.png')

    # add text to the top and bottom of the meme
    meme_gen.add_text('watching cs50 lectures in normal speed', 500, 5)
    meme_gen.add_text('watching cs50 lectures in 2x speed', 500, 500)

    # generate the meme!
    meme_gen.render()


if __name__ == '__main__':
    main()
