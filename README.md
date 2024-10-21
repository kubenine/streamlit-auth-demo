
# Streamlit Authentication Setup

This project demonstrates how to set up simple username and password authentication in **Streamlit** using the **streamlit-authenticator** library. Below are the steps to get the project running.

## Prerequisites

Make sure you have the following installed on your system:

- **Python 3.x**
- **pip** (Python package manager)

## Installation Steps

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/kubenine/streamlit-auth-demo.git
cd kubenine-authentication
```

### 2. Install Required Libraries

Install all necessary libraries by running the following command:

```bash
pip install -r requirements.txt
```

### 3. Set Up Credentials

Create a file named `credentials.yaml` to store the user credentials and cookie settings.

**Example `credentials.yaml` file:**

```yaml
credentials:
  usernames:
    admin:
      name: admin
      email: admin@example.com
      password: <hashed_password_here>  # Replace with your bcrypt-hashed password

cookie:
  expiry_days: 30
  key: superstrongkey
  name: demo_cookie
```

### 4. Hash the Password

Use the `hash.py` script to hash your password securely:

```bash
python hash.py
```

Replace the `<hashed_password_here>` in your `credentials.yaml` file with the generated hash.

### 5. Run the Application

After setting up the credentials, you can start the Streamlit app:

```bash
streamlit run main.py
```

This will open the app in your default browser. Log in using the credentials you set in `credentials.yaml`.

## Need Help?

If you need assistance or want to implement similar solutions for your projects, feel free to contact **KubeNine**. We offer specialized DevOps and cloud solutions tailored to your needs.
