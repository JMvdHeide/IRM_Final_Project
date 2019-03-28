data = read.csv('police_reports_Groningen.csv', header = TRUE, sep = ";")
str(data)

qqnorm(data$police_reports)
qqline(data$police_reports)

plot(density(data$police_reports), main = "Density plot for police_reports")

reports <- c(data$police_reports)
wilcox.test(data$police_reports, alternative = "greater", mu=500)
