import json
from openai import OpenAI

client = OpenAI() # global client object as re-initializations are not needed:

def call_model(prompt, config, expected_keywords=None):
    """
        Simple abstraction to call the model.

        make sure you set the OPENAI_API_KEY in the environment. The OpenAI module
        automatically searches the environment variable and sets the authentication key.
    """
    res = {}
    tries = 0

    while tries < config["max_retries"]:
        tries += 1
        try:
            response = client.chat.completions.create(
                model=config["model_name"],
                messages=[
                    {"role": "system", "content": prompt},
                ],
                temperature=config["temperature"]
            )

            res = json.loads(response.choices[0].message.content)

            break_flag = True
            for keyword in expected_keywords:
                if keyword not in res:
                    break_flag = False
            
            if break_flag:
                break
        except Exception as e:
            print("Error encountered in loading the json object ", e)

    return res

def main():
    config = json.load(open("llm_config.json"))
    call_model(open("./dataset/passage.txt", "r").read(), config)

if __name__ == "__main__":
    main()