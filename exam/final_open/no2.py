def popularity_scores(dic: dict):
    count = 0
    return_dic = {}

    # convert dict to a list using list comprehension
    new_list = [(key, value) for (key, value) in dic.items()] # [("Python", 100), ("C++", 99.7), ...]
    # sort the list in reverse order according to the score
    new_list = sorted(new_list, key=lambda each: each[1], reverse=True)

    previous_score = None
    for i in range(len(new_list)):
        
        # if new_score -> create a new list at a new position with a new key (count)
        if previous_score != new_list[i][1]:
            count += 1
            return_dic[count] = list() 
            
        return_dic[count].append(new_list[i][0]) # append value to the list - e.g. "Python"

        previous_score = new_list[i][1]
    return return_dic

def main():
    dic = {"C++": 99.7, "C": 96.7, "Java": 97.5, "JavaScript": 97.5, "Python": 100, "C#": 89.4, "Rust": 89.4}
    print(popularity_scores(dic))

main()