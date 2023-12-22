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
max_urls = int(input('How much sites you want ? '))
max_urls_pr = max_urls
if (max_urls > 100):
    max_urls_pr = 100

langu = input('what web lang you want ex: en,ar ? ')

array = []
for i in googlesearch.search(query,num=max_urls_pr,stop=max_urls,pause=10,lang=langu):
    array.append(i)
    print(f'{i}\n')

a = input('you want to save it ? y / n ')
if a.lower() == 'y':
    save = '\n'.join([str(url) for url in array])
    name = input('What do u wanna name of the file ? : ')
    file = open(f"{name}.txt", "w")
    file.write(save)
    file.close()
    print(f'File {name}.txt Saved ')
    quit()
else:
    quit()
