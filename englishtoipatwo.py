# imports
import eng_to_ipa


#input word
english_word = input("Type a word and press Enter... ")

# define word and convert
conversion = eng_to_ipa.convert(english_word)
 
# give output
  ## "\n" creates new blank line
  ## len( ) is for length of string
  ## "-" is for symbol that composes dividing line above output
print("\n" + len(conversion)*"-")
print(conversion)



