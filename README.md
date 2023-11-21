###**Project Overview**  
This project showcases the implementation of design patterns, including Singleton, Strategy, Adapter, Decorator, Factory, and Observer patterns. Each pattern contributes to different aspects of the clothing store application.  

#**Singleton Pattern**  
The Singleton pattern is utilized for user authentication. Upon logging in, the Singleton ensures that only one instance of the authentication process is active. User credentials (username and password) are verified securely.

#**Strategy Pattern**  
The Strategy pattern is applied to clothing categories. Users can select from four strategies: women, men, kids, and sports. Each strategy defines a unique approach to handling and displaying clothing items within its category.

#**Adapter Pattern**  
The Adapter pattern is employed to adapt and convert currency. Prices are adapted to the local currency (Tenge), converting from dollars. This ensures a seamless experience for users irrespective of their local currency.

#**Decorator Pattern**  
The Decorator pattern enhances the project with dynamic discounts using the DiscountDecorator class. This decorator allows the application to apply diverse discounts to each clothing item dynamically, providing flexibility in discount management.

**Factory Pattern**  
The Factory pattern is implemented through the ClothingStrategyFactory class. It instantiates clothing strategies based on user data, ensuring a systematic and organized approach to strategy creation.

**Observer Pattern**
The Observer pattern establishes a one-to-many dependency between objects. The ClothingStore acts as an Observable, and the ClothingStoreObserver is notified about catalog updates. This pattern ensures that changes in the store's catalog state are automatically reflected in all dependent observers.
