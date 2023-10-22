from transformers import LlamaForCausalLM, LlamaTokenizer

tokenizer = LlamaTokenizer.from_pretrained("decapoda-research/llama-7b-hf")
model = LlamaForCausalLM.from_pretrained("decapoda-research/llama-7b-hf")

MAX_TRIES = 3

def valid_response(response):
    return response in (1, 2, 3, 4, 5)

def rate_post(post_text):
    prompt = f"""Here is a social media post. It contains the following text: \"{post_text}\"
    On a scale of 1 to 5 (1 being the least positive and 5 being the most positive), how effective is this post at getting attention?
    (Please enter a number between 1 and 5)"""
    tries = 1
    response = respond(prompt)
    response = int("".join(char for char in response if char.isdigit()))

    while not valid_response(response):
        response = respond("Sorry, I didn't understand that. Please enter a number between 1 and 5.")
        response = int("".join(char for char in response if char.isdigit()))
        tries += 1
        if tries > MAX_TRIES:
            return -1

    return response

def rate_comment(comment_text):
    prompt = f"""Here is a comment from a social media post. It contains the following text: \"{comment_text}\"
    On a scale of 1 to 5 (1 being the least positive and 5 being the most positive), how positive is this comment?
    (Please enter a number between 1 and 5)"""
    tries = 1
    response = respond(prompt)
    response = int("".join(char for char in response if char.isdigit()))

    while not valid_response(response):
        response = respond("Sorry, I didn't understand that. Please enter a number between 1 and 5.")
        response = int("".join(char for char in response if char.isdigit()))
        tries += 1
        if tries > MAX_TRIES:
            return -1

    return response

def respond(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text