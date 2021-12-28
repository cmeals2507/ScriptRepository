library(tidyverse)
library(networkD3)
library(magrittr)

test3 <- read_csv("/Users/corymeals/Dropbox/Research/Diversity Work/TexasList.csv")
head(test3,3)

composers <- test3 %>%
  distinct(Composer) %>%
  rename(label = Composer)

grades <- test3 %>%
  distinct(Grade) %>%
  rename(label = Grade)

nodes <- full_join(composers, grades, by="label")
nodes <- nodes %>%
  mutate(id = 1:nrow(nodes)) %>%
  select(id, everything())

# phone.call <- phone.call %>%
#   rename(weight=n.call)

edges <- test3 %>%
  left_join(nodes, by = c("Composer" = "label")) %>%
  rename(from = id)

edges <- edges %>%
  left_join(nodes, by = c("Grade" = "label")) %>%
  rename(to = id)

#edges <- select(edges,from,to,Weight)
#head(edges,3)

library(tidygraph)
library(ggraph)
library(igraph)

net.tidy <- as_tbl_graph(test3, directed = FALSE)
degree(net.tidy, mode = "all")
test3close <- closeness(net.tidy, mode="all", normalized = T)
write.csv(test3close,"/Users/corymeals/Dropbox/Research/Diversity Work/Test3close.csv",row.names = T)

test3between <- betweenness(net.tidy,directed=F,normalized=T)
#write.csv(test3between,"/Users/corymeals/Dropbox/Research/Diversity Work/Test3between.csv",row.names = T)
test3eigen <- eigen_centrality(net.tidy,directed=F,scale=T,weights=test3$weight)
#write.csv(test3eigen,"/Users/corymeals/Dropbox/Research/Diversity Work/Test3eigen.csv",row.names = T)
test3page<- page_rank(net.tidy,vids=V(net.tidy),directed=F,weights=test3$weight)
#write.csv(test3page,"/Users/corymeals/Dropbox/Research/Diversity Work/Test3page.csv",row.names = F)

#distances(net.tidy, v=V(net.tidy)["Indiana"],to=V(net.tidy),weights=NA)

png(file="/Users/corymeals/Dropbox/Research/Diversity Work/Test5.png", width = 3200, height = 3200)
net.tidy %>%
  activate(nodes) %>%
  mutate(centrality = centrality_eigen()) %>%
  ggraph(layout = "fr") +
  geom_edge_link(aes(color="red")) +
  geom_node_point(aes(size = (centrality), color = centrality)) +
  geom_node_text(aes(label=name), size = 3, repel = TRUE) +
  theme_graph()
dev.off()

# Reform data for NetwordD3 package

nodesD3 <- mutate(nodes, id = id-1)
edgesD3 <- mutate(edges, from = from -1, to = to -1)

forceNetwork(Links = edgesD3, Nodes = nodesD3, Source = "from", Target = "to", NodeID = "label", Group = "id", Value = "Weight", opacity = 0.8, zoom = TRUE) 
%>% saveNetwork(file="/Users/corymeals/Dropbox/Research/Diversity Work/Test2.html") #Outputs network diagram to html file

# write.csv(nodes,"/Users/corymeals/Dropbox/Research/Diversity Work/nodes.csv",row.names = T)
# write.csv(edges,"/Users/corymeals/Dropbox/Research/Diversity Work/edges.csv",row.names = T)