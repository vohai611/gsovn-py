import requests as req
import pandas as pd
import unicodedata
import bs4 
import re

def gso_avail():
    url =  "http://www.gso.gov.vn/so-lieu-thong-ke/"
    res = req.get(url, verify=False)
    soup = bs4.BeautifulSoup(res.text)
    content = soup.find_all('a', href= True)
    a = [i.text for i in content]
    link = [i['href'] for i in content]
    ontent = soup.select('#content a')
    df = {'content': a, 'link': link}
    df = pd.DataFrame(df)
    my_link = df.link.str.count(r'px-web')
    my_link >=1
    df = df[my_link >=1]
    df = df.reset_index(drop=True)
    out = gso_data(df)
    return out

class gso_data:
  df = None
  def __init__(self, data):
    self.df= data
  def __repr__(self):
    return repr(self.df)

  @staticmethod
  def normalize(term):
    term = unicodedata.normalize("NFKD",term).encode('ascii', 'ignore').decode().lower()
    return term
    
  def search(self, term):
    """
    ## Search in content
    The search perform on ASCII transformed content
    ### params:
    term: term you want to search
    ### return:
    gso_data object
    """
    term = gso_data.normalize(term)
    df = self.df 
    df['data_set_normalize'] = list(map(gso_data.normalize, df['content']))
    match = df['data_set_normalize'].str.contains(term)
    df = df.loc[match]
    del df['data_set_normalize'] 
    out = df.reset_index(drop=True)
    out = gso_data(out)
    return out
  def head(self, n=5):
    """
    ##  View Top Data Set
    ### params: 
    n: Number of line to view
    ### return
    gso_data object
    """
    out = gso_data(self.df.head(n))
    return out
  def get(self, multi = False):
    """
    ## Download Data 
    Can download multiple dataset
    ### return
    list of [title, dataset]
    """
    if(len(self.df) == 1):
      link = self.df['link'][0]
      out = self.__get(link)
    elif (len(self.df) == 0):
      print("There are no dataset")
    elif not multi:
      raise ValueError("There are more than one dataset. Please set `multi=True` if you want to download all datasets")
    else:
      data_set_link = list(self.df['link'])
      out = map(self.__get, data_set_link)
      out = list(out)
    return out

  def __get(self, link):
    content = req.get(link, verify=False)
    soup = bs4.BeautifulSoup(content.text)
    get_link = soup.iframe['src']
    # extract page inside iframe
    page = req.get(get_link)
    page_content  = bs4.BeautifulSoup(page.text)
    # extract options
    form_val = page_content.select(".variableselector_valuesselect_statistics")
    option_count = [i.text for i in form_val]
    option_count = [re.findall(r'[0-9]+', i) for i in option_count]

    option_count = list(filter(None, option_count))

    form_key = ["ctl00$ContentPlaceHolderMain$VariableSelector1$VariableSelector1$VariableSelectorValueSelectRepeater$ctl0" +
                str(i) + "$VariableValueSelect$VariableValueSelect$ValuesListBox" for i in range(1, len(option_count) +1)]

    # set form value= 0:x
    form_value = [ list(range( int(i[0]))) for i in option_count]
	
    form_to_submit = dict(zip(form_key, form_value))
    form_to_submit["ctl00$ContentPlaceHolderMain$VariableSelector1$VariableSelector1$OutputFormats$OutputFormats$OutputFormatDropDownList"] = "tableViewLayout1"
	
    # extract the form input (include hiden input)
    name = [i['name'] for i in page_content.find_all('input')]
    #
    def take_value(content):
          input = content.find_all('input')
          r = input 
          for i in range(len(input)):
            try:
              r[i] = input[i]['value']
            except:
              r[i] = ""
          return r
    value = take_value(page_content)
    params = dict(zip(name, value))
	
    # modified fields need to change
    for item in form_to_submit.items():
      params[item[0]] = item[1]
	
    # send POST request
    out = req.post(get_link, data= params,verify=False)
    df = pd.read_html(out.content, encoding="UTF-8", skiprows =0)[0]
    # first index is titile
    title = df.columns.get_level_values(0)[1]
    df.columns = df.columns.get_level_values(1)
    return [title, df]   
    
#a 3= gso_avail()
#result = a.search("Mức").view(2).get()







    