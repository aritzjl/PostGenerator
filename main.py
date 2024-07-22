from Quote2Image import Convert, GenerateColors, ImgObject
import json
import random
import re


def sanitize_filename(filename):
    sanitized_filename = re.sub(r'[<>:"/\\|?*\s,]', '_', filename)
    return sanitized_filename


def generate_image(author, quote, bgImagePath, accountName):    
    bg=ImgObject(image=bgImagePath, brightness=80, blur=80)

    img=Convert(
        quote=quote,
        author=author,
        fg=(255, 255, 255),
        bg=bg,
        font_size=40,
        font_type="/usr/share/fonts/truetype/freefont/FreeMono.ttf",
        width=1080,
        height=1080,
        watermark_text="@"+accountName,)

    # Save The Image as a Png file
    imgName = author + "_" + quote[:10]
    imgName = sanitize_filename(imgName)
    imgName = accountName + "/" + imgName + ".png"
    img.save(imgName)

def main():
    print("Hello World!")
    quotesAmt = 10
    # Import all authors list
    authors = json.load(open("authors.json"))
    random.shuffle(authors)
    authors = authors[:quotesAmt]
    
    for author in authors:
        authorName = author["name"]
        authorQuotes = author["quotes"]
        if (len(authorQuotes) == 0):
            continue
        randomQuote = random.choice(authorQuotes)
        
        generate_image(authorName, randomQuote, "template1.jpg", "hitzak")

    
    
if __name__ == "__main__":
    main()