#draw_gene

This is a small python program to help you draw genes and dynamicly show the process.

##Requirement

- python 3.4+


## Install Dependencies
Choose either way to install numpy package.

Use pip:

    pip install numpy
    
Use conda:
    
    conda install numpy
    
## Run the Program

    python draw_gene.py

## Input File Formate
The example file is "test.txt".
>All the input columns should be separate with tab.

First row (remember to add the following zeros to prevent error):

    formate: total_length_of_your_DNA    0   0   0
    example:            
                1000	0	0	0

Following rows (the genes you want to draw):

Positive strand need to be 1, and negative strand need to be 0. 

    formate: gene_name  start_position end_position strand_type
    example:
                geneA	50    100    1
                geneB   200    300    0
                geneC	500    700    1

## Result
The red part (the upper part) represents the positive strand.
The blue part (the lower part) represents the negative strand.
The gene names and total length of your DNA will also be shown on the plot.
![image](https://github.com/LeeYiFang/draw_gene/blob/master/output_result.PNG)
