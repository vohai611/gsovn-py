import gsovn.gsovn.gsovn as gso
import importlib
import unicodedata

importlib.reload(gso) 

k  = gso.gso_avail()

k.search('san xuat cong nghiep').get()
k.head(20)

k.search('y te')

k.df['content'].str.match('T').any()

unicodedata.normalize("NFKD",'chuyển').encode('ascii', 'ignore').decode()