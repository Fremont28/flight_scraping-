#grabbing flights from San Diego International airport 
url="http://www.san.org/Flights/Flight-Status"
html=request.urlopen(url)
soup=BeautifulSoup(html)
#grab info
soup_div2=soup.find_all('tbody')
soup_div2

flights_sd=[]
for f in soup_div2:
    print(f.get_text()) 
    flights_sd.append(f.get_text())

type(flights_sd) #class list

sd_flights_array=array(flights_sd)
sd_flights_array
sd_flights_array.shape 
sd_df=pd.DataFrame(sd_flights_array)
sd_df.to_csv("sdx.csv",sep='\t')

#search for string in san diego flights
#e.j. 1 
busca_for=['Las Vegas']
flights_xx=[flights_sd.str.contains(x) for x in busca_for]




