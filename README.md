
- **driver/driver.py**: Contains the WebDriver setup and configuration.
- **pages/search.py**: Contains the `Search` class that encapsulates the search functionality.
- **test/test_search.py**: Contains the `TestSearch` class with various test cases.
- **README.md**: Project documentation.

## Installation

1. **Clone the repository**:
    git clone <https://github.com/d2inthenow/SoftWareTesting.gitl>
    cd assignment2


2. **Install the dependencies**:

    pip install selenium
    pip install pytest
    pip install pytest-html

## Running the Tests

1. **Navigate to the project directory**:
    
    cd assignment2

2. **Run the tests using PyTest**:
    pytest filetest

## Test Cases

## `test_search`

- **Purpose**: Verifies that searching for the term "macbook" returns the correct URL.
- **Expected Result**: The current URL contains 'product/search&language=en-gb&search=macbook'.

### `test_search_empty`

- **Purpose**: Checks the behavior when an empty search term is used.
- **Expected Result**: The current URL contains 'product/search&language=en-gb'.

### `test_search_not_exist`

- **Purpose**: Verifies the behavior when a non-existent product is searched.
- **Expected Result**: The message indicates no products match the search criteria.

### `test_search_sql_injection`

- **Purpose**: Checks for SQL injection vulnerabilities by using a SQL query as the search term.
- **Expected Result**: The message indicates no products match the search criteria.

### `test_validate_search_xss`

- **Purpose**: Checks for XSS vulnerabilities by using a script tag as the search term.
- **Expected Result**: The message indicates no products match the search criteria.

### `test_add_to_cart_single`

- **Purpose**: Tests adding a single product to the cart.
- **Expected Result**: The cart contains the single added product.

### `test_add_many_products`

- **Purpose**: Tests adding multiple different products to the cart.
- **Expected Result**: The cart contains both added products.

### `test_add_to_cart_zero`

- **Purpose**: Tests adding zero quantity of a product to the cart.
- **Expected Result**: The cart does not contain the product.

### `test_responsive`

- **Purpose**: Verifies that the website is responsive and displays correctly on different screen sizes.
- **Expected Result**: The layout adjusts correctly for mobile, tablet, and desktop views without any overlapping or hidden elements.

### `test_register`

- **Purpose**: Tests the user registration functionality.
- **Expected Result**: A new user can successfully register, and the system redirects to the welcome page or dashboard.

### `test_navigation`

- **Purpose**: Verifies that the navigation links work correctly.
- **Expected Result**: Clicking on navigation links redirects to the correct pages without any errors.

### `test_login`

- **Purpose**: Tests the user login functionality.
- **Expected Result**: A registered user can successfully log in, and the system redirects to the user dashboard.

### `test_datavalidation`

- **Purpose**: Checks the data validation for forms (e.g., registration, login).
- **Expected Result**: The system displays appropriate error messages for invalid inputs and prevents form submission.

### `test_checkout`

- **Purpose**: Tests the checkout process.
- **Expected Result**: A user can successfully complete a purchase, and the system processes the order correctly.

### `test_addtocart`

- **Purpose**: Verifies that products can be added to the shopping cart.
- **Expected Result**: A user can add products to the cart, and the cart updates correctly with the added items.

## Contributing

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Create a new Pull Request**.

## License

This project is licensed under the MIT License - see the LICENSE file for details.