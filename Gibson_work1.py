# Question 6
# Write a function second_largest(lst) that finds the second largest number in a list without using sorted().

def is_second_largest(n):
    for passes in range(len(n)-1):
        for i in range(len(n)-1-passes):
            if n[i] < n[i+1]:
                n[i+1], n[i] = n[i], n[i+1]
    return n[1]

try:
    n = []
    while True:
        user_input = input("Enter number (press enter to stop): ")
        if user_input == "":
            break
        n.append(int(user_input))

    if len(n) < 2:
        print("Must be at least 2 numbers")
    else:
        print("Second largest:", is_second_largest(n))

except ValueError:
    print("Please enter a number")



# Question 2
# Given a list of numbers, do the following using list comprehensions and built-in functions:
# ● Double each number
# ● Keep only even numbers
# ● Find the sum of the remaining numbers

def processed_list(n):
    total=0
    new_list=[]
    for numbers in n:
        if numbers%2==0:
            new_list.append(numbers)
            numbers*2
            total+=numbers
    return total
                      

   
n=[]
while True:    
    user_input=input("Enter numbers: (press enter to stop)")
    if user_input=="":
        break
    n.append(int(user_input))
print(f"Processed list {processed_list(n)}")

#Question 1
# Write a function capitalize_words(sentence) that takes a string and capitalizes the first letter of each word.
def capitalize_word(n):    
    return n.capitalize()
user_input=input("Enter a sentence: " )
print(f"Capitalized version-{capitalize_word(user_input)}")

#Question 7
# Write a function apply_operation(lst, operation) where operation can be "square", "double", or "negate", and apply it to every element of the list.
def apply_operation(numbers, operation):
        result=[]    
        for number in numbers:
            if operation=='square':
                result.append(number**2)
            elif operation=='double':
                result.append(number*2)
            elif operation=='negate':
                result.append(-number)
            else:
                print("Error, try again")
        return result
try:   
    while True:
        nums=[]
        user_input=input("Enter a number (Press enter to stop): ")
        if user_input=="":
            break
        nums.append(int(user_input))

        op=input("Enter operation (square, double, negate): ")
        result=apply_operation(nums,op)
        print(f"Result={result}")

        
except ValueError:
    print("Please enter an operation!!")    

#Question 4
# Write a function get_affordable_products(products, budget) that returns all products with a price less than or equal to budget.
#This one seems easy all I have to do is iterate through a list and check whether it matches a user's input
def get_affordable_products(products,budget):
    chosen_products=[]
    for item in products:
        #ok I underestimated this
        #how do I refer to things in a dictionary
        if item['price'] <=budget:
            chosen_products.append(item)

    return chosen_products

try:
    while True:
        products = [
{"name": "Laptop", "price": 1200},
{"name": "Phone", "price": 800},
{"name": "Tablet", "price": 600}
]
        

        user_budget=int(input("Enter your budget: "))
        affordable=get_affordable_products(products,user_budget)
        if affordable:#Let's print what they can afford       
            for p in affordable:            
                print(f"{p['name']} -${p['price']}")
        else:
            print("No products within your budget")

except ValueError:
    print("Error-invalid number for budget entered!!")


#Question 9
# Write a function get_user_city(user) that safely returns a user’s city. If the city is missing, return "Unknown".
#kinda like the shopping list thing, looping through dictioneries
#o..k it's nothing like that,this time it's a single list
def get_user_city(user):    
       return user.get("city","unknown")


#Question 3
# Write a function that extracts username, email, and theme and prints them.
#just like Q9
def get_user_details(username,email,theme):
    return {"username": username,"email":email,"theme":theme}


#Question 5
# Write a function merge_lists(*lists) that accepts multiple lists and merges them into a single unique list (no duplicates).
def merge_lists():
    user_list=[] 
    while True:              
        user_response=input("Enter numbers separated by commas(press enter to stop): ")
        if user_response=="":
            break
        #what now??!!, I'm suppossed to separate them,
        numbers=[x.strip() for x in user_response.split(",")]
        user_list.extend(numbers)#appending doesn't seem to work here

    merged=list(set(user_list))
    return merged
print(f"Merged list: {merge_lists()}")
 
#Question 8
#Write a function group_by_category(items) that groups a list of dictionaries by a category key.
def group_by_category(items):
    #arrays are different from dictionaries
    grouped={}
    for item in items:
        category=item.get("category")
        if category not in grouped:#kinda like the grocery question
            grouped[category]=[]
        grouped[category].append(item)
    return grouped


#Question 10
#Write an async function fetch_posts() that fetches posts from https://jsonplaceholder.typicode.com/posts 
# using aiohttp or httpx and prints the titles of the first 5 posts.
#wtf is this??!!,beyond my current capabilities
import aiohttp
import asyncio

async def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            posts = await response.json()
            for post in posts[:5]:
                print(post["title"])


if __name__ == "__main__":
    asyncio.run(fetch_posts())





        




