#scraping flights from Los Angeles 
url="https://flightaware.com/live/airport/KLAX/arrivals?;offset=280;order=actualarrivaltime;sort=DESC"
html=request.urlopen(url)
soup=BeautifulSoup(html)
#get urls
urls=soup.find_all(href=re.compile("/live/airport/KLAX/arrivals"))
urls
#grab flight information 
soup_div=soup.find_all('div')
soup_div1=soup.find_all('td',class_=re.compile('smallrow1'))
soup_div1 
soup_div2=soup.find_all('td',class_=re.compile('smallrow2'))
soup_div2

#div1
flights=[]
for f in soup_div1:
    print(f.get_text()) 
    flights.append(f.get_text())

type(flights)

#div2
flights=[]
for f in soup_div2:
    print(f.get_text())
    flights.append(f.get_text())


#convert list to numpy array
flights_array=array(flights)
flights_array.shape 
flights_a1=flights_array.reshape(10,5)

#convert array to dataframe
df=pd.DataFrame(flights_a1)
#write to csv 
df.to_csv("x.csv",sep='\t')