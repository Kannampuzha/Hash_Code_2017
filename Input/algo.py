
myfile = open('a_example.in', 'r')
lines= myfile.readlines()
lines_as_list=[]
special_lines=[]
data_lines=[]
for x in lines:
    lines_as_list.append(x.split())
myfile.close()
#This code will convert all str to int
for line in lines_as_list:
    for element_index in range(0 , len(line)) :
        if line[element_index].isnumeric() == True:
            line[element_index]=int(line[element_index])
        else:
            pass

    print(line)

#Basic Editor ends here
#####################################################################

t_videos = lines_as_list[0][0]
t_endpoints = lines_as_list[0][1]
request_descriptions = lines_as_list[0][2]
caches =lines_as_list[0][3]
chache_length=lines_as_list[0][4]

#Chache length of each server is same

videos = ( [index_of_video , video_space] for index_of_video,video_space in zip(range(t_videos),lines_as_list[1]) )
# Categorising each endpoint
def endpoint_make(start_list):
    endpoint=[start_list]
    for x in range(start_list[1]):
        endpoint=endpoint+lines_as_list

endpoints = ( for index_of_endpoint, in zip(range(t_endpoints),lines_as_list[1]) )

def get_the_subs(list,start):
    lis=[]
    for x in range(list[start][1]):
        lis=lis+[list[start + x + 1]]
    return(lis)
def get_indexes(list):
    indexes=[0]
    indexes.append(indexes[-1] + list[0][1] + 1)
