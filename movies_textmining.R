library(rJava)
library(tm)		
library(SnowballC)
library(wordcloud)
library(RWeka)	
library(xml2)
library(textir)
library(maptpx)
library(data.table)
library(stringr)
library(slam)
library(ggplot2)
library(rvest)
library(readr)
require(graphics)
----------------------------------------------------------------
  

url <-'http://www.imdb.com/title/tt8413338/reviews?ref_=tt_ql_3'
url<-'https://www.imdb.com/title/tt4975722/reviews?ref_=tt_ql_3'

page=read_html(url)

movie<-html_nodes(page,'div.text.show-more__control')
movie_text<-html_text(movie)
corpus<-Corpus(VectorSource(movie_text))

inspect(corpus[1:5])
inspect(movie_clean[1:5])
movie_clean<-tm_map(corpus,tolower)
movie_clean<-tm_map(movie_clean,removeNumbers)
movie_clean<-tm_map(movie_clean,removePunctuation)
movie_clean<-tm_map(movie_clean,removeWords,c("the","and",'character',stopwords("english")))
movie_clean<-tm_map(movie_clean,stripWhitespace)

inspect(movie_clean[1:5])

review_dtm<-DocumentTermMatrix(movie_clean)
review_dtm
inspect(review_dtm[1:5,])
review_dtm<-removeSparseTerms(review_dtm,.99)
inspect(review_dtm[1:5,])

freq<-findFreqTerms(review_dtm,20)
freq_moview<-data.frame(sort(colSums(as.matrix(review_dtm)),decreasing = TRUE))
freq_moview
#Word cloud
wordcloud(rownames(freq_moview),freq_moview[,1],max.words =50,colors = brewer.pal(1,'Dark2'))


