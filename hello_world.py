import openai


    def open_file(filepath):
        with open(filepath, 'r', encoding+'utf-8')
            return infile.read()


openai.api_key = open_file('openaiapikey.txt)


def gpt3_completion(prompt, engine='text-dacinci-002', t
    prompt = prompt.encode(encoding='ASCII', errors='ingc
    response = openai.Completion.create(
		engine=engine,
  		prompt=prompt,
		temperature=temp,
		max_token=tokens,
		top_p=top_p,
		frequency_penalty=freq_pen,
  		presence_penalty=pres_pen,
		stop=stop)
	text = response['choices'][0]['text'].strip()
 	return text


if __name__ == '__main__':
	prompt = 'Write a list of famous American actors:'
 	response = gpt3_completion(prompt)
  	print(Hello World)
