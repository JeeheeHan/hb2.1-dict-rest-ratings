
def list_rest_rating(file):
    """Restaurant rating lister."""
    file_opened = open(file)
    ratings_dic = {} 

    for line in file_opened:    #Creates a rating_dic entry for each line in opened_file
        name, rating = line.rsplit(":")
        ratings_dic[name] = int(rating)
    
    file_opened.close()

    return ratings_dic

def sort_rating_dic(diction):
    
    for name, num in sorted(diction.items()):
        print(f"{name} is rated at {num}")
        

def new_rating(another_diction):
    new_restaurant = input("What restaurant do you want to rate? ")
    n_rest_rating = int(input("What is the rating? " ))

    another_diction[new_restaurant] = n_rest_rating
    return another_diction


result = list_rest_rating("scores.txt")

sort_rating_dic(result)

new_rating(result)

sort_rating_dic(result)




    #Our first solution for everything in one function 
    # list_tuple = []
    # [list_tuple.append(tuples) for tuples in ratings_dic.items()] #Pull items from rating_dic with tuple impacting
    #     # list_tuple.append(tuples)
    
    # list_tuple.sort()


    # for items in list_tuple:  #Run through tuples in sorted list of tuples 
    #     print(f"{items[0]} is rated at {items[1]}")
    


        
    
    




