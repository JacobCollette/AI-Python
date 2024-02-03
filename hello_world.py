
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    prompt = 'Write a list of famous American actors:'
    response = gpt3_completion(prompt)
    print(response)
