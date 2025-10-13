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

   
   
     

