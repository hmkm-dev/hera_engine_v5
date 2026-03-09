from ai_script_writer import generate_script
from voice_generator import generate_voice
from timing_engine import get_word_times
from renderer import render

script = generate_script()
audio_path = generate_voice(script)

words = get_word_times(audio_path)

render(words, audio_path)