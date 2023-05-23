import requests
from bs4 import BeautifulSoup as bs
def get_content(item):

	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
	item_link=[]
	item_title=[]
	item_image_link=[]

	result_list=[]
	all_items_list = []
	soup_list = []

	url = ''

	url_dict = {'Салаты':'https://lefood.menu/salaty/',
				'Выпечка':'https://lefood.menu/vypechka/',
				'Супы':'https://lefood.menu/pervye-blyuda/',
				'Гарниры':'https://lefood.menu/vtorye-blyuda/',
				'Напитки':'https://lefood.menu/napitki/',
				'Десерты':'https://lefood.menu/deserty/',
				'Перекусы':'https://lefood.menu/zakuski/'
				}
	try:
		for key,val in url_dict.items():
			if key==item:
				url=val


	
	

		r=requests.get(url,headers=headers)

		soup = bs(r.text,'lxml')

		links = soup.find('div',class_='recipes-list').find_all('div',class_='recipes-block')
	except:
		return 'Что - то пошло не так. Попробуйте перезапустить приложение.'

	finally:
		for link in links:
	
			item_link.append(link.a['href'])
			item_title.append(link.a['title'])
			item_image_link.append(link.img['src'])
	

		for i in range(0,len(item_title)):
	
			result_list.append({
				'title':item_title[i],
				'url':item_link[i]
				
			})
				
			
		
	
	return result_list

def get_info_from_link(link):
	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
	lnk = link
	list_with_content = []
	

	try:
		r = requests.get(lnk,headers=headers)
		soup = bs(r.text,'lxml')
		content = soup.find('div',class_='inner-content page-content_recipe hrecipe')
		#print(content)

		

	except:
		return 'Something went wrong.'

	finally:
		try:
			picture=content.picture.img['src']
			ingridients = content.find_all('li')
			steps = content.find('div',class_='recipe-steps_list instructions')
			ing = []
			stp = steps.text.replace('\n','')

			#print()

			for i in ingridients:
				
				ing.append(i.text.replace('\n',''))
			list_with_content = [picture,ing,stp]

			return list_with_content
				
			

		except:
			return 'Error'



#a = get_content('Гарниры')
#print(type(a))
#print(a[2])


#print(len(a[1]['title']))



