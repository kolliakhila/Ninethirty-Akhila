17-09-2025


what is self variable?
     In Python, the self variable is just a conventionally used name for the reference to the current instance (object) of the        class. When you create an object from a class, Python automatically passes that object as the first argument to any              instance method you call. By convention, we call that first parameter self.
     self represents "this object".It lets you access the attributes and methods of the object inside the class.

03-09-2025

1.What is factorial of zero?
       0! = 1

2.What is palindrome and some examples:
           Palindrome : A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as  
                          forward.
                             Ex:  MADAM,LEVEL
                             
3. what is meaning of purge?
       Purge: Purge means to completely remove or clear stored data, memory, cache, or unwanted items, so that 
              nothing remains.

4. what is conflit?How do slove conflit?
       Conflict: A conflict happens when there is a disagreement, clash, or mismatch between two or more parties, ideas, or
                  actions.
       steps for solving conflicts:
                > Run git status to see which files have conflicts.
                > Open the conflicted file → Git will mark conflicts with <<<<<<<, =======, >>>>>>>.
                > Choose which version to keep (or merge both if needed).
                > Save the file after fixing it.
                > Run:
                   git add filename
                   git commit


18-09-2025

1. Why and When we use class method?
   Use of Class Methods: To work with class-level data (shared by all objects).They can access and modify class variables.Useful when you need methods that make sense for the
                         class as a whole, not just for one object.
   Class method is using in this situations: When you want to create alternative constructors (different ways of creating objects).When you need to perform actions that depend
                                             on the class, not on a single instance. When you want to keep logic tied to the class rather than making it a utility function.


2.Why and When we use static method?
  Use of Static Methods: They don’t need access to instance (self) or class (cls) variables.Useful for utility functions related to the class but not tied to any    
                         object.Keeps the method logically grouped with the class for better organization.
  Static Method using situations: When the method does some work related to the class but doesn’t need object data.
                                  For example, performing calculations, validations, or helper tasks.
                                  When you want a method inside a class for clarity, but it doesn’t need self or c

3. How can you access the static variables of outer calss from inner class?
     Using "OuterClassName.variable_name" we can access the static variables of outer class from inner class.

4. How can you access the instance variables of outer calss from inner class?
   Create an outer class with instance variables.Create an inner class inside the outer class.When creating the inner class object, pass the outer class object to it.Use
   that reference to access the instance variables.

19-09-2025

1.How will you know that classes,functions of that particular module?
   Using below handy tools we can know all that in a module: dir(module) → lists all attributes (names).
                                                             help(module) → shows docs.
                                                             inspect.getmembers(module, inspect.isfunction) → only functions.
                                                             inspect.getmembers(module, inspect.isclass) → only classes.

2.if __name__=="__main__": 
              It checks whether a Python file is being run directly or being imported into another file.
              When you run a Python file directly, Python sets the special variable __name__ to "__main__".
              When you import that file as a module into another program, __name__ will be set to the file’s name (not "__main__").

25-09-2025

1. What are the features of web applications?
     A web application is a software or program that runs in a web browser(chrome,firebox,Edge)
     Features:
         > Accessibility(runs in browser)
         > cross platform compatibility
         > User Interaction(dynamic content)
         > Database connectivity
         > Authentication and authorisation
         > Scalability
         > Updates are easy
         > Responsive design
         > security
         > Interaction with API's

2. What is OWASP?
     OWASP: Open Web Application Security Project.
     > It is a global community that provides best practices,tools and guide lines to secure web applications.
     > It also provides:
              Cheat Sheets → quick guides for secure coding
              ZAP Tool (OWASP Zed Attack Proxy) → used to test your app for security flaws
              Training materials → free documentation, videos, and community projects

3. What is HTTP,HTTPS,TCP/IP and UDP?
       HTTP,HTTPS,TCP/IP,UDP are protocols.
   HTTP: HyperText Transfer Protocol
         Used to transfer data between a brower(client side) to web server.It is a foundation of web communication.But it is          not secure because it sends data as plain text.
   HTTPS: HYperText Transfer Protocol Secure
          Same as HTTP,but secure- it encrypts all data between browser and server.
   TCP/IP: Transimission Control Protocol / Internet Protocol
           It defines how data travel from one computer to another. Its the foundation of entire internet.
           IP - Finds correct address
           TCP - Ensures the message is delivered safely and in right order.
   UDP: USer Datagram Protocol
        Sends data faster,but less reliable than TCP.It doesn't checks if packets arrive in order or if any are lost- it
        just sends them.It is used when speed is more important than accuracy.



   8-10-2025
   1.What is API Get, Put and Post?
         GET,PUT and POST are the HTTP Methods used in REST API.
      GET: Retrieve data.It only reads data and it doesn't change anything in database.
      PUT: Create new data.Used to send or create new data on the server.
      POST: Used to update or replace existing data on the server.

23-10-2025
1.Difference between RAM,ROM and BIOS?
   RAM: Random Access Memory,it’s the temporary memory of a computer.Stores data and instructions only while the computer is running.Volatile memory → data is lost when 
        power is off.Used for Running programs, games, or any task currently being done.RAM = short-term working memory.
        
   ROM: Read Only Memory,It’s the permanent memory of the computer.Stores the instructions required to start the computer (called firmware).Non-volatile memory → data is 
        not lost when power is off.Used for Storing programs that rarely change (like system boot instructions).ROM = permanent built-in memory that tells the computer how          to start.

  BIOS: Basic Input/Output System,It’s a small program stored inside ROM.Runs when the computer is turned on (called booting process).Checks and initializes hardware 
        (keyboard, mouse, hard drive, etc.).Then loads the operating system into RAM.BIOS = startup manager that helps the system boot and run properly.   

2.What is Automation Process?
   Automation is the process of making a system or task operate automatically using machines, software, or scripts.
   Automation often means writing scripts to:
                        Automatically handle data (read files, generate reports).
                        Test web applications (using tools like Selenium).
                        Manage servers or cloud resources (AWS automation).
                        Deploy apps automatically (CI/CD pipelines).
  Steps in an Automation Process:
                     Identify repetitive task → e.g., daily data entry.
                     Design workflow → how the process should happen.
                     Use tools or scripts → Python, Jenkins, Selenium, etc.
                     Test and monitor → ensure it works correctly.
                     Optimize → make it faster and more efficient.
 Benefits:
         Saves time and effort
         Reduces human errors
         Improves consistency
         Can run 24/7
         Increases productivity

3.What is the framework used to test the web application?
    In web application development, testing frameworks help check whether the app works correctly — both frontend and backend parts.
         1. Selenium (for Web UI Testing)
         2. Pytest (for Backend & API Testing)
         3. Postman (API Testing Tool)
         4. Unittest (Built-in Python Testing Framework)
         5. Cypress / Playwright (Modern Web Testing Tools)
         Cucumber is a testing framework used for Behavior Driven Development (BDD).

4.How can we calculate 1024?
   1 KB=1024 bytes
   Computers work in binary (base-2), so powers of 2 are very common.Computers use 1024 instead of 1000 because memory is binary-based, and powers of 2 (like 2¹⁰ = 1024)       fit perfectly with how data is stored and accessed.

5.What is difference between SQL,MySQL,PLSQL and DB2?
  SQL: Structured Query Language
      SQL is a standard language used to communicate with databases.
      It is not software, but a language used to perform tasks like:
                                                Create databases and tables
                                                Insert, update, and delete data
                                                Retrieve data using queries

 MySQL: MySQL is a database management system (DBMS) — a software that uses SQL to store, organize, and retrieve data.
       It is open-source and very popular in web development (used with PHP, Python, Node.js, etc.).

 PLSQL : Procedural Language SQL
        PL/SQL is an extension of SQL used by Oracle Database.
        It adds programming features like loops, conditions, and variables — so you can write stored procedures, triggers, and functions.

 DB2: DB2 is a Relational Database Management System (RDBMS) developed by IBM.
     It also uses SQL but is known for high performance and scalability, often used in large enterprises and banking systems. 

6.What is connection and connection pooling?
  Connection:
            A connection is a link between your application (like Python code) and the database (like MySQL, PostgreSQL, etc.) that allows data exchange.
            When your program wants to:
                              Fetch data (SELECT)
                              Add data (INSERT)
                              Update data (UPDATE)
                              Delete data (DELETE)
            …it first needs to open a connection to the database server.

Connection Pooling:
             Connection Pooling is a technique to reuse existing database connections instead of opening and closing new ones every time.
             It keeps a pool (collection) of open connections that can be shared by multiple users or requests.Pool keeps 3 active connections ready.
             No need to create a new one each time.

7.what is apllication server in cloud computing?
           In cloud computing, an application server is a server that runs and manages your application’s logic and services — it acts as the middle layer between the     
           frontend (user interface) and the backend database.
                    When a user opens a website or app:
                                       The frontend (browser/app) sends a request.
                                       The application server processes it — runs the backend code (like Python, Java, Node.js).
                                       Then it connects to the database to fetch or store data and sends a response back to the user.

8.What is open source contribution,importance and how to contribute?
  Open source:   Open Source means that the source code of a software project is publicly available for anyone to:
                                              View 
                                              Modify 
                                              Distribute 
                                              Contribute 
 Open source contribution: Open Source Contribution means helping improve public projects in any way — not just coding!
                           You can contribute by:
                                        Fixing bugs 
                                        Adding new features 
                                        Improving documentation 
                                        Translating content 
                                        Testing code 
                                        Helping other developers in discussions
Importance:
        Builds Your Resume: Recruiters love open-source contributors — it shows teamwork and practical skills.
        Improves Skills: You learn real-world coding standards, version control (Git), and collaboration tools.
        Networking:	You meet developers globally and build professional connections.
        Learn from Experts:	You can read high-quality code written by experienced engineers.
        Gives Confidence:	Your code becomes part of something used by thousands of people!
Contribute to open source:
         Step 1: Learn Git & GitHub-
                          Create a GitHub account: https://github.com
                          Learn basic commands:
                                           git clone
                                           git add
                                           git commit
                                           git push
                                           git pull
                                           git status
         Step 2: Find a Beginner-Friendly Project-
                           Search using:
                                       https://goodfirstissue.dev
                                       https://github.com/explore
                                       Look for tags like: “good first issue”, “beginner”, or “help wanted”
         Step 3: Understand the Project -
                           Read the README.md file (it explains what the project does).
                           Explore the issues tab to see what problems need fixing.
         Step 4: Fork and Clone -
                         Fork → make your own copy of the project.
                         Clone → download it to your system.
                         git clone https://github.com/your-username/project-name.git
         Step 5: Make Your Changes -
                         Create a new branch:
                                     git checkout -b my-fix
                                     Fix a bug or add a feature.
                                     Commit your changes:
                                                  git commit -m "Fixed typo in README"
         Step 6: Push & Create Pull Request (PR) -
                         Push your branch:
                                    git push origin my-fix
                                    Go to GitHub → Click “Compare & Pull Request” → Submit your PR.

9. Differences of Var and Varchar
     VarChar: VARCHAR (short for variable character) is a variable-length data type.
              When you declare a column as VARCHAR(n), it can store up to n characters.
              It uses only the required space — no padding.
     Var: There is no standard SQL data type called VAR
          However:
              Some systems (like MS Access) or programming contexts may use VAR as a shorthand or variable name.
              In databases, when you say VAR, you almost always mean VARCHAR.

10.Differences between SQL and NoSql?
  SQL: SQL stands for Structured Query Language.
       It is used in relational databases (RDBMS) — where data is stored in tables (rows & columns) with relationships between them.
                Examples:
                      MySQL
                      PostgreSQL
                      Oracle
                      Microsoft SQL Server
       Data is structured, related, and follows a strict schem
  NoSQL: NoSQL stands for Not Only SQL.
         It is used for unstructured or semi-structured data — no fixed table format, and no strict schema.
                                  Examples:
                                        MongoDB
                                        Cassandra
                                        Redis
                                        CouchDB
                                        Firebase
          Data is stored as documents (JSON-like), key-value pairs, or graphs.


3-11-2025

1. What is Database?
  Database:
          A database is an organized collection of data that is stored and managed electronically on a computer.
          It allows you to store, retrieve, update, and delete data easily and efficiently.

2. How many types of Databases?
   Different kinds of Databases are there like:
            > Relstional Database(RDBMS)
            > Non-Relational Database
            > Hierarchical Database
            > Network Database
            > ObjectOriented Database
            > Timeseries Database
            > Distributed Database
            > Graph Database
            > Cloud Database
            > Key-value Database

3. What is UML?
   UML (Unified Modeling Language) is a visual modeling language used to design and represent the structure and behavior of
   a software system before actually coding it.
   It is used for:
      To visualize how the system works.
      To communicate ideas between developers, designers, and clients.
      To plan database structures and API designs before implementation.
   UML → “Draw before you build” (visual design of system).

5. What is Schema?
   A Schema is the structure or blueprint of how data is stored in a database.
      It defines the organization of data.
      Ensures consistency and validation of data.
      Helps developers understand the data model quickly.
   Schema → “Blueprint of your database” (how data is stored).
     
    
  
       
  
    

