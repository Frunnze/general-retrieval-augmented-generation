import requests

from .. import PROMPT_MANAGER_SERVICE_URL


def upload_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        files = {'file': (pdf_path, f, 'application/pdf')}
        res = requests.post(
            url=f"{PROMPT_MANAGER_SERVICE_URL}/add_material",
            files=files
        )
    return res