import requests
def format(category,name):
    formatted_name=name.lower().replace(" ","-")
    return formatted_name

def spacer():
    print("---------------------------------")

def catogorys_List():
    categories = ["Monsters", "Spells", "Classes", "Races", "Items", "Backgrounds"]
    for number, category in enumerate(categories, start=1):
        print(f"{number}.{category}")

    
        

print("Welcome to the Dnd Encylopedia")
spacer()
while True:
    print("Please Select a category from the following list:")
    catogorys_List()
    caogroyinput=input()
    if caogroyinput=="1":
             category="monsters"
             break
     
    elif caogroyinput=="2":
             category="spells"
             break
     
    elif caogroyinput=="3":
             category="classes"
             break
     
    elif caogroyinput=="4":
             category="races"
             break
    elif caogroyinput=="5":
             category="items"
             break
    elif caogroyinput=="6":
             category="backgrounds"
             break
    else:
          print("Invalid option, please try again") 


print(f"You have selected {category}")
print("Please enter the name of the item you would like to search for:")
name=input()
formatted_name=format(category,name)

response=requests.get(f"https://www.dnd5eapi.co/api/{category}/{formatted_name}")
if response.status_code==200:
    print("test passed")
    
      



