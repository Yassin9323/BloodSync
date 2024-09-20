# BloodSync

**BloodSync** An internal web application designed to seamlessly connect hospitals with blood banks.  BloodSync addresses the critical need for efficeint blood bank operations by providing a user friendly interface for hospitals and blood banks to track and manage blood supplies.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## About the Project

BloodSync aims to tackle the challenge of ensuring that hospitals always have a reliable supply of blood bags in stock providing a scalable, and user-friendly platform. By leveraging real-time communication, BloodSync ensures that blood bag requests and transfers are handled swiftly, reducing delays in critical healthcare scenarios. 

## Features

- **Real-time Updates**: Leverages WebSocket and AJAX to provide real-time updates of blood requests and inventory stock.
- **Recipient Requests**: Hospitals can easily submit requests to blood banks through the system, ensuring a timely supply of the required blood bags.
- **Blood Bank Management**: Blood banks can track their inventory, manage blood stocks, and notify users when certain blood types are low.
- **Secure User Authentication**: Implements secure user registration and login with password encryption.
- **Dashboard for Monitoring**: An admin dashboard that provides real-time insights and tracking of Blood requests and stock levels.

## Technologies Used

- **Backend**: FastApi, Python
- **Frontend**: HTML, CSS, JavaScript (AJAX, WebSocket, JQuery)
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Real-time Functionality**: WebSocket, AJAX
- **Version Control**: Git, GitHub
- **UI/UX**: Figma

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yassin9323/BloodSync.git
   ```
2. Navigate to the project directory:
   ```bash
   cd BloodSync
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv sync
   source sync/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up environment variables (e.g., `DATABASE_URL`):
   ```bash
   export DATABASE_URL="your_postgresql_db_url"
   ```
6. Navigate to backend directory:
    ```bash
    cd backend
    ```
7. Run the application:
   ```bash
   fastapi dev main.py
   ```

## Usage

1. Register as a hospital or bloodbank admin.
2. Access the dashboard to monitor blood availability.
3. Post requests for blood or respond to donor alerts in real-time.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact

**Yassin Waleed**  
Email: yassin.waleed94@gmail.com  
GitHub: [Yassin9323](https://github.com/Yassin9323)

**Yousra Adel**  
Email: yousraaadel@gmail.com  
GitHub: [Yousraaa-adel](https://github.com/Yousraaa-adel)

---
