import tiktoken
import PyPDF2


def load_file(path): 
    """
    extract each word in the file pdf and return and calc the tokens numbers
    """
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return "".join(page.extract_text() or "" for page in reader.pages)


text = load_file('meta_10k.pdf')
enc = tiktoken.encoding_for_model('gpt-4o')

print(len(enc.encode(text)))
