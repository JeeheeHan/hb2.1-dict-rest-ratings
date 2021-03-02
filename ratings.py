"""Restaurant rating lister."""
def list_rest_rating(file):
    file_opened = open(file)
    ratings_dic = {}
    for line in file_opened:
        #restaurant = line.rsplit(":")

        name, rating = line.rsplit(":")
        rating_dic[name] = int(rating)

    print(rating_dic)
    




