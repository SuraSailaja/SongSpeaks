import os

import base64

import streamlit as st

from dotenv import load_dotenv

from sarvamai import SarvamAI



load_dotenv()



st.set_page_config(page_title="SongSpeak AI", page_icon="🎵")



st.title("🎵 SongSpeak AI")

st.write("Learn English through music with your voice tutor.")



api_key = os.getenv("SARVAM_API_KEY")



if not api_key:

    st.error("API key missing. Check your .env file.")

    st.stop()



client = SarvamAI(api_subscription_key=api_key)



SYSTEM_PROMPT = """

You are SongSpeak, a friendly English tutor.

Teach vocabulary, grammar, idioms and natural expressions.

Use short explanations and ask one practice question at a time.

Use original examples and do not reproduce substantial song lyrics.

"""



if "messages" not in st.session_state:

    st.session_state.messages = [{

        "role": "assistant",

        "content": (

            "Hi! Welcome to SongSpeak! 🎵 "

            "Ask me about English or use the microphone below "

            "to speak to your tutor."

        )

    }]



st.subheader("🎙️ Speak to your tutor")

st.write("Click the microphone, record your question, then submit it.")



if "voice_widget_id" not in st.session_state:
    st.session_state.voice_widget_id = 0

recording = st.audio_input(
    "Record your voice",
    key=f"voice_input_{st.session_state.voice_widget_id}"
)

if recording is not None:
    st.audio(recording, format="audio/wav")

if st.button("🗣️ Transcribe and ask tutor", key="submit_voice"):
    if recording is None:
        st.warning("Please record your question using the microphone above.")
    else:
        try:
            with st.spinner("Listening to your English..."):
                result = client.speech_to_text.transcribe(
                    file=("recording.wav", recording.getvalue(), "audio/wav"),
                    model="saaras:v4",
                    language_code="en-IN",
                    mode="transcribe"
                )
            transcript = result.transcript.strip()
            if transcript:
                st.session_state.pending_message = transcript
                st.session_state.voice_widget_id += 1
                st.rerun()
            else:
                st.warning("I couldn't recognize your speech. Please record again.")
        except Exception as e:
            st.error(f"Speech recognition failed: {e}")

typed_message = st.chat_input("Or type your question here...")

voice_message = st.session_state.pop("pending_message", None)

prompt = typed_message or voice_message



for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])



if prompt:

    st.session_state.messages.append(

        {"role": "user", "content": prompt}

    )



    with st.chat_message("user"):

        st.markdown(prompt)



    with st.chat_message("assistant"):

        try:

            messages = [

                {"role": "system", "content": SYSTEM_PROMPT}

            ] + st.session_state.messages[-8:]



            with st.spinner("Your tutor is thinking..."):

                response = client.chat.completions(

                    model="sarvam-105b",

                    messages=messages,

                    reasoning_effort=None,

                    max_tokens=500,

                )



            answer = response.choices[0].message.content



            if not isinstance(answer, str) or not answer.strip():

                st.error("The model returned no text. Please try again.")

            else:

                st.markdown(answer)

                st.session_state.messages.append({

                    "role": "assistant",

                    "content": answer,

                })



                try:

                    with st.spinner("Generating spoken response..."):

                        speech = client.text_to_speech.convert(

                            text=answer[:1500],

                            model="bulbul:v3",

                            speaker="shubh",

                            language_code="en-IN",

                        )



                    if speech.audios:

                        audio_bytes = base64.b64decode(speech.audios[0])

                        st.audio(audio_bytes, format="audio/wav")



                except Exception as e:

                    st.warning(

                        "Text works, but voice output failed: "

                        f"{type(e).__name__}: {e}"

                    )



        except Exception as e:

            st.error(f"Tutor error: {type(e).__name__}: {e}")



st.divider()

st.caption("Built for the Sarvam AI Hackathon 🚀")



