"""
A few boolean expression puzzles to solve.
You can assume all numbers are integers.
Do not call any of these functions from this file... Do that from the main.py file.
"""

def is_sweltering():
  """
  This function asks the user for the current temperature (in Farenheit).
  It returns True if that temperature is very hot, False otherwise.
  Hot is defined as any temperature over 90 degrees Farenheit.

    :returns: True if the temperature is over 90, False otherwise.
  """
  temp = input("What is the temperature today? (F) ")
  hot = int(temp) > 90
  return hot

def is_warm():
  """
  This function asks the user for the current temperature (in Farenheit).
  It returns True if that temperature is very warm, False otherwise.
  Warm is defined as any temperature between 75 and 87 degrees Farenheit, inclusive.

    :returns: True if the temperature is between 75 and 87, inclusive, False otherwise.
  """
  temp = input("What is the temperature today? (F) ")
  temp = int(temp)
  warm = 75 <= temp <= 87
  return warm

def is_humid():
  """
  This function asks the user whether it is currently humid.
  We assume the user will answer either "yes" or "no".
  It returns True if so, False otherwise.

    :returns: True if it is humid today, False otherwise.
  """
  response = input("Is it humid today? ")
  humid = response == "yes"
  return humid

def is_inclement():
  """
  This function asks the user what the weather forecast is today.
  We allow the user to respond any way they want.
  If they respond with any of the following, we return True, otherwise we return False: "rain", "snow", "sleet"

    :returns: True if it is raining, snowing, or sleeting today, False otherwise.
  """
  response = input("What's the weather like today?")
  inclement = response == "rain" or response == "snow" or response == "sleet"
  return inclement

def is_typical_new_york_summer():
  """
  This function asks the user what the temperature is today and whether it is humid.
  If they respond that the temperature is above 90 degrees Farenheit and that it is humid, we return True, otherwise False.
  Requirements:
  - You must use the functions, is_sweltering() and is_humid() defined above to determine these two facts.
  - In other words, you cannot use the input function direclty in the code you write for this function.

    :returns: True if the temperature is over 90 and it is humid, False otherwise.
  """
  awful = is_sweltering() and is_humid()
  return awful

def is_cool_and_nice():
  """
  This function determines whether it is cool and nice today.  It does so by relying on other functions defined above.
  Requirements:
  - You must use the functions, is_sweltering(), is_warm(), is_humid(), and is_inclement defined above to determine whether it is cool and nice today.
  - The weather is considered cool if these functions all return False.

    :returns: True if the weather is cool and nice today, False otherwise.
  """
  good = not is_sweltering() and not is_humid()
  return good

