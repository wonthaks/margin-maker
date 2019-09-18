import margin_maker



def CalculateMarginTest():

  expected = 18

  test_margin = 3

  test_point_size = 12

  result = margin_maker.CalculateMargin(test_margin, test_point_size)

  assert (expected == result)



def _CheckWordTestTrues():

  test_word_one = "a."

  test_word_two = "a?"

  test_word_three = "a!"



  assert (margin_maker._CheckWord(test_word_one) == True)

  assert (margin_maker._CheckWord(test_word_two) == True)

  assert (margin_maker._CheckWord(test_word_three) == True)



def _CheckWordTestFalse():

  test_word = "a"

  assert (margin_maker._CheckWord(test_word) == False)



def RunTests():

  CalculateMarginTest()

  _CheckWordTestTrues()

  _CheckWordTestFalse
