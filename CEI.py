import json
import requests
import streamlit as st
from requests import Request, Session

st.header('Welcome to my application')

selectbox_1 = st.sidebar.selectbox('Choose widget built with serverless function',
                                   ('Sum-Widget', 'Weather Widget', 'Bitcoin Converter', 'My account name in LOL',
                                    'Power-Widget', 'My Course Details'))
x = 0
y = 0
if selectbox_1 == 'Sum-Widget':
    st.markdown('This is a serverless function built with AWS and calculates the sum of 2 numbers you parse in.')
    st.markdown('Parse 2 float/integer numbers so I can calculate their sum.')
    parameters = {
        'x': st.text_input('Give 1st variable: '),
        'y': st.text_input('Give 2nd variable: ')
    }
    url = r'https://pkl6e32cldo3l36k7gee4tjsfi0fmran.lambda-url.us-east-1.on.aws/'
    if st.button('Calculate'):
        result = requests.request("GET", url, params=parameters)
        result_data = result.json()
        st.write(result_data)
elif selectbox_1 == 'Weather Widget':
    st.markdown('This is a function built that retrieves the temperature of your City you parse in.')
    api_key = '9268d481b9184d82485611bc81613fab'
    city_in = st.text_input('Choose city:')
    #city_in = 'limassol'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_in}&appid={api_key}&units=metric'
    if st.button('Check Weather'):
        result = requests.get(url).json()
        city = result['name']
        country = result['sys']['country']
        temp = result['main']['temp']
        feels_like = result['main']['feels_like']
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric('City:', city)
        with c2:
            st.metric('Country:', country)
        with c3:
            st.metric('Temperature:', temp, u'\xb0C')
        with c4:
            st.metric('Feels like:', feels_like, u'\xb0C')
elif selectbox_1 == 'Bitcoin Converter':
    #convert_to = st.text_input('Convert BTC to :')
    convert_to = st.selectbox('Choose currency to convert Bitcoin:', ('EUR', 'USD', 'GBP', 'CAD', 'JPY',))
    url = r'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'slug': 'bitcoin',
        'convert': convert_to,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'e34de774-047e-4e2c-9e85-354c8261d848'
    }
    session = Session()
    session.headers.update(headers)
    if st.button('Convert'):
        r = session.get(url, params=parameters)
        # Last_Modified_Time = json.loads(r.text)['data']['1']['quote'][convert_to]['last_updated']
        price = json.loads(r.text)['data']['1']['quote'][convert_to]['price']
        st.metric(value=price, label=convert_to)
elif selectbox_1 == 'My account name in LOL':
    webste = 'https://developer.riotgames.com/'
    api_key = r'RGAPI-5031b9f6-1a9d-4293-b49f-38576bea6281'
    url = r'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Maniac%20Warlock'
    api_url = url + '?api_key=' + api_key
    # print(api_url)
    r = requests.get(api_url)
    #print(r)
    data = r.json()
    st.metric(label='My name in League of Legends is :', value=data['name'])
elif selectbox_1 == 'Power-Widget':
    st.markdown('This is a serverless function built with AWS and calculates the value of 1st variable to the power of the 2nd.')
    st.markdown('Parse 2 numbers.')
    parameters = {
        'x': st.text_input('Give 1st variable: '),
        'y': st.text_input('Give 2nd variable: ')
    }
    url = r'https://sxzp3jazmw5ngdwwmb4oh7scqe0vkebv.lambda-url.us-east-1.on.aws/ '
    if st.button('Calculate'):
        result = requests.request("GET", url, params=parameters)
        result_data = result.json()
        st.write(result_data)
elif selectbox_1 == 'My Course Details':
    url = r'https://hrziscy3hclw23zzulggifkzju0altsa.lambda-url.us-east-1.on.aws/'

    parameters = {
        'id': 'CEI_521',
        'name': 'Advanced Topics in Software Technology',
        'lecturer': 'Dr. Andreas Christoforou'
    }

    result = requests.request("GET", url, params=parameters)
    result_data = result.json()
    st.write(result_data)