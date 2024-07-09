from passlib.context import CryptContext


# Create a CryptContext object with bcrypt as the hashing scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a plain password
def hash_password(password):
    return pwd_context.hash(password)


# Function to verify a plain password against a hashed password
def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)
