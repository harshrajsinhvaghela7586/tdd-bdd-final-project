Feature: Product Management UI
  Background:
    Given the following products
      | name  | description    | price | available | category |
      | Hat   | A red fedora   | 59.95 | True      | Cloths   |
      | Shirt | Blue cotton    | 29.99 | True      | Cloths   |
      | Ball  | Soccer ball    | 19.99 | False     | Toys     |
      | Book  | Python guide   | 39.99 | True      | Books    |
      | ToyCar| Small toy car  | 9.99  | True      | Toys     |

  # -------------------- READ --------------------
  Scenario: Read a Product
    When I start on the "Home Page"
    And I set "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red fedora" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "Cloths" in the "Category" dropdown
    And I should see "59.95" in the "Price" field

  # -------------------- UPDATE --------------------
  Scenario: Update a Product
    When I start on the "Home Page"
    And I copy the "Id" field for "Hat"
    And I set "Description" to "A stylish red fedora"
    And I press the "Update" button
    Then I should see the message "Success"
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "A stylish red fedora" in the "Description" field

  # -------------------- DELETE --------------------
  Scenario: Delete a Product
    When I start on the "Home Page"
    And I copy the "Id" field for "Shirt"
    And I press the "Delete" button
    Then I should see the message "Success"
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Not Found"

  # -------------------- LIST ALL --------------------
  Scenario: List all Products
    When I start on the "Home Page"
    And I press the "List All" button
    Then I should see "Hat" in the "Name" field
    And I should see "Shirt" in the "Name" field
    And I should see "Ball" in the "Name" field
    And I should see "Book" in the "Name" field
    And I should see "ToyCar" in the "Name" field

  # -------------------- SEARCH BY NAME --------------------
  Scenario: Search by Name
    When I start on the "Home Page"
    And I set "Name" to "Ball"
    And I press the "Search" button
    Then I should see "Ball" in the "Name" field

  # -------------------- SEARCH BY CATEGORY --------------------
  Scenario: Search by Category
    When I start on the "Home Page"
    And I set "Category" to "Toys"
    And I press the "Search" button
    Then I should see "Ball" in the "Name" field
    And I should see "ToyCar" in the "Name" field

  # -------------------- SEARCH BY AVAILABILITY --------------------
  Scenario: Search by Availability
    When I start on the "Home Page"
    And I set "Available" to "True"
    And I press the "Search" button
    Then I should see "Hat" in the "Name" field
    And I should see "Shirt" in the "Name" field
    And I should see "Book" in the "Name" field
    And I should see "ToyCar" in the "Name" field
