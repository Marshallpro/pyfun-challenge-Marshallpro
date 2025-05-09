def format_text (name:str,prefix:str ="",suffix :str ="",capitalize = False,max_length =None):
   
   '''Formats the the  input text by adding a prefix, suffix and optionally
     applying CAPITALISATION  and returning actual length of arguments'''
   
   if not isinstance(name,str):
      raise ValueError("The input must be a string.")
   
   if not isinstance(prefix, str) or not isinstance(suffix, str):
      raise ValueError("Prefix and suffix must be strings.")
   
   if not isinstance(capitalize,bool):
      raise TypeError("The 'capitalize' parameter must be a boolean.")
   
   if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' parameter must be an integer.")
        if max_length < 0:
            raise ValueError("max_length must be a non-negative integer.")



     # Applying formats
   formatted_text = f"{prefix} {name} {suffix}"
    
    # Capitalization
   if capitalize :
      formatted_text = formatted_text.capitalize()

    # Truncation
   if max_length is not None:
     formatted_text = formatted_text[:max_length]

   return(formatted_text) 

if __name__ == "__main__" :
   try :
      Name=input("enter your main string:  ")
      prefix=input("enter the prefix (optional) : ")
      suffix= input("enter suffix (optional) : ")
      cap_input = input("Capitalize the result? (yes/no): ").strip().lower()
      max_length=input("Enter max length (or leave blank): ").strip()


      capitalize = cap_input == "yes"
      max_length = int(max_length) if max_length else None

      result = format_text(Name, prefix=prefix, suffix=suffix, capitalize=capitalize, max_length=max_length)
      print("Formatted text:\n", result)


   except ValueError:
      raise ValueError("Unable to continue")   

