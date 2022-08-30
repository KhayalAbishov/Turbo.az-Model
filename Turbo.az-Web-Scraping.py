import requests
from bs4 import BeautifulSoup
from csv import writer

baseUrl = "https://turbo.az"

with open('turbobbb.csv', 'w', encoding="utf-8") as csv_file:
  csv_writer = writer(csv_file)
  csv_writer.writerow(['city', 'brand', 'model', 'year','body','engine','engine_power','fuel_type','mileage','gearbox','transmission','new','price'])

  for num in range(1,417):
      response = requests.get(f"https://turbo.az/autos?page={num}").content
      soup = BeautifulSoup(response, 'html.parser')
      objects = soup.find_all(class_='products-container')[0].find_all(class_='products')[2].find_all(class_='products-i')

      for i in objects:
        link = baseUrl + i.find("a")['href']
        response2 = requests.get(link).content
        soup2 = BeautifulSoup(response2, 'html.parser')
        objects2 = soup2.find(class_='product-properties-container').find(class_='product-properties').find_all(class_='product-properties-i')

        city = objects2[0].find('div').string
        brand = objects2[1].find('a').string
        model = objects2[2].find('a').string
        year = objects2[3].find('a').string
        body = objects2[4].find('div').string
        # color = objects2[5].find('div').string
        engine = objects2[6].find('div').string
        engine_power = objects2[7].find('div').string
        fuel_type = objects2[8].find('div').string
        mileage = objects2[9].find('div').string
        gearbox = objects2[10].find('div').string
        transmission = objects2[11].find('div').string
        new = objects2[12].find('div').string
        price = objects2[13].find(class_='product-properties-value').find(class_='product-price').text.strip(' AZN $')

        csv_writer.writerow([city, brand,model,year,body,engine,engine_power,fuel_type,mileage,gearbox,transmission,new,price])
      # print([city, brand,model,year,body,color,engine,engine_power,fuel_type,mileage,gearbox,transmission,new,price])
      # print(len(objects), len(objects2), len(a))

    # print(city)
    # print(brand)
    # print(model)
    # print(year)
    # print(body)
    # print(color)
    # print(engine)
    # print(engine_power)
    # print(fuel_type)
    # print(mileage)
    # print(gearbox)
    # print(transmission)
    # print(new)
    # print(price)
    # print(objects2)