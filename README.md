This repository contains the source code of the paper entitled:

> **A General Framework for the Practical Disintegration of PAC-Bayesian Bounds**<br/>
> Paul Viallard, Pascal Germain, Amaury Habrard, Emilie Morvant<br/>
> Machine Learning Journal, 2023<br/>
> Presented at ECML-PKDD 2023

### Running the experiments 

To run the experiments, you have to execute the following commands in your bash shell.

> python run.py sequential generate_data.ini  
> python run.py sequential run.ini

### Generating the plots and the tables of the paper

To generate the plots and the tables, you need to execute the following commands in your bash shell.

> python run.py sequential generate_plots.ini  
> python run.py sequential generate_tables.ini 

### Generating the figures in the presentation and the poster

To generate the figures in the poster and the presentation, you need to execute the following command in your bash shell.

> python run.py sequential generate_slides.ini 

### Dependencies

The code was tested on Python 3.9.12 with the packages in the env.yml
