![banner](https://res.cloudinary.com/dloadb2bx/image/upload/v1704943653/python_rvcah5.png)
# Contact List App
This project belongs to the first challenge of the **[Rocketseat](https://www.rocketseat.com.br/)** specialization in Python and consists in a simple command-line contact management application that allows users to manage their contacts efficiently. The application offers various functionalities to add, view, edit, and delete contacts, as well as mark/unmark them as favorites.

To create a high level of challenges, I also added helper functions to ensure a more Don't Repeat Yourself (DRY) approach and bring this project closer to real-world scenarios. These helper functions contribute to the overall code quality, maintainability, and extensibility of the application. 

## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Helper Functions: Enhancing Code Readability and Reusability

In the Contact List App, the inclusion of helper functions serves as a crucial aspect of code optimization, promoting readability and reusability. The following helper functions have been thoughtfully implemented to streamline specific tasks within the application:

### `number_not_allowed(num)`

The `number_not_allowed` function is designed to notify users when an invalid choice is made. By encapsulating this functionality in a separate helper function, the code benefits from improved clarity and maintainability. This function reduces redundancy, ensuring consistent and informative messages when an unsupported option is selected.

### `phone_number_formatter(phone_number)`

The `phone_number_formatter` function showcases the importance of encapsulating complex logic for phone number formatting. This helper function efficiently cleans and formats the provided phone number, making the code more modular. Its usage ensures uniform formatting across the application, eliminating the need to repeat this logic whenever a phone number needs to be displayed.

### `formatted_index(index)`

The `formatted_index` function plays a key role in converting user input (index) into a format compatible with list indices. By subtracting 1 from the provided index, the function aligns with the zero-based indexing commonly used in programming languages. This abstraction simplifies index manipulation throughout the code, enhancing code consistency and reducing the likelihood of indexing errors.

### `formatted_contact(index, contact)`

The `formatted_contact` function consolidates the formatting logic for displaying contact details. By centralizing this presentation logic, the code becomes more readable and avoids duplication of formatting code. The inclusion of this helper function promotes a cleaner codebase and facilitates any future changes to the display format.

In summary, the use of these helper functions significantly contributes to the overall quality of the Contact Management App codebase. It fosters a modular structure, reduces redundancy, and enhances maintainability, making the application more adaptable to future modifications or feature additions.

## How to run this project?
1. On your terminal add:

	    git clone git@github.com:thiagohrcosta/Contact-List.git

2. Navigate to the project directory:

	    cd contact-list

3. Run the script

	    python app.py

 
