import requests


def img_of_the_day(api_key , date):
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}'
    response = requests.get(url)
    print(response)
    response = response.json()
    title = response['title']
    explanation = response['explanation']
    image = requests.get(response['hdurl'])
    image = image.content
    with open('img.jpeg','wb') as img :
        img.write(image)

    return [title, explanation]
