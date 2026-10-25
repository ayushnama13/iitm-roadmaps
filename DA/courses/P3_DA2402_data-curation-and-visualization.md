# DA2402 — Data Curation and Visualization

| | |
|---|---|
| Tier | A |
| Phase (order) | 3 |
| Do this first | DA1301 |
| Estimated effort | 8 weeks |
| Unlocks | DA3406, DA5500W |

## Roadmap

1. Collection, cleaning (missing values, outliers), wrangling (groupby, pivot, merge, time series).
2. Visual design principles; Matplotlib/Seaborn/Plotly dashboards.

## Video courses (all links checked on YouTube on 2026-10-22)

### 🎓 Main course: follow it start to end

- [Data Science for Engineers | IIT Madras](https://www.youtube.com/playlist?list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0) (50 videos). NPTEL *Data Science for Engineers* (IIT Madras): data handling, stats, regression, clustering, in R.

### 🎥 Other full lecture series (pick one if the main one doesn't click, or for topics it skips)

- [Pandas Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) (11 videos). Corey Schafer *Pandas Tutorials*: loading, cleaning, grouping and reshaping real data.
- [Matplotlib Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) (10 videos). Corey Schafer *Matplotlib Tutorials*.
- [Data Analysis with Python Course](https://www.youtube.com/playlist?list=PLWKjhJtqVAblvI1i46ScbKV2jH1gdL7VQ) (6 videos). freeCodeCamp *Data Analysis with Python*.
- [Building Data Apps in Python - Plotly Dash](https://www.youtube.com/playlist?list=PLYD54mj9I2JevdabetHsJ3RLCeMyBNKYV) (7 videos). Plotly *Building Data Apps in Python (Dash)* (official): interactive dashboards.

## Study plan (week by week)

Lecture numbers are positions in the main playlist above. Click a number to open that video.

| Week | Lectures | What to do |
|---|---|---|
| 1 | [1](https://www.youtube.com/watch?v=MTjOuCbdBCo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=1)–[11](https://www.youtube.com/watch?v=t4bTmlZLfaw&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=11) | R basics: data types, data frames, functions, control flow, plotting. (You may do the same work in Python/pandas.) |
| 2 | [12](https://www.youtube.com/watch?v=ehwt18bt3h8&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=12)–[18](https://www.youtube.com/watch?v=tztdsBUiGHo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=18) | Linear algebra for data science. |
| 3 | [19](https://www.youtube.com/watch?v=KqlKCO9X9VI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=19)–[22](https://www.youtube.com/watch?v=8oNGkvuRP60&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=22) | Statistical modelling, random variables, sample statistics, hypothesis testing. |
| 4 | [23](https://www.youtube.com/watch?v=LpamajnMpZY&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=23)–[28](https://www.youtube.com/watch?v=IgTzPczE14I&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=28) | Optimisation: unconstrained, gradient descent, equality and inequality constraints. |
| 5 | [29](https://www.youtube.com/watch?v=YUrbUOcZcB8&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=29)–[40](https://www.youtube.com/watch?v=MnBUgv7yYnM&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=40) | Data science process, linear regression, model assessment, diagnostics, cross-validation, multiple regression. Do a regression project on a real dataset. |
| 6 | [41](https://www.youtube.com/watch?v=32M5v9jJtJ0&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=41)–[50](https://www.youtube.com/watch?v=udtfDr5idi4&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=50) | Classification: logistic regression, performance measures, kNN, k-means. Do a Kaggle classification task end to end. |

<details>
<summary>All lectures in <i>Data Science for Engineers | IIT Madras</i> (50 videos)</summary>

1. [Data science for engineers Course philosophy and expectation](https://www.youtube.com/watch?v=MTjOuCbdBCo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=1)
2. [Introduction to R](https://www.youtube.com/watch?v=pJj1T35kaGo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=2)
3. [Introduction to R (Continued)](https://www.youtube.com/watch?v=Rftn5XkYAhk&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=3)
4. [Variables and datatypes in R](https://www.youtube.com/watch?v=GM4D2Z-5TU4&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=4)
5. [Data frames](https://www.youtube.com/watch?v=RR46Nw8nLL0&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=5)
6. [Recasting and joining of dataframes](https://www.youtube.com/watch?v=SrhKWcrnzBk&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=6)
7. [Arithmetic,Logical and Matrix operations in R](https://www.youtube.com/watch?v=2zZxsiOfhxY&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=7)
8. [Advanced programming in R : Functions](https://www.youtube.com/watch?v=vwMltOwTPBA&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=8)
9. [Advanced Programming in R : Functions (Continued)](https://www.youtube.com/watch?v=AWca3GD7m7Y&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=9)
10. [Control structures](https://www.youtube.com/watch?v=7RHnRMQn5Go&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=10)
11. [Data visualization in R Basic graphics](https://www.youtube.com/watch?v=t4bTmlZLfaw&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=11)
12. [Linear Algebra for Data science](https://www.youtube.com/watch?v=ehwt18bt3h8&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=12)
13. [Solving Linear Equations](https://www.youtube.com/watch?v=vEf0vry_UaA&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=13)
14. [Solving Linear Equations ( Continued )](https://www.youtube.com/watch?v=bnRTwPur4PU&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=14)
15. [Linear Algebra - Distance,Hyperplanes and Halfspaces,Eigenvalues,Eigenvectors](https://www.youtube.com/watch?v=nMtNPiRzd8Q&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=15)
16. [Linear Algebra  - Distance,Hyperplanes and Halfspaces,Eigenvalues,Eigenvectors ( Continued 1)](https://www.youtube.com/watch?v=NzGKuQ7afR8&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=16)
17. [Linear Algebra - Distance,Hyperplanes and Halfspaces,Eigenvalues,Eigenvectors ( Continued 2 )](https://www.youtube.com/watch?v=yOtFCa9Naxo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=17)
18. [Linear Algebra  - Distance,Hyperplanes and Halfspaces,Eigenvalues,Eigenvectors ( Continued 3 )](https://www.youtube.com/watch?v=tztdsBUiGHo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=18)
19. [Statistical Modelling](https://www.youtube.com/watch?v=KqlKCO9X9VI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=19)
20. [Random Variables and Probability Mass/Density Functions](https://www.youtube.com/watch?v=Hnq0Gj0H5FQ&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=20)
21. [Sample Statistics](https://www.youtube.com/watch?v=Tg5V-11YIqc&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=21)
22. [Hypotheses Testing](https://www.youtube.com/watch?v=8oNGkvuRP60&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=22)
23. [Optimization for Data Science](https://www.youtube.com/watch?v=LpamajnMpZY&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=23)
24. [Unconstrained Multivariate Optimization](https://www.youtube.com/watch?v=bMEmJMI3ViE&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=24)
25. [Unconstrained Multivariate Optimization ( Continued )](https://www.youtube.com/watch?v=BdTEKVELwQg&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=25)
26. [Gradient ( Steepest ) Descent ( OR ) Learning Rule](https://www.youtube.com/watch?v=mMHR4iEswTU&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=26)
27. [Multivariate Optimization With Equality Constraints](https://www.youtube.com/watch?v=W5W9krjFrNE&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=27)
28. [Multivariate Optimization With Inequality Constraints](https://www.youtube.com/watch?v=IgTzPczE14I&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=28)
29. [Introduction to Data Science](https://www.youtube.com/watch?v=YUrbUOcZcB8&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=29)
30. [Solving Data Analysis Problems - A Guided Thought Process](https://www.youtube.com/watch?v=I48yqXg2PBo&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=30)
31. [Module : Predictive Modelling](https://www.youtube.com/watch?v=_KNDrnLILFI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=31)
32. [Linear Regression](https://www.youtube.com/watch?v=sg_qvRl9gAI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=32)
33. [Model Assessment](https://www.youtube.com/watch?v=KvhEifwVxrE&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=33)
34. [Diagnostics to Improve Linear Model Fit](https://www.youtube.com/watch?v=5fJjWU7ovac&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=34)
35. [Simple Linear Regression Model Building](https://www.youtube.com/watch?v=ce3xsqy1qZU&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=35)
36. [Simple Linear Regression Model Assessment](https://www.youtube.com/watch?v=jQl10n_2iQI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=36)
37. [Simple Linear Regression Model Assessment ( Continued )](https://www.youtube.com/watch?v=cSPJDO1RlaM&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=37)
38. [Muliple Linear Regression](https://www.youtube.com/watch?v=I6AVFwkAMJc&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=38)
39. [Cross Validation](https://www.youtube.com/watch?v=jtZfCpo0858&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=39)
40. [Multiple Linear Regression Modelling Building and Selection](https://www.youtube.com/watch?v=MnBUgv7yYnM&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=40)
41. [Classification](https://www.youtube.com/watch?v=32M5v9jJtJ0&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=41)
42. [Logisitic Regression](https://www.youtube.com/watch?v=H4986KDZkeI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=42)
43. [Logisitic Regression ( Continued )](https://www.youtube.com/watch?v=lIHDgiluhQ8&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=43)
44. [Performance Measures](https://www.youtube.com/watch?v=Sowy3iZyRVk&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=44)
45. [Logisitic Regression Implementation in R](https://www.youtube.com/watch?v=y4n92JEvjtM&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=45)
46. [K - Nearest Neighbors (kNN)](https://www.youtube.com/watch?v=2ATqoglcHus&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=46)
47. [K - Nearest Neighbors implementation in R](https://www.youtube.com/watch?v=3kKBbR94Z9M&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=47)
48. [K - means Clustering](https://www.youtube.com/watch?v=ZTP6b3LaVGg&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=48)
49. [K - means implementation in R](https://www.youtube.com/watch?v=xZxjebqLnbI&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=49)
50. [Data Science for engineers - Summary](https://www.youtube.com/watch?v=udtfDr5idi4&list=PLyqSpQzTE6M-Rf2y3MT5aZ1UpTF1UQBK0&index=50)

</details>


## Books, notes and websites

- Book: McKinney, *Python for Data Analysis* (free online)
- Knaflic, *Storytelling with Data*
- pandas and Plotly docs; Kaggle *Data Cleaning* course
- ✅ Nearest NPTEL match: *Data Science for Engineers* (Rengasamy & Narasimhan, IIT Madras) — nptel.ac.in/courses/106106179. NPTEL has no dedicated data-visualization course, so this covers only part of it.

## Practice / proof of understanding

Clean a messy public dataset and ship a 5-chart story (notebook + short report).

## What your IITM course sheet says

### From the PDF: DA2402

**Official description:** By the end of the course, students will be able to:  • Describe and implement the steps involved in data curation (collection, cleaning &; wrangling)  • Understand core principles of effective data visualization  • Create static and interactive charts  • Design and build interactive dashboards

**Official syllabus (trimmed):**

> 1. Module 1: Introduction to Data Curation: Importance of data curation Data acquisition and collection Data
>  lifecycle management Data governance & compliance;
>  2. Module 2: Data cleaning methods: Types of data (quantitative, categorical, temporal etc) Common data
>  quality issues Handling missing data Outlier detection and treatment methods Handling other data inconsistencies
>  3. Module 3: Data wrangling techniques: Data summarization (Groupby, Pivot) Data reshaping (melting, stack-
>  ing) Data integration from multiple sources Working with time series data
>  4. Module 4: Introduction to Data Visualization: Importance of data visualization Application across industries
>  Types of charts Python visualization libraries overview (Matplotlib, plotly, seaborn) Introduction to grammar of
>  graphics Types of analysis (univariate, bivariate, multivariate)
>  5. Module 5: Standard visualization charts: Charts for statistical analysis (box plots, histograms etc) Univariate
>  & Bivariate analysis (Distribution analysis, Frequency analysis, Trending analysis)
>  6. Module 6: Advanced charts: Understanding multi-variate analysis Charts for Hierarchical analysis (stacked
>  bars, Treemaps, Sunburst) Geographical analysis (Maps) Text analysis (word clouds) Visualizing time series data
>  7. Module 7: Building interactive dashboards using Python: Designing a dashboard Adding filters for inter-
>  activity C

**Official textbooks:** 1. Iliinsky, N., & Steele, J. (2011). Designing data visualizations: Representing informational relationships. O’Reilly  Media.  2. Knaflic, C. N. (2015). Storytelling with data: A data visualization guide for business professionals. Wiley.  3. McKinney, W. (2022). Python for data analysis: Data wrangling with Pandas, NumPy, and Jupyter (3rd ed.).  O’Reilly Media.

**Official references:** 1. Iliinsky, N., & Steele, J. (2011). Designing data visualizations: Representing informational relationships. O’Reilly  Media.  2. Knaflic, C. N. (2015). Storytelling with data: A data visualization guide for business professionals. Wiley.  3. McKinney, W. (2022). Python for data analysis: Data wrangling with Pandas, NumPy, and Jupyter (3rd ed.).  O’Reilly Media.
