var app = new Vue({
    el: 'app',
    data : {
        articles : [],
        article_count : 0
    },
    mounted : function(){
        let articles = getFirstArticles()
        this.articles = articles
    }
});

const getFirstArticles = () => {
    axios.get(CONTEXT_PATH + 'getFirstArticles/')
        .then(function(response){
            console.log(response)
            app.article_count = response.data.article_count
            return response.data.articles
        })
        .catch(ERROR_RESPONSE);
}