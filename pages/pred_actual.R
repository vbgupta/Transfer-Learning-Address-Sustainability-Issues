

predictions <- read.csv("./Chicago/chi_prediction.csv")
feature <- read.csv('./Chicago/Data/ChicagoFeatures.csv')
predictions <- subset(predictions, select = - c(X))
feature <- subset(feature, select = - c(X))

chi_actual_pred <- cbind(predictions, feature)
write.csv(chi_actual_pred, "./Data/chi_actual_pred.csv")


predictions <- read.csv("./Philly/phl_prediction.csv")
feature <- read.csv('./Philly/Data/PhillyFeatures.csv')
predictions <- subset(predictions, select = - c(X))
feature <- subset(feature, select = - c(X))

phl_actual_pred <- cbind(predictions, feature)
write.csv(phl_actual_pred, "./Data/phl_actual_pred.csv")
