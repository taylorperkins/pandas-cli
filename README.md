# pandas-cli
Pandas CLI!
Note that this project is still in it's infant stages, and there are not many bells and whistles.. __yet..__

Big thanks to [pandas](https://pandas.pydata.org/) for such an incredible tool, and [PyInquirer](https://github.com/CITGuru/PyInquirer) for your innovative solutions to a beautiful CLI.

### The Problem
I am personally really passionate about finding ways to bridge the gap between software engineering and data science.
Being a part of the data science community while working as a data analyst/software engineer, I see this gap becoming more evident all the time. 

So what am I trying to solve?

1. First and foremost.. Create a tool that holds your hand through the dirty work of _cleaning data_.

This is always such a chore, consuming ~70% of your time as a data scientist. 
Rather than spinning up jupyter notebook and playing around with the data for hours, I want a nice interface that holds my hand through the process. 
How does the data need to be read in? 
CSV? JSON? Excel?
What are the arguments for those functions? 
What does my data look like?

On reading in the data.. 
Can I get a nice breakdown of the columns I specify?
Is there a way to automatically determine column types?
How about renaming?
Subsetting?

These are all parts of the process that are _required_ and _redundant_. 
I hope to at least relieve some of the pains of this process with pandas-cli.

2. Save my process.

A current challenge in data science is version control, especially through jupyter notebook. 
No one wants to read through a 2000+ diff on an `.ipynb` just because an svg has changes and it is saved in the json. 
As I slice and dice my data, I want to keep track of my progress, have the ability to replicate it, and allow other developers to _easily_ contribute to it.

3. Import to jupyter notebook / console.

At the end of the day.. I still love jupyter.
I still want to create some graphs, find correlations, and do some ml. 
The ability to go from `pandas-cli` to a jupyter notebook and seamlessly pick up where I started is a **must have**.


### What next?
This project lives on!! 
I welcome any and all help. 
Please reach out for any questions you may have about the useage, and _please_ *__please__* reach out for suggestions on how to make this better. 
Thanks in advance!


### Running Locally
* `git clone <project url>`
* Create virtualenv of your choice, and `pip install -r requirements.txt` (will make package later)
* `python main.py`

#### Current Features

* Create
    - Read in a file and save it as a dataframe.
    - You are able to specify file type
    - Arguments are shows as a dropdown, specific to the method chosen (example, `pd.read_csv`)
    - Args are required, kwargs are optional
