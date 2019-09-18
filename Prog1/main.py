import margin_maker

import margin_maker_test



def main(): 

  margin_maker_test.RunTests()

  with open("output.txt", 'w+') as output_file:

    with open("DAT1.txt", 'r') as input_file:

      margins_and_size = input_file.readline().split()



      right_margin = margin_maker.CalculateMargin(int(margins_and_size[0]), int(margins_and_size[2]))

      left_margin = margin_maker.CalculateMargin(int(margins_and_size[1]), int(margins_and_size[2]))

      char_count = 0

      char_limit = 80 - right_margin - left_margin



      for num_char in range(left_margin):

        print(' ', end='')

        output_file.write(' ')

      for line in input_file:

        char_count = margin_maker.HandleLine(line.split(), char_count, char_limit, left_margin, output_file)

        if (char_count == -1):

          return

        if (len(line) < 80):

          if (line.endswith('.\n') or line.endswith('.')):

            char_count = 0

            print()

            output_file.write('\n')

            for num_char in range(left_margin):

              print(' ', end='')

              output_file.write(' ')

      print()

      output_file.write('\n')



main()
