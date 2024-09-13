import requests

api_key = 'abcRefWSP3w1LRHjvt7jCxBBJSZibbcwrAwkfvSS'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

def img_of_the_day():
    response = requests.get(url)
    print(response.content)
    response = response.json()
    print(response)
    title = response['title']
    date = response['date']
    explanation = response['explanation']
    image = requests.get(response['hdurl'])
    image = image.content
    with open('img.jpeg','wb') as img :
        img.write(image)

    return [title, explanation, date]