import pandas as pd
import networkx as nx

def compute_moral_homophily(G):
    # The function displays the moral homophily scores of five moral foundations
    # i.e.care, fairness, ingroup, authority and purity using the input retweet network
    
    #Extract nodes and edges of the input network
    nodes=list(G.nodes())
    edges=list(G.edges())
    
    #Extract labels of every node computed based on the moral loadings
    #of the users computed previously 
    node_labels=nx.get_node_attributes(G,'label')
    
    #creating list to store homophily score of each node based on thier label
    hom_node=[[] for i in range(5)]
    
    #for each node computing moral homophily score with the help of edges
    #connecting nodes of similar types 
    for node in nodes:
        E_di_count=0
        out_edges=list(G.out_edges(node))
        nghs_nodes=[edge[1] for edge in out_edges]
        if len(nghs_nodes)>=1:
            dim=node_labels[node]
            for ngh in nghs_nodes:
                if node_labels[ngh]==dim:
                    E_di_count+=1
            hom_node[dim].append(E_di_count/len(nghs_nodes))
            
    #print the average homophily score of each dimension.
    for i in range(5):
        print('homophily for dim=',i,' is ',np.average(hom_node[i]))
        
        
        
#*******Compute moral homophily scores for English tweets based retweet network*******#

#Load English Retweet Network (Network can be constructed from the given tweet ids of English tweets)
G=nx.read_gexf('eng_retweet_network.gexf')

#call moral homophily function to display scores for each moral foundation
compute_moral_homophily(G)

#*******Compute moral homophily scores for Japanese tweets based retweet network*******#

#Load English Retweet Network (Network can be constructed from the given tweet ids of Japanese tweets)
G=nx.read_gexf('jp_retweet_network.gexf')

#call moral homophily function to display scores for each moral foundation
compute_moral_homophily(G)