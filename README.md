### API Documentation

#### Endpoints:

1. **Calculate Delivery Price:**
   - **URL:** `/calculate_delivery_price/`
   - **Method:** GET
   - **Description:** Calculate the delivery price based on provided parameters.
   - **Parameters:**
     - `zone` (string): The delivery zone.
     - `organization_id` (integer): The ID of the organization.
     - `total_distance` (integer): Total distance of delivery in kilometers.
     - `item_type` (string): Type of the item (perishable or non-perishable).
   - **Response:**
     - `total_price` (float): The calculated total delivery price.
   - **Errors:**
     - 400 Bad Request: Missing parameters or invalid values.
     - 404 Not Found: Pricing information not found.

#### Request/Response Formats:

1. **Request Format:**
   - **Method:** GET
   - **Headers:** No special headers required.
   - **Parameters:**
     - `zone` (string): The delivery zone.
     - `organization_id` (integer): The ID of the organization.
     - `total_distance` (integer): Total distance of delivery in kilometers.
     - `item_type` (string): Type of the item (perishable or non-perishable).

2. **Response Format:**
   - **Content Type:** JSON
   - **Success Response:**
     - **Code:** 200 OK
     - **Content:**
       ```json
       {
           "total_price": 17.5
       }
       ```
   - **Error Responses:**
     - **Code:** 400 Bad Request
       - **Content:** `{ "error": "Required parameters are missing: zone, organization_id, total_distance, item_type." }`
       - **Content:** `{ "error": "Invalid value for total_distance. Please provide a valid integer value." }`
     - **Code:** 404 Not Found
       - **Content:** `{ "error": "Pricing information not found" }`
     - **Code:** 405 Method Not Allowed
       - **Content:** `{ "error": "Only GET requests are allowed" }`

#### Error Handling:

- **400 Bad Request:** This error occurs when the required parameters are missing or contain invalid values. The response contains an error message indicating the missing or invalid parameters.
- **404 Not Found:** This error occurs when the pricing information is not found based on the provided parameters. The response contains an error message indicating that the pricing information is not found.
- **405 Method Not Allowed:** This error occurs when a request method other than GET is used. The response contains an error message indicating that only GET requests are allowed.

#### Additional Notes:

- The API follows RESTful principles.
- The API uses Django's built-in JsonResponse for handling JSON responses.
- The `PriceCalculator` class in `services.py` is responsible for calculating the total delivery price based on the provided parameters.
- The API provides comprehensive unit tests in `testview.py` and `testmodels.py` to ensure the functionality and reliability of the endpoints and models.






### Setup Guide

#### 1. Clone the Repository
```bash
git clone <repository_url>
cd <food_delivery>
```

#### 2. Create and Activate Virtual Environment
```bash
python3 -m venv my_env
source my_env/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Apply Migrations
```bash
python manage.py migrate
```
Follow the prompts to create a superuser account.

#### 5. Run the Development Server
```bash
python manage.py runserver
```

#### 6. Access the Application
- Open your web browser and go to `http://127.0.0.1:8000/` to access the application.
- To access the Django admin interface, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials created earlier.
