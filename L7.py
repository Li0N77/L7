from time import sleep
import pip
import os

try:
    import googlesearch
except ImportError:
    print("i well install google module for you after 3 Seconds")
    sleep(3)
    pip.main(['install','google'])
if os.path.exists(".google-cookie"):
  os.remove(".google-cookie")
os.system('clear')
print("""
      Programmed By Li0N AlShmmari
      Github - Li0N77
      """)
query = input('Enter your dork : ')
max_urls = int(input('How much sites you want MAX : 100? '))
langu = input('what web lang you want ex: en,ar ? ')


file = open("list.txt", "w")
array = []
for i in googlesearch.search(query,num=max_urls,stop=max_urls,pause=10,lang=langu):
    array.append(i)
    print(f'{i}\n')
    file.write('\n'.join([str(url) for url in array]))

print("Saved in list.txt")
file.close()
quit()
