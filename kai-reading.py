import streamlit as st
import random

red_words = ["and", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other", "about", "out", "many", "then", "them", "these", "so", "some", "her", "would", "make", "like", "him", "into", "time", "has", "look", "two", "more", "write", "go", "see", "number", "no", "way", "could", "people", "my", "than", "first", "water", "been", "call", "who", "oil", "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part", "over", "new", "sound", "take", "only", "little", "work", "know", "place", "year", "live", "me", "back", "give", "most", "very", "after", "thing", "our", "just", "name", "good", "sentence", "man", "think", "say", "great", "where", "help", "through", "much", "before", "line", "right", "too", "mean", "old", "any", "same", "tell", "boy", "follow", "came", "want", "show", "also", "around", "form", "three", "small", "set", "put", "end", "does", "another", "well", "large", "must", "big", "even", "such", "because", "turn", "here", "why", "ask", "went", "men", "read", "need", "land", "different", "home", "us", "move", "try", "kind", "hand", "picture", "again", "change", "off", "play", "spell", "air", "away", "animal", "house", "point", "page", "letter", "mother", "answer", "found", "study", "still", "learn", "should", "America", "world"]
green_words = ["cat", "dog", "pig", "hen", "fox", "bus", "red", "sun", "bed", "top", "pan", "pin", "hat", "rat", "mat", "fan", "van", "can", "map", "cap", "tap", "nap", "sad", "sit", "sip", "tip", "tin", "bin", "fin", "win", "hit", "bit", "fit", "kit", "six", "mix", "fix", "box", "tax", "wax", "yes", "yet", "web", "wet", "jet", "jog", "jam", "jug", "jut", "zip", "zig", "zap", "quiz", "quit", "quick", "quack", "queen", "quilt", "quill", "quiz", "quit", "quick", "quack", "queen", "quilt", "quill", "ship", "shop", "shed", "shell", "fish", "wish", "dish", "trash", "bash", "rash", "mash", "chop", "chin", "chip", "chill", "check", "cheese", "them", "then", "this", "that", "with", "math", "path", "bath", "king", "ring", "sing", "wing", "long", "song", "hung", "lung", "rung"]

comprehension_questions = [
    {
        "passage": "The cat sat on the mat. The dog ran to the cat. The cat and the dog played together.",
        "question": "What did the cat sit on?",
        "options": ["The mat", "The dog", "The chair"],
        "answer": "The mat"
    },
    {
        "passage": "The boy kicked the ball. The ball rolled into the goal. The boy scored a point.",
        "question": "Where did the ball go?",
        "options": ["Into the goal", "Under the chair", "Over the fence"],
        "answer": "Into the goal"
    },
    {
        "passage": "The girl drew a picture. She used red and blue crayons. The picture was of a flower.",
        "question": "What did the picture show?",
        "options": ["A flower", "A sun", "A cat"],
        "answer": "A flower"
    },
    {
        "passage": "The bird flew high in the sky. It landed on a branch. The bird sang a song.",
        "question": "What did the bird do in the sky?",
        "options": ["Flew", "Swam", "Danced"],
        "answer": "Flew"
    },
    {
        "passage": "The boy had a toy car. He pushed the car across the floor. The car was red and fast.",
        "question": "What did the boy do with the car?",
        "options": ["Pushed it", "Pulled it", "Threw it"],
        "answer": "Pushed it"
    },
    {
        "passage": "The girl saw a butterfly. The butterfly had colorful wings. It flew from flower to flower.",
        "question": "What had colorful wings?",
        "options": ["The butterfly", "The bird", "The flower"],
        "answer": "The butterfly"
    },
    {
        "passage": "The dog had a bone. He buried the bone in the yard. Later, he dug it up and chewed on it.",
        "question": "What did the dog do with the bone first?",
        "options": ["Buried it", "Ate it", "Threw it"],
        "answer": "Buried it"
    },
    {
        "passage": "The cat chased a mouse. The mouse ran into a hole. The cat waited by the hole.",
        "question": "Who ran into a hole?",
        "options": ["The cat", "The mouse", "The dog"],
        "answer": "The mouse"
    },
    {
        "passage": "The boy rode his bike. He pedaled fast down the hill. The wind blew through his hair.",
        "question": "What did the boy ride?",
        "options": ["A bike", "A horse", "A skateboard"],
        "answer": "A bike"
    },
    {
        "passage": "The girl played with her doll. She brushed the doll's hair. Then, she put the doll to bed.",
        "question": "What did the girl play with?",
        "options": ["A doll", "A ball", "A puzzle"],
        "answer": "A doll"
    }
]

def set_page_config():
    st.set_page_config(page_title="Reading Practice", page_icon=":books:", layout="wide")

def display_header(title):
    st.title(title)

def set_css_style():
    st.markdown(
        """
        <style>
            body { 
                background-color: #F0E6EF;
                font-family: 'Comic Sans MS', cursive;
            }
            .stButton button { 
                background-color: #4CAF50;
                color: white;
                padding: 10px 24px;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
            }
            .stButton button:hover { 
                background-color: #45a049;
            }
            .word_display { 
                font-size: 48px;
                font-weight: bold;
                margin: 20px 0;
            }
            .passage_text { 
                font-size: 38px; 
            }
            .question_prompt { 
                font-size: 38px; 
                font-weight: bold;
            }
            .stRadio > label {
                font-size: 24px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def initialize_session_state():
    if "gold_coins" not in st.session_state:
        st.session_state.gold_coins = 0
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "show_balloons" not in st.session_state:
        st.session_state.show_balloons = False
    if "shuffled_questions" not in st.session_state:
        random.shuffle(comprehension_questions)  
        st.session_state.shuffled_questions = comprehension_questions

def display_gold_coins():
    st.sidebar.header("Rewards")
    coin_image = "media/goldcoin2.png"
    st.sidebar.image(coin_image, width=50, use_column_width=False, output_format='PNG')
    st.sidebar.write(f"Gold Coins: {st.session_state.gold_coins}")
    if st.session_state.show_balloons:
        st.balloons()
        st.session_state.show_balloons = False

def handle_error(e):
    st.error(f"An error occurred: {e}")
    st.stop()

def main():
    try:
        set_page_config()
        display_header("Reading Practice for Kai")
        set_css_style()
        initialize_session_state()

        tab1, tab2, tab3 = st.tabs(["Red Words", "Phonics Practice", "Understanding"])

        with tab1:
            # Red word recognition exercise
            red_word = random.choice(red_words)
            st.markdown(f"<div class='word_display'>{red_word}</div>", unsafe_allow_html=True)
            if st.button("Next", key="red_word_button"):
                st.session_state.gold_coins += 1
                st.session_state.show_balloons = True  # Set the flag to show balloons
                st.experimental_rerun()

        with tab2:
            # Green practice exercise
            green_word = random.choice(green_words)
            st.markdown(f"<div class='word_display'>{green_word}</div>", unsafe_allow_html=True)
            if st.button("Next", key="green_word_button"):
                st.session_state.gold_coins += 1
                st.session_state.show_balloons = True  # Set the flag to show balloons
                st.experimental_rerun()

        with tab3:
            # Reading comprehension exercise
            question = st.session_state.shuffled_questions[st.session_state.question_index]
            st.markdown(f"<div class='passage_text'>{question['passage']}</div>", unsafe_allow_html=True)
            st.divider()
            st.markdown(f"<div class='question_prompt'>{question['question']}</div>", unsafe_allow_html=True)
            answer = st.radio("", question["options"], key="comprehension_answer", index=None, label_visibility="visible")
            if st.button("Submit Answer", key="comprehension_submit"):
                if answer == question["answer"]:
                    st.session_state.gold_coins += 1
                    st.session_state.question_index = (st.session_state.question_index + 1) % len(st.session_state.shuffled_questions)
                    st.session_state.show_balloons = True  # Set the flag to show balloons only for correct answers
                else:
                    st.error("Incorrect answer. Try again!")
                st.experimental_rerun()

        display_gold_coins()

    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()