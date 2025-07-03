import pandas as pd
from rapidfuzz import process, fuzz
import re

class AdmissionChatbot:
    def __init__(self, excel_path):
        self.knowledge_base = []
        self.greeting_response = (
            "🌟 Greetings, future scholar! I'm KeplerBot Genie, your magical study companion! ✨ "
            "Rub my lamp (ask me anything) and I'll grant you wisdom about Kepler College! 🧙‍♂️💫"
        )

        # Load all relevant sheets including Draft
        sheets = ["Draft", "Admission and Registration", "Admission & Registration 2", "Programs", "Orientation"]
        df_dict = pd.read_excel(excel_path, sheet_name=sheets)

        for sheet, df in df_dict.items():
            df.columns = df.columns.str.strip().str.lower()
            question_col = None
            answer_col = None

            # Auto-detect question and answer columns
            for col in df.columns:
                if 'question' in col:
                    question_col = col
                elif 'answer' in col:
                    answer_col = col

            if question_col and answer_col:
                for _, row in df.iterrows():
                    question = str(row[question_col]).strip()
                    answer = str(row[answer_col]).strip()

                    if question.lower() != "nan" and answer.lower() != "nan":
                        self.knowledge_base.append((question.lower(), answer))

        print(f"✅ Loaded {len(self.knowledge_base)} QA pairs from all sheets")

    def get_response(self, user_input):
        if not user_input.strip():
            return "Please ask a question."

        # Handle gratitude first — before any matching
        if self.handle_gratitude(user_input):
            return "🤗 You're welcome! Happy to assist you any time!"

        user_input_clean = user_input.lower().strip()

        # Greeting detection
        if user_input_clean in ["hi", "hello", "hey"]:
            return self.greeting_response

        # Special case: About Kepler
        if ("kepler" in user_input_clean and 
            ("about" in user_input_clean or "what is" in user_input_clean or "describe" in user_input_clean)):
            for q, a in self.knowledge_base:
                if "tell me about kepler" in q:
                    return a

        # General question matching
        matches = process.extract(
            user_input_clean,
            [q[0] for q in self.knowledge_base],
            scorer=fuzz.token_sort_ratio,
            limit=3
        )

        if matches:
            best_match = matches[0]
            if best_match[1] > 65:
                return self.knowledge_base[best_match[2]][1]

        return (
            "🔑 I'm sorry, I couldn't find an answer to that. Please check Kepler College's website "
            "or contact admissions@keplercollege.ac.rw."
        )

    def handle_gratitude(self, user_input):
        user_input = user_input.lower()
        gratitude_keywords = ["thank you", "thanks", "thank", "grateful", "appreciate"]
        for keyword in gratitude_keywords:
            if keyword in user_input:
                print(f"🔍 Detected gratitude: matched '{keyword}' in '{user_input}'")  # Optional debug log
                return True
        return False
