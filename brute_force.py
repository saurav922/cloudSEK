import requests
val = input('enter a webapp url:')
print(val)
# now we have to get the words from the list of sample word list
sample_word = open('sample_word_list.txt', 'r')
while True:
    line = sample_word.readline()
    url = val + "/" + line.replace("\n","")
    response = requests.get(url)
    if response.status_code == 200 or response.status_code == 302:
        print(url + "   " + str(response.status_code))
    if not line:
        break
sample_word.close()