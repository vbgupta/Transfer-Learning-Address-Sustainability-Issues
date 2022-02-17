# DS440-Transfer-Learning-Address-Sustainability-Issues
PSU DS440 Capstone Project Repository

### Tools For Database Management
* Install Git Large File Storage (LFS)
![image][https://git-lfs.github.com/images/graphic.gif|width=100px]



This is an open source Git extension for versioning large files. It will help us upload datasets to GitHub.
Download and install the Git command line extension. Once downloaded and installed, set up Git LFS for your user account by running:

`git lfs install`
You only need to run this once per user account.
[Full instruction can be found here.](https://git-lfs.github.com/)

* Exploring [Microsoft Azure SQL](https://azure.microsoft.com/en-us/products/azure-sql/database/)
Azure SQL Database is an always-up-to-date relational database service built for the cloud. 
Download [Azure Data Studio](https://docs.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio?view=sql-server-ver15#download-azure-data-studio).

Azure Data Studio is a cross-platform database tool for data professionals who use on-premises and cloud data platforms on Windows, macOS, and Linux. Use Azure Data Studio to query, design, and manage your databases and data warehouses wherever they are, on your local computer or in the cloud.

*@Vaibhav and @Ally have been added to the shared resource. I will share server link via email. Please create an Azure Account using PSU ID and accept request to join Resource Group. Navigate to `prediction` SQL Database.*

### Tools For Exploratory Data Analysis (EDA)
Use packages to automate EDA of datasets. Please read *References* to explore other available tools for data exploration.

For Primary Analysis
* (R) [DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/vignettes/dataexplorer-intro.html)
* (Python) [Pandas-Profiling](https://pypi.org/project/pandas-profiling/)

References
* (R) [4 R-Packages For Automated EDA by Towards Data Science](https://towardsdatascience.com/four-r-packages-for-automated-exploratory-data-analysis-you-might-have-missed-c38b03d4ee16#aba1)
* (Python) [4 Libraries To Perform EDA in One Line of Python Code by Towards Data Science](https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae)

### Interim Github Instructions
* Please create your individual branch for committing changes. 
* Create a [pull request to merge your commits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) onto `master`.

### Set Up Environment
* Download `Anaconda Navigator` to install essential Python and R libraries. 
* Refer to [Anaconda Navigator Cheatsheet](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf) to follow best-practices.

### Accessing AQI in R - Package
https://cran.r-project.org/web/packages/RAQSAPI/index.html
walk through -> https://github.com/USEPA/RAQSAPI

### Accessing Open Data Datasets in R
Install [RSocrata in R](https://github.com/Chicago/RSocrata) to retrieve datasets from Open Data. 

To get the current released version from CRAN:
```
install.packages("RSocrata")
```

The most recent beta with soon-to-be-released changes can be installed from GitHub:
```
# install.packages("devtools")
devtools::install_github("Chicago/RSocrata")
```
Mapping spatial data using `Leaflet` 
* Use GeoJSONs as explained [here](https://dev.socrata.com/docs/formats/geojson.html).

