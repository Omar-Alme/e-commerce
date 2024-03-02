## Manual Testing

### User Authentication

| Feature              | Description                                                      | Expected Result                 | Actual Result               | Pass/Fail |
|----------------------|------------------------------------------------------------------|---------------------------------|-----------------------------|-----------|
| Sign Up              | Create a new account with valid credentials                      | Account is created successfully| Account created successfully| Pass      |
| Login                | Log in with valid credentials                                    | User is logged in successfully  | User logged in successfully | Pass      |
| Forget Password      | Request a password reset email with valid email address           | Password reset email is sent    | Reset email sent            | Pass      |
| Reset Password       | Set a new password using the reset link sent via email           | New password is set successfully| New password set            | Pass      |
| Confirm New Password | Log in with the new password after resetting                     | User is logged in successfully  | User logged in successfully | Pass      |
| Email Verification   | Verify email by clicking the verification link after signing up  | Email is verified successfully | Email verified successfully | Pass      |

### Cart Functionalities

| Feature                | Description                                                     | Expected Result                  | Actual Result               | Pass/Fail |
|------------------------|-----------------------------------------------------------------|----------------------------------|-----------------------------|-----------|
| Add Product to Cart    | Add a product to the shopping cart                              | Product is added to the cart     | Product added to the cart   | Pass      |
| Increase Quantity      | Increase the quantity of a product in the cart                  | Quantity increases by one        | Quantity increased by one   | Pass      |
| Decrease Quantity      | Decrease the quantity of a product in the cart                  | Quantity decreases by one        | Quantity decreased by one   | Pass      |
| Remove Product         | Remove a product from the cart                                  | Product is removed from the cart | Product removed from the cart| Pass      |
| Open Product Detail    | View the details of a product                                  | Product detail page is displayed | Product detail page displayed| Pass      |
| Select Color and Size  | Choose color and size options for a product                    | Options are selected successfully| Options selected successfully| Pass      |
| Add Size and Color     | Add a product to cart with selected color and size options      | Product with options is added    | Product with options added  | Pass      |
| Cart Counter           | Verify that the cart counter updates correctly                  | Counter displays correct count   | Counter displays correct count| Pass      |

### Logged In User & User Profile

| Feature                   | Description                                                  | Expected Result                 | Actual Result               | Pass/Fail |
|---------------------------|--------------------------------------------------------------|---------------------------------|-----------------------------|-----------|
| Update Profile Image      | Upload a new profile image                                    | Image is updated successfully  | Image updated successfully  | Pass      |
| Update User Address       | Edit user address details                                      | Address details are updated     | Address details updated     | Pass      |

### Checkout Process

| Feature                  | Description                                                  | Expected Result                 | Actual Result               | Pass/Fail |
|--------------------------|--------------------------------------------------------------|---------------------------------|-----------------------------|-----------|
| Checkout Form            | Fill out the checkout form with valid information            | Form is submitted successfully | Form submitted successfully | Pass      |
| Checkout Functionality   | Proceed through the checkout process with a test product      | Order is placed successfully   | Order placed successfully   | Pass      |
| Stripe Checkout Session  | Verify that the Stripe checkout session is created correctly  | Session is created without errors | Session created without errors | Pass      |
| Test Card Payment        | Use Stripe test card details to simulate a payment            | Payment is processed successfully | Payment processed successfully | Pass      |
| Success URL              | Verify that the user is redirected to the success page        | Success page is displayed       | Success page displayed       | Pass      |
| Email Confirmation       | Check the email inbox for a confirmation email after checkout | Confirmation email is received  | Confirmation email received  | Pass      |


## Validators

### PEP 8

#### Cart App
 - admin.py
 ![Admin Cart](documentation/validations/cartadmin.png)

 - context_processor.py
 ![Context Cart](documentation/validations/cartcontext.png)

 - models.py
 ![Model Cart](documentation/validations/cartmodel.png)

 - urls.py
 ![URLS Cart](documentation/validations/carturl.png)

 - views.py
 ![Views Cart](documentation/validations/cartview.png)


#### Category App
 - admin.py
 ![Admin Category](documentation/validations/categoryadmin.png)

 - context_processor.py
 ![Context Category](documentation/validations/categorycontext.png)

 - models.py
 ![Model Category](documentation/validations/categorymodel.png)


#### Orders App
 - admin.py

 ![Admin Order](documentation/validations/orderadmin.png)

 - models.py

 ![Model Order](documentation/validations/ordermodel.png)

 - Form.py
 ![Form Order](documentation/validations/orderform.png)

 - views.py
 ![View Order](documentation/validations/orderview.png)

#### Product App
 - admin.py
 ![Admin Product](documentation/validations/productadmin.png)

 - models.py
 ![Model Product](documentation/validations/productmodel.png)

 - views.py
 ![View Product](documentation/validations/productview.png)

#### Users App
 - admin.py
 ![Admin User](documentation/validations/useradmin.png)

 - models.py
 ![Model User](documentation/validations/usermodel.png)

 - Form.py
 ![Admin User](documentation/validations/userform.png)

 - views.py
 ![Admin User](documentation/validations/userviews.png)


### W3C Jigsaw Validation

    There consists only one base.css file. 

![CSS Validation](documentation/validations/cssvalid.png)

### HTML Validation






## Lighthouse
     
 - Home Page
![Home Lighthouse](documentation/lighthouse/homelighthouse.png)


- Product Page
![Product Lighthouse](documentation/lighthouse/productslighthosue.png)


- Product Detail Page
![Product detail Lighthouse](documentation/lighthouse/productdetail-lighthouse.png)

- Cart Page
![Home Lighthouse](documentation/lighthouse/cartlighthouse.png)

- Sign Up Page
![Signup Lighthouse](documentation/lighthouse/singuplighthouse.png)

- Sign in Page
![Signin Lighthouse](documentation/lighthouse/singinlighthouse.png)

- Reset Password
![Reset Password Lighthouse](documentation/lighthouse/passwordreset-lighthouse.png)

- Dashboard Page
![Dashboard Lighthouse](documentation/lighthouse/dashboardlighthouse.png)

- Edit Profile Page
![Edit Profile Lighthouse](documentation/lighthouse/accountsettinglighthouse.png)

- Order History Page
![Home Lighthouse](documentation/lighthouse/orderhistoryligthouse.png)

- Checkout Page
![Home Lighthouse](documentation/lighthouse/checkoutligthhouse.png)

- Success Checkout Page
![Home Lighthouse](documentation/lighthouse/successcheckout-lighthouse.png)