import json

# data = {
#     "responses": {
#         "life_story": "I have always been driven by curiosity and problem-solving. My background combines engineering and AI research, and I’ve worked on projects that challenge me to learn and adapt. I enjoy building practical solutions, whether it's through automation, AI, or optimizing workflows. Outside of work, I value continuous learning and personal growth.",
#         "superpower": "My ability to break down complex problems into structured, actionable steps. Whether it’s analyzing data, troubleshooting technical issues, or improving processes, I focus on clarity, efficiency, and results.",
#         "growth_areas": [
#             "Deepening my expertise in AI and machine learning, especially in real-world applications.",
#             "Enhancing my leadership and mentorship skills to guide teams effectively.",
#             "Improving my ability to communicate technical concepts in a way that is accessible to non-technical stakeholders."
#         ],
#         "misconception": "Some might assume that I am always focused on technical details and don’t engage much in broader strategic discussions. In reality, I enjoy collaborating on high-level problem-solving and aligning solutions with business goals.",
#         "pushing_boundaries": "I seek out challenging projects that force me to learn new skills and think differently. I actively explore new technologies, take on responsibilities outside my comfort zone, and continuously refine my approach based on feedback."
       
#     }
# }

data = {
    "responses": {
        "life_story": "I have always been driven by curiosity and problem-solving. My background combines engineering and AI research, and I’ve worked on projects that challenge me to learn and adapt. I enjoy building practical solutions, whether it's through automation, AI, or optimizing workflows. Outside of work, I value continuous learning and personal growth.",
        "superpower": "My ability to break down complex problems into structured, actionable steps. Whether it’s analyzing data, troubleshooting technical issues, or improving processes, I focus on clarity, efficiency, and results.",
        "growth_areas": [
            "Deepening my expertise in AI and machine learning, especially in real-world applications.",
            "Enhancing my leadership and mentorship skills to guide teams effectively.",
            "Improving my ability to communicate technical concepts in a way that is accessible to non-technical stakeholders."
        ],
        "misconception": "Some might assume that I am always focused on technical details and don’t engage much in broader strategic discussions. In reality, I enjoy collaborating on high-level problem-solving and aligning solutions with business goals.",
        "pushing_boundaries": "I seek out challenging projects that force me to learn new skills and think differently. I actively explore new technologies, take on responsibilities outside my comfort zone, and continuously refine my approach based on feedback.",
        "experience": {
            "Vbuild Tech: AI Intern (11/24 - Present)": [
                "Developing automated document comparison solutions using Vision-Language Models (VLM).",
                "Implementing a Tamil Speech-to-Text (STT) model for Raspberry Pi.",
                "Building an invoice information extraction application.",
                "Technologies Used: VLM, LLM, Cloud Computing (E2E Network), DeepSpeech, Coqui STT, Whisper."
            ],
            "Siam Computing: Machine Learning Intern (10/23 - 03/24, Chennai)": [
                "Designed and implemented a Conversational AI Chatbot using RASA.",
                "Developed Generative AI solutions, including an automated meme generation app and a healthcare assistant chatbot powered by OpenAI.",
                "Created an information extraction application for structured data processing.",
                "Technologies Used: Stable Diffusion, Replicate, ComfyUI, RASA, RAG, VLM, LLM."
            ]
        },
        "skills": {
            "Technical Stack": [
                "Data Science", "Machine Learning", "Deep Learning", "NLP", "Image Processing",
                "Generative AI", "LLMs", "RAG", "AI Agents", "MLops"
            ],
            "Programming Languages": ["Python (OOPs)", "Java", "HTML", "C++"],
            "Databases": ["MySQL", "MongoDB"],
            "Python Packages & Frameworks": [
                "Scikit-learn", "TensorFlow", "Keras", "Pandas", "Numpy", "Matplotlib",
                "Seaborn", "OpenCV", "Streamlit", "Heroku", "Flask", "FastAPI",
                "OpenAI", "LangChain", "LlamaIndex", "PyTorch"
            ],
            "API Development": ["REST API (FastAPI)"],
            "Cloud Platform": ["E2E Network"]
        }
    }
}

with open('profile.json', 'w') as f:
    json.dump(data, f)

import json
import os
from langchain_groq import ChatGroq
from gtts import gTTS

from dotenv import load_dotenv
load_dotenv()


# Load profile data from JSON file
with open('profile.json') as f:
    data = json.load(f)


llm = ChatGroq(
    model='llama-3.1-8b-instant',
    
    verbose=True,
    max_tokens=None
)

# Text-to-Speech Function
def text_to_speech(text, filename="response.mp3"):
    """Converts text to speech using gTTS and saves to an audio file."""
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    
    return filename

# Get user input
user_input = input("Enter your question: ")

# Define messages
messages = [
    (
        "system",
        f"You are  SIBANI NAYAK. When an interviewer asks about SIBANI NAYAK, read the following biopic data and answer professionally: {data}"
    ),
    ("human", user_input),
]

# Get response from LLM
response = llm.invoke(messages)
response_text = response.content
print(response_text)

#Convert response to speech
audio_file = text_to_speech(response_text)

# Play the audio
playsound.playsound(audio_file)

# Remove the audio file
os.remove(audio_file)