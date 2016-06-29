#データ読み込み
mansion.frame<-read.table("mansion.rda",header=TRUE)
mansion.frame 

# データ要約, プロット
summary(mansion.frame)
cor(mansion.frame)
plot(mansion.frame)

# 散布図
plot(mansion.frame$area, mansion.frame$price)

# 単回帰分析
mansion.lm.simple<-lm(formula=price ~ area, data=mansion.frame)
mansion.lm.simple
summary(mansion.lm.simple)

coef(mansion.lm.simple)
coefficients(mansion.lm.simple)

# 標本回帰直線
abline(mansion.lm.simple)

# 単回帰分析の要素のリスト
names(mansion.lm.simple)

# 残差抽出, インデックスプロット
mansion.resid<-mansion.lm.simple$residuals
mansion.resid
plot(mansion.resid)

# 単回帰分析の要約
mansion.lm.simple.summary<-summary(mansion.lm.simple)
mansion.lm.simple.summary
names(mansion.lm.simple.summary)
mansion.lm.simple.summary$fstatistic


# 単回帰分析に関する回帰診断プロット
par(mfcol=c(2,2))
plot(resid(mansion.lm.simple),ylab="Residuals")
mtext("Index Plot of Residuals", 3, 0.25, cex = 1)
plot(mansion.lm.simple,which=c(1,2))
plot(density(resid(mansion.lm.simple)),main="")
mtext("Density Plot of Residuals", 3, 0.25, cex = 1)
par(mfcol=c(1,1))

# 重回帰モデルの当てはめ
mansion.lm<-lm(formula=price ~ area + year, data=mansion.frame)
mansion.lm

# 結果の要約
mansion.lm.summary<-summary(mansion.lm)
mansion.lm.summary


# 重回帰分析に関する回帰診断プロット
par(mfcol=c(2,2))
plot(resid(mansion.lm),ylab="Residuals")
mtext("Index Plot of Residuals", 3, 0.25, cex = 1)
plot(mansion.lm,which=c(1,2))
plot(density(resid(mansion.lm)),main="")
mtext("Density Plot of Residuals", 3, 0.25, cex = 1)
par(mfcol=c(1,1))

