import pypdf

class DocParser:
    supported_format = [".pdf", ".doc", ".docx"]
    # TODO: more features = ['basic', 'dl-based', 'llm-based']
    
    def __init__(self, dir): 
        ...

    @staticmethod
    def load_document(dir):
        try: 
            with open(dir, 'rb') as file:  # Open in binary mode for PDFs
                reader = pypdf.PdfReader(file)
                text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
            return text
        
        except FileNotFoundError:
            print(f"File not found at the specified path: {dir}")
            return ""
        
        except pypdf.errors.PdfReadError:
            print(f"Error reading the PDF file at: {dir}. It may be corrupted or encrypted.")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred while extracting text: {e}")
            return ""