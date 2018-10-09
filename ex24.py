print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
  \tThe lovely world
  with logic so firmly planted
  cannot discern \n the needs of love
  nor comprehend passion from intuition
  and requires an explanation
  \n\t\twhere there is none.
  """

print("--------")
print(poem)
print("--------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
      jelly_beans = started * 500
      jars = jelly_beans / 1000
      crates = jars / 100
      return jelly_beans, jars, crates


start_point = 1000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


print("Now to practice with my work schedule and payment per week.")
chad = 65 * 3
jacinda = 65
raina = 65 * 2
jrs = 25 * 12
syd = 65

payment = chad + jacinda + raina + jrs + syd
print("\tThis is the gross amount that I earn from my private lessons and juniors.")
print("===>", payment)

print("This is the payment after the percentage is taken out.")
actual_pmt = payment * .65
print("\t====>", actual_pmt)
lost_pmt = payment - actual_pmt
print(f"This is the amount I lost from the percentage taken out: {lost_pmt}")
print("Country Club's really get you with what they take out. \n:-(")
