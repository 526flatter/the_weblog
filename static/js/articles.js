var app = null;

const initapp = () => {
    app = new Vue({
        el: '#app',
        data : {
            articles : [],
            article_count : 0
        },
        mounted : getFirstArticles()
        // mounted : function(){
            // this.articles = getFirstArticles()
            // console.log(this.articles)
        // }
    });
    
}

const getFirstArticles = () => {
    let url = CONTEXT_PATH + 'articles/getFirstArticles/'
    console.log(url)
    axios.get(url)
        .then(function(response){
            console.log(response)
            app.article_count = response.data.article_count
            console.log(app.article_count)
            console.log(response.data.articles)
            app.articles = response.data.articles
            // return response.data.articles
        })
        .catch(ERROR_RESPONSE);
}

initapp();