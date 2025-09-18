17-09-2025

what is self variable?
     In Python, the self variable is just a conventionally used name for the reference to the current instance (object) of the        class. When you create an object from a class, Python automatically passes that object as the first argument to any              instance method you call. By convention, we call that first parameter self.
     self represents "this object".It lets you access the attributes and methods of the object inside the class.

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
