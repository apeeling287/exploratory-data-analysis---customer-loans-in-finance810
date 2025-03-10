# Exploratory Data Analysis Project-Customer Loans in Finance
## Description
this project is to display my abilities of data analysis using techniques such as object oriented programming, connecting to databases using SQLAlchemy and statistical analysis of data with the example of customer loans in finance 
# Table of Contents
1. [Introduction](#introduction)
2. [Section 1 - Connect to Database](#section-1)
    - [Subsection 1.1 - Load credentials](#subsection-1.1)
    - [Subsection 1.2 - ](#subsection-1.2)
3. [Section 2 - Transform the Dataframe](#section-2)
4. [Section 3 - Extract information from the dataframe](#section-3)
    - [Subsection 3.1 - dataset description](#subsection-3.1)
5. [Section 4 - Dataframe Transformations](#section-4)
    - [Subsection 4.1 - dataset transformations](#subsection-4.1)
    - [Subsection 4.2 - dataset plots](#subsection-4.1)
    - [Subsection 4.3 - identifying outliers](#subsection-4.1)

## Introduction
This project uses Object Oriented Programming to connect to a RDS and extract data from this database for data transformation, analysis and visualisation purposes

## Section 1
The class RDSDatabaseConnector allows the user to connect to a database
### Subsection 1.1
There is a function to load in a yaml file containing RDS credentials so that specific credentials can be loaded in to connect to specific databases

### Subsection 1.2
There is a function to extract data from the database and return is as a dataframe 

## Section 2
This class allows transformation of data in the dataframe to different datatypes such as date, string and numeric 

## Section 3
This class allows information to be gained about the data 

### Subsection 3.1
Functions allow the user to extract information about the dataframe e.g. statistical values: mean, median, mode, unique values, count of nulls and the shape of the dataframe 

## Section 4
This class allows transformations to be performed on a dataframe

### Subsection 4.1
Functions allow the user to perform transformations such as count null values, drop rows and columns containing null values and imputing values 

### Subsection 4.2
Functions allow the user to visualise whether the dataset is normally distributed and perform log transformations, boxcox and yeojohnson transformations if required 

### Subsection 4.3
Functions allow the user to 