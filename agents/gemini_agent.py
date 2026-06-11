import importlib
import importlib.util
import os

package_name = "google.generativeai"
if importlib.util.find_spec(package_name) is None:
    raise ImportError(
        "Package 'google.generativeai' not found. Install it with 'pip install google-generative-ai'"
    )
genai = importlib.import_module(package_name)

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_suggestions(summary):

    response = model.generate_content(
        summary
    )

    return response.text