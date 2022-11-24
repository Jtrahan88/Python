# ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `Python_To_PostgresSQL` 
> * Take our Cleaned data in python and send it to PostGress SQL_V1.0
> * [Source for helping set this up](https://www.youtube.com/watch?v=M2NzvnfS-hI)

### Goals: Send cleaned data to database in a dynamic way after our data has been cleaned.  
#### Important notes:
* Your database will need to be made in Posgress before running this.
* This will over write a pre-existing table. In my case I am over writing .GOV Data as it come in. Their API does not work currently.
#### Learning objectives:
* [Python convert Dataframe to list of tuples:](https://pythonguides.com/python-convert-dataframe-to-list/)
* [Youtube for sql updating:](https://www.youtube.com/watch?v=M2NzvnfS-hI)
* For/While Loop
* Slicing of strings
* Dynamic functions
* global varibale

## Below is the how and what is needed to connect to PostgreSQL database.


# ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `SQL_hosting - Will get the  following if not already connected.`
#### Prompts users for the following information:
> > * hostName = '' 
> > * database = '' 
> > * username = ''
> > * pwd = ''
> > * port_id = ''


## Will need to know to run on your system:
**Database needs to be created before this is ran.**
## Login to PosgresSQL host name inputs:
### Locations:
#### Right click host name (mine is PostgreSQL 13) and select properties -> connection. 
* host
* dbname 
#### Right click on pre-made database in PostgreSQL, click properties. 
* user
* password
* port

# ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `Table_Setup - This will add tables to posgress. This can be ran as many times as needed:`
* SQL hostname/etc needed?: 'Y' or 'N' n   -> this one ONLY needs to be ran ONCE if other tables are being made in the **SAME** database -see **SQL_hosting** above.
#### Prompts users for the following information:
* Number(#) of columns in table: 4 examples -> if less or more it will prompt for that number amount and whatever column names user provides.
> * Column 1 Name: Year 
> * Column 2 Name: Rates 
> * Column 3 Name: Brackets 
> * Column 4 Name: Notes 
> > * Data Type for Year in SQL syntax: 
> > * Data Type for Rates in SQL syntax: 
> > * Data Type for Brackets in SQL syntax: 
> > * Data Type for Notes in SQL syntax: 
