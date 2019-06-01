var axs = axios.create({
    baseURL: 'http://localhost:5000', // バックエンドB のURL:port を指定する
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest'
    },
    responseType: 'json'  
})

var app = new Vue({
    el: '#app',
    data : {
        articles : [],
        article_count : 0
    },
    mounted : async function(){
        let url = CONTEXT_PATH + 'articles/getFirstArticles/'
        console.log(url)
        let response = await axios.get(url)
        console.log(response)
        app.article_count = response.data.article_count
        app.articles = response.data.articles
    },
    methods : {
        getNextArticles: async function(){
            let length = app.articles.length
            let lastid = app.articles[length-1].id
        
            let url = CONTEXT_PATH + 'articles/getNextArticles/'
            // let param = new URLSearchParams();
            // param.append('lastid', lastid)
            let param = {
                lastid: lastid
            }

            let response = await axs.post(url, param)
            app.article_count = response.data.article_count
            app.articles = response.data.articles
        }
    }
});
