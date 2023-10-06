from flask import Flask, render_template, request 
import random
import requests
app = Flask(__name__)

@app.route('/')
def home():
    name = '강민범'
    lotto = [16,18,22,43,32,11]

    def generate_lotto_numbers():
        lotto_numbers = random.sample(range(1, 46), 6)
        lotto_numbers.sort()
        return lotto_numbers
 
    random_lotto = generate_lotto_numbers()


    def count_common_elements(list1, list2):
        # 두 리스트에서 공통 요소를 찾고 세는 방법
        common_elements = set(list1) & set(list2)
        count = len(common_elements)
        return count

    common_count = count_common_elements(lotto, random_lotto)

    context={
        "name": name,
        "lotto": lotto,
        "random_lotto": random_lotto,
        "common_count": common_count,
    }
    return render_template('index.html',data = context)

@app.route('/mypage')
def mypage():
    return 'This is MyPage!'

@app.route('/movie')
def movie(): 
    query = request.args.get('query')
    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}"
    )
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    return render_template('movie.html', data=movie_list)

@app.route("/answer")
def answer():
    if request.args.get('query') :
        query = request.args.get('query')
    else :
        query = 20230601
    
    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={query}"

    res = requests.get(URL)
    rjson = res.json()
    movie_list  = rjson.get('boxOfficeResult').get('weeklyBoxOfficeList')
    return render_template("answer.html", data=movie_list)

if __name__ == '__main__':  
    app.run(debug=True)
