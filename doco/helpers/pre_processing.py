import requests
import re
from PIL import Image

####################
#   ### TEXT ###    
####################


def clean_extra_whitespace(text: str) -> str:
    """
        Cleans extra whitespace characters that appear between words.
    """
    cleaned_text = re.sub(r"[\xa0\n]", " ", text)
    cleaned_text = re.sub(r"([ ]{2,})", " ", cleaned_text)
    return cleaned_text.strip()

def clean_dashes(text: str) -> str:
    """
        Cleans dash characters in text.
    """

    return re.sub(r"[-\u2013]", " ", text).strip()

def clean_carriage_return(text: str) -> str: 
    """
        Cleans carriage return in text. 
    """
    return re.sub(r"\r+", " ", text)

def clean(
    text: str,
    extra_whitespace: bool = True,
    dashes: bool = False,
    carriage_return: bool = True, 
    lowercase: bool = False,
) -> str:
    """
        Cleans text.
    """

    cleaned_text = text.lower() if lowercase else text
    cleaned_text = clean_dashes(cleaned_text) if dashes else cleaned_text
    cleaned_text = clean_carriage_return(cleaned_text) if carriage_return else cleaned_text
    cleaned_text = clean_extra_whitespace(cleaned_text) if extra_whitespace else cleaned_text

    return cleaned_text.strip()



####################
#   ### IMAGE ###    
####################


def get_image(image): 
    image = Image.open(image).convert("RGB")
    return image

def load_image(image_str: str) -> Image.Image:
    if image_str.startswith("http"):
        image = Image.open(requests.get(image_str, stream=True).raw).convert("RGB")
    else:
        image = Image.open(image_str).convert("RGB")

    return image
