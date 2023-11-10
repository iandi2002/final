This project implements the Singleton, Strategy, Adapter patterns. 
Using the Singleton template, the user logs in and the username and password are verified. 
The Strategy template allows the program to implement four strategies. The user needs to select a clothing category: women's, men's, children's, sports. 
The adapter template adapts the price and converts dollars to tenge.
In this project, the Decorator pattern is implemented using the DiscountDecorator class. This decorator  applies dynamic and varied discounts to each item of clothing.
The Factory pattern instantiates clothing strategies based on user data.  In this project, the Factory pattern is implemented with the ClothingStrategyFactory class.
The Observer pattern is used to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. In this project, the Observer and Observable classes are used to implement the Observer pattern. ClothingStore acts as an Observable, and ClothingStoreObserver is an Observer that receives notifications about catalog updates.
