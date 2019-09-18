#  Returns the margin to be used in "character"

#  length. 1 point = 1/72 inch

def CalculateMargin(inch_margin, point_size):

  return inch_margin * (72 // point_size)



#  Checks whether the word is at the end of a 

#  sentence or not.

def _CheckWord(word):

  if (word.endswith('.') or word.endswith('?') or word.endswith('!')):

    return True

  else:

    return False



#  Handles outputting the line (that is taken 

#  in as a list of split words). Returns the 

#  char counter. 

def HandleLine(line, char_count, char_limit, left_margin, output_file):

  for word in line:

    if (len(word) > char_limit):

      print("ERROR: WORD LENGTH MORE THAN MARGIN DEFINED.")

      return -1

    if (char_count + len(word) > char_limit):

      print()

      output_file.write('\n')

      for num_char in range(left_margin):

        print(' ', end='')

        output_file.write(' ')

      print(word, end='')

      output_file.write(word)

      print(' ', end='')

      output_file.write(' ')

      char_count = len(word) + 1

    else:

      print(word, end='')

      output_file.write(word)

      char_count += len(word)

      if (char_count + 1 > char_limit):

        print()

        output_file.write('\n')

        for num_char in range(left_margin):

          print(' ', end='')

          output_file.write(' ')

        print(' ', end='')

        output_file.write(' ')

        char_count = 1

      else:

        print(' ', end='')

        output_file.write(' ')

        char_count += 1

    if (_CheckWord(word)):

      print(' ', end='')

      output_file.write(' ')

      char_count += 1

  return char_count
