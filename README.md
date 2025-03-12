# Exploratory Data Analysis Project-Customer Loans in Finance
## Description
this project is to display my abilities of data analysis using techniques such as object oriented programming, connecting to databases using SQLAlchemy and statistical analysis of data with the example of customer loans in finance 
# Table of Contents
1. [Introduction](#introduction)
2. [Section 1 - Connect to Database](#section-1)
    - [Subsection 1.1 - Load credentials](#subsection-1.1)
    - [Subsection 1.2 - ](#subsection-1.2)
3. [Section 2 - Convert datatypes in the Dataframe](#section-2)
4. [Section 3 - Extract information from the dataframe](#section-3)
    - [Subsection 3.1 - dataset description](#subsection-3.1)
5. [Section 4 - Dataframe Transformations](#section-4)
    - [Subsection 4.1 - dataset transformations](#subsection-4.1)
    - [Subsection 4.2 - dataset plots](#subsection-4.1)
    - [Subsection 4.3 - identifying outliers](#subsection-4.1)
6. [Section 5 - Dataframe Plots](#section-4)
    - [Subsection 5.1 - ](#subsection-4.1)
    - [Subsection 5.2 - ](#subsection-4.1)
    - [Subsection 5.3 - ](#subsection-4.1)

## Introduction
This project uses Object Oriented Programming to connect to a RDS and extract data from this database for data transformation, analysis and visualisation purposes

## Section 1 - Connect to Database
The class RDSDatabaseConnector allows the user to connect to a database
### Subsection 1.1 - Connect to Database
There is a function to load in a yaml file containing RDS credentials so that specific credentials can be loaded in to connect to specific databases

### Subsection 1.2 - Connect to Database
There is a function to extract data from the database and return is as a dataframe 

## Section 2 - Convert datatypes in the Dataframe
The class DataTransform handles conversion of columns in the dataframe to different datatypes/formats such as date, string and numeric 

## Section 3 - Extract information from the dataframe
The class DataFrameInfo allows information to be gained about the data 

### Subsection 3.1 - Extract information from the dataframe
Functions allow the user to extract information about the dataframe e.g. statistical values: mean, median, mode, unique values, count of nulls and the shape of the dataframe 

## Section 4 - Dataframe Transformations
The class DataFrameTransform allows transformations to be performed on a dataframe

### Subsection 4.1 - Dataframe Transformations
Count null function is inherited from the DataFrameInfo class 

### Subsection 4.2 - Dataframe Transformations
Functions allow the user to perform transformations such as drop rows and columns containing null values and imputing values using the mean and median

### Subsection 4.3 - Dataframe Transformations
Functions allow data to be transformed to normal distribution such as log_transformation, boxcox and yeojohnson

### Subsection 4.4 - Dataframe Transformations
Z-Scores function allows the user to test for outliers in the dataset and remove the outliers 

### Subsection 4.5 - Dataframe Transformations
The correlation_heatmap functions shows the highly correlated columns in the dataframe to asist the user in dropping correlated columns 

### Section 5 - Dataframe Plots
The class Plotter allows the dataframe to be plotted on various charts 

### Subsection 5.1 - Plots
The histogram and QQ plot functions display the distribution of the data allowing the user to see if it is normally distributed 

### Subsection 5.2 - Data Transformations
The class inherits transformation functions from DataFrameTransform so that once the data has been visualised it can be transformed with the appropriate transformation

