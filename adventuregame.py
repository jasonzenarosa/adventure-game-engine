# adventure game

class Option:

    def __init__(self, option, next):
        self.option = option
        self.next = next

class Prompt:

    def __init__(self, prompt):
        self.prompt = prompt
        self.options = []

    def add_option(self, option, next=None):
        self.options.append(Option(option, next))

    def run(self):
        """Print prompt, options, and requests user input"""
        print(self.prompt + '\n')

        if len(self.options) > 0:

            print('Options:\n')
            print('\n'.join([f'{i + 1}: {j.option}' for (i, j) in enumerate(self.options)]) + '\n')
            choice = int(input('Select an option: ')) - 1
            print()
            return self.options[choice].next

        else:
            return None

def load_prompts(file):
    """room name: prompt text"""
    prompt_dict = {}
    for line in list(file):
        line = line.rstrip().split(':')
        prompt_dict[line[0]] = Prompt(line[1])
    return prompt_dict

def load_options(pd:dict, file):
    """start room: option text: end room"""
    for line in list(file):
        line = line.rstrip().split(':')
        start_room = pd[line[0]]
        option = line[1]
        try:
            end_room = pd[line[2]]
        except IndexError:
            end_room = None
        start_room.add_option(option, end_room)


if __name__ == '__main__':
    pd = load_prompts(open('prompts.txt'))
    load_options(pd, open('options.txt'))
    cur = pd['start']

    while cur is not None:
        cur = cur.run()
    print('GAME OVER')