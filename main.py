import random
from datetime import datetime
from gtts import gTTS

topics = [
    "Black Hole ke andar kya hota hai?",
    "Human Brain ka 100% use kyun nahi hota?",
    "Sabse darawna psychological experiment",
    "AI duniya par kab control karega?",
    "Time travel possible hai ya nahi?",
    "Universe ka end kaise hoga?",
    "Top 5 ajeeb scientific facts",
    "Insaan sapne kyun dekhta hai?",
    "Dark web kya hota hai?",
    "Parallel universe sach hai?"
]

def generate_short_script(topic):
    return f"""
{topic}

Kya aapne kabhi socha hai?

Yeh sach jaan kar aap hairaan ho jayenge.

Science ke hisaab se iska jawab aapki soch se bhi zyada interesting hai.

Aise hi aur facts ke liye FactNexus Hub ko follow karein.
"""

def generate_long_script(topic):
    return f"""
Aaj hum baat karne wale hain: {topic}

Is topic ko samajhne ke liye hume thoda gehra jaana padega.

Science aur research ke mutabik, iske peeche bahut hi interesting theory hai.

Log iske baare me galat dharna rakhte hain, lekin asal sach kuch aur hai.

Is video me hum jaanenge:
- Iska scientific explanation
- Iska psychological impact
- Aur kya yeh future me possible ho sakta hai

Agar aapko aise deep facts pasand hain to channel ko subscribe zaroor karein.
"""

selected_topic = random.choice(topics)

short_script = generate_short_script(selected_topic)
long_script = generate_long_script(selected_topic)

today = datetime.now().strftime("%Y-%m-%d")

# Save scripts
with open(f"short_script_{today}.txt", "w", encoding="utf-8") as f:
    f.write(short_script)

with open(f"long_script_{today}.txt", "w", encoding="utf-8") as f:
    f.write(long_script)

# Generate Voice
short_tts = gTTS(short_script, lang='hi')
short_tts.save(f"short_voice_{today}.mp3")

long_tts = gTTS(long_script, lang='hi')
long_tts.save(f"long_voice_{today}.mp3")

print("Scripts and voice generated successfully 🚀")
