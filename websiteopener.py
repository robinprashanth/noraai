import config
import webbrowser

# import and configure OpenAI
import openai
openai.api_key = config.OPENAI_API_KEY

# import and configure asyncio package
import asyncio
import nest_asyncio
nest_asyncio.apply()

last_occurrence = -1

async def check_transcript():
    global last_occurrence

    with open('transcriptions/transcript.txt') as f:
        text = f.read()
        occurrence = text.lower().rfind(config.COMMAND_WORD)
        if occurrence != last_occurrence:
            print(f"Found new {config.COMMAND_WORD} at {occurrence}")

            # get command starting at occurrence of command word
            command = text[occurrence:]
            print(command)

            # store last occurrence so we don't repeat the same command
            last_occurrence = occurrence

            prompt = f"""{config.PROMPT_INSTRUCTIONS}
            {command}
            """

            print(prompt)

            engine = 'text-davinci-003'

            response = openai.Completion.create(
                engine=engine, 
                prompt=prompt,
                temperature=0.3,
                max_tokens=140,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=1
            )

            try:
                print(response['choices'][0]['text'].strip())
                webbrowser.open(response['choices'][0]['text'].strip())
            except Exception as e:
                print(f"error parsing response from OpenAI {e}")
                return

async def run_periodically(interval, periodic_function):
    while True:
        await asyncio.gather(asyncio.sleep(interval), periodic_function())

asyncio.run(run_periodically(1, check_transcript))