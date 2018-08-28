from googleplaces import GooglePlaces, types, lang
import pandas as pd
import time
API_KEY = 'AIzaSyDMyNyQlAw_XMeUf9NTNQ7xE09Bo1k-t3U'

google_places = GooglePlaces(API_KEY)

#take input search information
location1 = str(input('Please enter the geographic location:\n'))
keyword1 = str(input('Please enter the keyword:\n'))
radius1 = int(input('What is the search radius:\n'))

#relevant types:

query_result = google_places.nearby_search(
				location=location1, keyword=keyword1, 
				radius=radius1)

next_page = query_result.next_page_token

print('Time to give Google\'s API a break.')

time.sleep(2)

if query_result.has_next_page_token:
    query_result_second_page = google_places.nearby_search(location=location1, keyword=keyword1, 
                                    radius=radius1, pagetoken=query_result.next_page_token)
    responses = [query_result, query_result_second_page]
    
    print('Time for another break....')
    time.sleep(2)

    if query_result_second_page.has_next_page_token:
        query_result_third_page = google_places.nearby_search(location=location1, keyword=keyword1, 
                                    radius=radius1, pagetoken=query_result_second_page.next_page_token)
        responses = [query_result, query_result_second_page, query_result_third_page]
else:
    responses = [query_result]

#if query_result.has_attributions:
	#print(query_result.html_attributions)


data = pd.DataFrame(columns=['Name', 'Phone Number', 'Address', 'Website', 'Google URL'])

for response in responses:
    for place in response.places:
        place.get_details()
        data = data.append({
            "Name": place.name,
            "Phone Number": place.local_phone_number,
            "Address": place.formatted_address,
            "Website": place.website,
            "Google URL": place.url
            }, ignore_index=True)
        #print(place.name)
        #print(place.geo_location)
        #print(place.place_id)
print(data.head())
print(data.shape)

data.to_csv('d2_' + keyword1 + '_in_' + location1 + '.csv', encoding='utf-8')