const axs = axios.create({
    baseURL: 'http://localhost:5000', // バックエンドB のURL:port を指定する
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest'
    },
    responseType: 'json'  
})

const articleComponent =  {
    props: ['article'],
    template: `<div class="article">
                <label>{{ article.title }}</label>
                <div class='contentinfo'>
                    <label>{{ article.user }}</label>
                </div>
                </div>`
}

async function getArticles(page = 1) {
    let url = CONTEXT_PATH + 'articles/getArticles'
    console.log(url)
    return axios.get(url, {params: {page: page.toString()}})
}

const app = new Vue({
    el: '#app',
    data : {
        articles : [],
        page : 1,
        maxpage: 0
    },
    components: {
        'article-component': articleComponent
    },
    mounted : async function(){
        const response = await getArticles()
        console.log(response)
        app.articles = response.data.articles
        app.maxpage = response.data.maxpage
    },
    methods : {
        getArticles: async function(next){
            const response = await getArticles(next)
            console.log(response)
            app.articles = response.data.articles
            app.maxpage = response.data.maxpage
            app.page = next
        }
    }
});
