# VAMP2 rotation project 
This is my rotation project in Andrew Su's Lab.


## Description 
### Use case: Treatment of VAMP2 deficiency 
Clinical reports have described patients with VAMP2 gene deficiency and symptoms related with developmental delay, autistic tendencies, and behavioral disturbances.(In this article https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24109?af=R, the authors describe five new patients with VAMP2 deficiency. Five different patients described ~1 year earlier in https://pubmed.ncbi.nlm.nih.gov/30929742/)


### BioThings Explorer (BTE)
Documentation: https://biothings-explorer.readthedocs.io/en/latest/

Using BTE, we retrieved a path (VAMP2 > Biological Process > Genes > Chemical Substances > Diseases) that helped us to identify new potential treatments for VAMP2 deficiency. 


### Dash Cytoscape 
Documentation: https://dash.plotly.com/cytoscape

We used Dash Cytoscape to display the path we retrieved from BioThingsExplorer. 
This is an example  of the graph (with 500 connections) we build using Dash Cytoscape:


![example](https://github.com/Carolina1396/VAMP2_BTE/blob/cb4eb29b4b8a262a13d17347ff1f233e6a5e7e6e/images/cytoscape_example_500connections.png?raw=true)  
