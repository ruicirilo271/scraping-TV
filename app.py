from flask import Flask, render_template
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

def get_m3u8_url(page_url):
    # Configurar navegador headless
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3')

    driver = webdriver.Chrome(options=options)

    try:
        print(f"🔍 Acessando página: {page_url}")
        driver.get(page_url)

        # Esperar o carregamento do player
        time.sleep(10)

        # Procurar qualquer requisição com .m3u8
        for request in driver.requests:
            if request.response and '.m3u8' in request.url:
                print("✅ Link .m3u8 encontrado:", request.url)
                return request.url

        print("❌ Nenhum link .m3u8 encontrado.")
        return None
    finally:
        driver.quit()

@app.route('/')
def index():
    # Página inicial com o novo link para o canal "sport-tv-nba"
    return render_template('index.html')

@app.route('/play/<int:channel_id>')
def play(channel_id):
    # Busca o link .m3u8 apenas quando o usuário escolher o canal
    if channel_id == 1:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/sport-tv-1.html")
    elif channel_id == 2:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/hustler-hd.html")
    elif channel_id == 3:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/sport-tv-2.html")
    elif channel_id == 4:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/bang-u.html")
    elif channel_id == 5:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/cum-4k.html")
    elif channel_id == 6:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/mytime.html")
    elif channel_id == 7:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/benfica-tv.html")
    elif channel_id == 8:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/sporting-tv.html")
    elif channel_id == 9:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/tvi-reality.html")
    elif channel_id == 10:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/moviesphere.html")
    elif channel_id == 11:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/rtp-1.html")
    elif channel_id == 12:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/miami-tv.html")
    elif channel_id == 13:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/dorcel-tv.html")
    elif channel_id == 14:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/trace-latina.html")
    elif channel_id == 15:
        stream_url = get_m3u8_url("http://www.tvhdinacios.com/canal/abolatv/")
    elif channel_id == 16:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/sport-tv-nba.html")
    elif channel_id == 17:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/cmtv.html")  # Novo canal "CM TV"
    elif channel_id == 18:
        stream_url = get_m3u8_url("https://www.pirilampo.tv/live-tv/sic-noticias.html")  # Novo canal "SIC Notícias"
    else:
        stream_url = None  # Caso não haja o canal

    return render_template('play.html', stream_url=stream_url)

if __name__ == "__main__":
    app.run(debug=True)



