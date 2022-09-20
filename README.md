# Candy Statistics
> This program was created to practice data-cleaning CSV (Excel) files and web-scraping online data through Python.

## Table of Contents
* [General Info](#general-information)
* [Resources Used](#resources-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- This program is intended to enable users to easily compare statistics of 50+ common candy preferences from a 2017 survey. I chose to take up this project to help improve my skills at data-scraping websites and excel files while also teaching myself how to clean this data and how to utilize two common Python libraries; pandas and beautifulsoup.


## Resources Used
- Visual Studio Code 1.71.2
- Junk Food Blog, A-Z Alphabetical Candy List (https://junkfoodblog.com/alphabetical-candy-list/)
- BoingBoing, The 2017 Halloween Candy Hierarchy (https://boingboing.net/2017/10/30/the-2017-halloween-candy-hiera.html. File included.)


## Features
After organizing the column titles and filtering only candy, allows the user to type which statistics they would like to view before displaying the results. Each result shows:
#### General breakdown of specific candy preferences.
- Total (& percent) of people who enjoy the candy.
- Total (& percent) of people who are indifferent to the candy.
- Total (& percent) of people who dislike the candy.
#### Gender breakdown of specific candy preferences. (Added in version 1.2)
- M/F breakdown of people who enjoy the candy.
- M/F breakdown of people who are indifferent to the candy.
- M/F breakdown of people who dislike the candy.


## Setup
1. Download 'Candy Cleaning - Aine Bolton.py'
2. Download 'candyhierarchy2017.csv'
2. Open 'Candy Cleaning - Aine Bolton.py' and run in prefered development software (I used Visual Studio Code).


## Usage
Upon running the code, it should take five to ten seconds to load before asking you to enter a candy. Enter the candy that you would like to search for. Results are not case-sensative and should be able to detect minor errors.
- Example: User enters 'Sweethearts'.
- Result: Computer uses fuzzy comparison to locate and return statistics for 'SweeTarts'.


## Project Status
Project is: In-Progress


## Room for Improvement
In the future, I plan to extend the amount of statistics reported for each candy as well as to add/fix candies that are currently unavailable due to either errors within the code or are presented as multiple variations of one candy type.

### To-do Candy Additions:
- Bonkers, Cadburry Creme Eggs, Chick-o-Sticks, Good N' Plenty, Hershey's Milk Chocolate, Jolly Ranchers (multiple variations), M&Ms (multiple variations), Kinder, Licorice (multiple variations), Mint Kisses, Mint Juleps, Now & Laters, Reese’s Pieces, Reggie Jackson Bar, Sweetums, & Three Musketeers.

### To-do Statistic Features:
#### Age breakdown of specific candy preferences.
- Average age of people who enjoy the candy.
- Average age of people who are indifferent to the candy.
- Average age of people who dislike the candy.

#### Regional breakdown of specific candy preferences.
- Country with the highest percentage of people who enjoy the candy.
- Country with the highest percentage people who are indifferent to the candy.
- Country with the highest percentage of people who dislike the candy.
- (US) State with the highest percentage of people who enjoy the candy.
- (US) State with the highest percentage people who are indifferent to the candy.
- (US) State with the highest percentage of people who dislike the candy.
- (Other) Province with the highest percentage of people who enjoy the candy.
- (Other) Province with the highest percentage people who are indifferent to the candy.
- (Other) Province with the highest percentage of people who dislike the candy.

#### General candy preferences.
- Total people who enjoy (chocolate/fruity) candy.
- Total people who are indifferent to (chocolate/fruity) candy.
- Total people who dislike (chocolate/fruity) candy.


## Acknowledgements
Give credit here.
- This project was inspired by Rachel Tatman at Making Noise and Hearing Things (https://makingnoiseandhearingthings.com/2018/04/19/datasets-for-data-cleaning-practice/).


## Contact
Created by [@bolton-a](https://github.com/Bolton-A) - feel free to contact me!
