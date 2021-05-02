### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:# should read if card.value == 1:
      return True
    else # colon is missing here needs to read as else:
      return False
   

  dif highest_card(self, card1 card2):#dif should read def and card1, card2 (comma missing)
  #indentation of if statement needs to be moved inline.
  if card1.value > card2.value:#indentation is wrong
    return card # should read card1. indentation of return is wrong
  else:
    return card2 #indentation of return is wrong
  


def cards_total(self, cards):#indentation required
  total # should read total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # this should read "You have a total of #f{total}"
  
```
