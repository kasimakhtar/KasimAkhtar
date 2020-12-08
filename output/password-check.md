## Function to check if password is valid

This is a simple function that is designed for a [CodeWar challenge](https://www.codewars.com/kata/57e35f1bc763b8ccce000038) and checks whether a password is strong enough or not. It takes a string as an arguement and returns either "valid" or "not valid" depending on whether the password is or isn't in line with the following requirements:

* Is between 8-20 characters

* Is made up of only uppercase letters, lowercase letters, numbers, special characters (!@#$%^&*), and contains at least one of each of these categories

[CodeWars challenge](https://www.codewars.com/kata/57e35f1bc763b8ccce000038).
~~~

def check_password(s):
  special = ["!", "@", "$", "%", "^", "&", "*"]
  for i in special:
    if i in s:
      if any(char.isdigit() for char in s):
        if any(char.isupper() for char in s):
          if any(char.islower() for char in s):
            if len(s) >= 8 and len(s) <= 20:
              return "valid"
    else:
      return "not valid"

~~~


The idea for this function is a [CodeWars challenge](https://www.codewars.com/kata/57e35f1bc763b8ccce000038).

