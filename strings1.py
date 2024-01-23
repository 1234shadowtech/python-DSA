class string1:
    def __init__(self):
        self.a="enter the first string "
        self.b=''
    def string_slicing(self):
        
        c=int(input("enter the index of the letter to be removed"))
        d=self.a[:c]+self.a[c+1:] #here a[:c]=represents the letters before the index except the letter in the index +(added with)a[c+1:]which consists of all the letters after the indexed letter
        print(d)
    def remove_word(self):
        e=str(input("enter the word to remove"))
        f=self.a.replace(e,"")#replace is a built in function the is used to replace or remove a word from the string
        print(f)
    
    # simmilarly
    #words = original_string.split() // the sting is split into words using built in funtion split()
    #filtered_words = [word for word in words if word != word_to_remove] //works as a filter loop and filters out the given word
    #new_string = ' '.join(filtered_words) // join function is a built in functon which is used to join words into a string
    #print(new_string)
    
    def word_search(self):
        g=str(input("enter the word that needs to be searched "))
        if g in self.a:
            print("the word is present ")
        else:
            print("the word is not present")
    # using find() function
    #my_string = "Hello, World!"
     #m = my_string.find("World")
    #if m != -1:
    #print(f"Found at index {m}!")
    #else:
    #print("Not found.")

    # similarly using .index()function
    #my_string = "Hello, World!"
    #try:
    #index = my_string.index("World")
    #print(f"Found at index {index}!")
    #except ValueError:
    #print("Not found.")
