library("tidyverse")
library("lubridate")
library("tidytext")
library("scales")
library("ggridges")
library("ggrepel")
theme_set(theme_bw())

dat <- read.csv("distribution_samples.csv",
                header= TRUE,
                stringsAsFactors = FALSE,
                sep = ",")

dat$clas <- as.character(dat$clas)
ggplot(dat, aes(x=x, y=y, color=clas)) +
  geom_point(size=2) +
  facet_wrap(~ type, ncol=3) +
  scale_color_discrete(name="Class") +
  labs(title="", x="", y="") +
    theme(legend.position = "none",
          strip.background = element_rect(colour="purple",
                                          fill="white"))

dat2 <- read.csv('differences.csv',
                 header=TRUE,
                 sep=",")
dat2 %>% pivot_longer(-X) %>%
  ggplot(aes(x=name,y=value,fill=name))+
  labs(title="", x="", y="Percentage better than KNN") +
  geom_boxplot(alpha=0.8)+ 
  geom_jitter(color="black", size=0.4, alpha=0.8)+
scale_y_continuous(labels = scales::percent)

