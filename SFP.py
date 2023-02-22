from itertools import permutations

class ShortestFindPath:
    def __init__(self,str_list,list_distance):
        self.str_list = str_list
        self.list_distance = list_distance
        self.l_str = len(str_list)

    def find_shortest_path(self):
        min_dis = float('inf')
        min_path = None

        try:
            for path in permutations(range(1,self.l_str)):
                path = (0,) + path + (0,)
                dis = 0

                for i in range(self.l_str):
                    j = i + 1
                    dis += self.list_distance[path[i]][path[j]]

                if dis < min_dis:
                    min_dis = dis
                    min_path = path
        except Exception as E:
            print("Logic is not working please check it...", E)

        min_path = [self.str_list[i] for i in min_path]
        print("Shortest Distance is:", min_dis)
        print("Shortest Path is", "-".join(min_path))
        return min_path,min_dis


if __name__ == "__main__":
    cities_no = int(input("Enter number of cities:"))
    str_list = list(str(string) for string in input("Enter the list items separated by space:").strip().split())[:cities_no]
    print(str_list)
    list_size = int(input("Enter the number of sub list:"))
    list_distance = [[int(input("Enter single number and press enter: ")) for _ in range(list_size)] for _ in range(list_size)]
    print(list_distance)
    try:
        s = ShortestFindPath(str_list,list_distance)
        s.find_shortest_path()
    except Exception as e:
        print("Program is not working.", e)