import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from prompts import build_review_prompt


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)


class AIReviewerError(Exception):
    """Raised when CodeMentor AI cannot generate a review."""


def review_solution(
    problem_statement: str,
    code: str,
    language: str,
    review_mode: str,
) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise AIReviewerError("GEMINI_API_KEY environment variable is not set.")

    api_key = api_key.strip()

    if api_key == "":
        raise AIReviewerError("GEMINI_API_KEY environment variable is empty.")

    prompt = build_review_prompt(
        problem_statement=problem_statement,
        code=code,
        language=language,
        review_mode=review_mode,
    )

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        review_text = response.text

        if not review_text or not review_text.strip():
            raise AIReviewerError("Gemini returned an empty response.")

        return review_text.strip()

    except AIReviewerError:
        raise
    except Exception as exc:
        raise AIReviewerError(f"Gemini request failed: {exc}") from exc