from bs4 import BeautifulSoup

class WebReader: 
    
    def __init__(self): 
        ...

    @staticmethod
    def load_document(url): 
        try:
            if url.endswith('.html'):
                with open(url, 'r', encoding='utf-8') as file:  # Open in text mode for HTMLs
                    soup = BeautifulSoup(file, 'html.parser')
                    text = soup.get_text()
            else:
                raise ValueError("Unsupported file type. Only HTML are supported.")

            return text
        
        except FileNotFoundError:
            print(f"File not found at the specified path: {url}")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred while extracting text: {e}")
            return ""