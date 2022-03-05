library("tidyverse")
library("lubridate")
library("tidytext")
library("scales")
library("ggridges")
library("ggrepel")
library("ggthemes")
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
        panel.border = element_rect(colour="#fe5185", size=0.8),
          strip.background = element_rect(colour="blue",
                                          fill="white", size=0.8),
        axis.text.x=element_text(colour="#fe5185"),
        axis.text.y=element_text(colour="#fe5185"),
        axis.ticks = element_line(colour = '#fe5185', size = 0.8, linetype = 'dashed')
        )

dat2 <- read.csv('differences.csv',
                 header=TRUE,
                 sep=",")
dat2 %>% pivot_longer(-X) %>%
  ggplot(aes(x=name,y=value,fill=name))+
  labs(title="", x="", y="Percentage better than KNN") +
  geom_boxplot(alpha=0.8)+ 
  geom_jitter(color="black", size=0.4, alpha=0.8)+
scale_y_continuous(labels = scales::percent)

reg1 <- read.csv('linear_model_1_input_15.csv',
                 header=TRUE,
                 sep=",")

ggplot(reg1, aes(x=x, y=y, color=from)) +
  geom_point(size=1.5) +
  geom_function(aes(colour="True regression fn."),
                fun = ~ -22*.x + 45) +
  scale_color_hue(name = "",
                  labels = c("GPT-3 predictions",
                             "Training points",
                             "True regression fn."))

reg2 <- read.csv('linear_model_2_input_15.csv',
                 header=TRUE,
                 sep=",")

ggplot(reg2, aes(x=x, y=y, color=from)) +
  geom_point(size=1.5) +
  geom_function(aes(colour="True regression fn."),
                fun = ~ 24*.x + 95) +
  scale_color_hue(labels = c("GPT-3 predictions",
                             "Training points",
                             "True regression fn.")) +
  geom_vline(xintercept=30, linetype='dotted', col = 'purple', label="Training bound") +
  geom_vline(xintercept=70, linetype='dotted', col = 'purple') +
  theme(legend.position=c(0.8, 0.2),
        legend.title=element_blank(),
        legend.box.background = element_rect(colour = "purple", size=1),
        legend.margin=margin(t=-0.18,l=0.05,b=0.0,r=0.05, unit='cm'))


reg3 <- read.csv('quadratic_model_2_input_25_smaller_variance.csv',
                 header=TRUE,
                 sep=",")

ggplot(reg3, aes(x=x, y=y, color=from)) +
  geom_point(size=1.5) +
  geom_function(aes(colour="True regression fn."),
                fun = ~ (.x**2) - 88*.x + 3) +
  scale_color_hue(labels = c("GPT-3 predictions",
                             "Training points",
                             "True regression fn.")) +
  geom_vline(xintercept=24, linetype='dotted', col = 'purple', label="Training bound") +
  geom_vline(xintercept=75, linetype='dotted', col = 'purple') +
  theme(legend.position=c(0.8, 0.2),
        legend.title=element_blank(),
        legend.box.background = element_rect(colour = "purple", size=1),
        legend.margin=margin(t=-0.18,l=0.05,b=0.0,r=0.05, unit='cm'))

reg4 <- read.csv('quadratic_model_1_input_25.csv',
                 header=TRUE,
                 sep=",")


ggplot(reg4, aes(x=x, y=y, color=from)) +
  geom_point(size=1.5) +
  geom_function(aes(colour="True regression fn."),
                fun = ~ (-5)*(.x**2) + 35*.x + 201) +
  scale_color_hue(labels = c("GPT-3 predictions",
                             "Training points",
                             "True regression fn.")) +
  geom_vline(xintercept=20, linetype='dotted', col = 'purple', label="Training bound") +
  geom_vline(xintercept=80, linetype='dotted', col = 'purple') +
  theme(legend.position=c(0.2, 0.2),
        legend.title=element_blank(),
        legend.box.background = element_rect(colour = "purple", size=1),
        legend.margin=margin(t=-0.18,l=0.05,b=0.0,r=0.05, unit='cm'))

