path = 'make_me_a_video_game_template.txt'
# path = 'assets/dark_and_stormy_night.txt'

def read_template(path):
  try:
    with open(path) as file:
      string = file.read()
  except FileNotFoundError as error:
    print(error)

  return string

def parse_template(string):
  temp_list = []
  start_count = 0
  for character in string:
    start_count = start_count + 1
    if character == '{':
      end_count = string.find('}', start_count)
      substring = string[start_count:end_count]
      temp_list.append(substring)
      string = string.replace(substring, '', 1)
      start_count = start_count - len(substring)

  substrings = tuple(temp_list)
  return string, substrings

def merge(string, input_tuple):
  madlib = string.format(*input_tuple)
  return madlib

def write_madlib(string):
  with open('madlib.txt', 'w') as file:
    file.write(string)

def main():
  print("""
  Welcome to My Madlibs!

  You are about to be presented with a series of blanks to fill in. When you're done, we'll use them to tell you a short story.\n
  """)

  raw_template = read_template(path)
  stripped_template, input_terms = parse_template(raw_template)

  temp_list = []
  for term in input_terms:
    user_input = input(f'Give us... {term.lower()}: ')
    temp_list.append(user_input)

  input_data = tuple(temp_list)
  
  new_madlib = merge(stripped_template, input_data)
  print(f'Heres your story...\n{new_madlib}')

  write_madlib(new_madlib)

main()