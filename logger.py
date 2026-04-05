import logging
import mysql.connector

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='verification_attempts.log',
                    filemode='a')

class DatabaseLogger:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def log_verification_attempt(self, user_id, success):
        try:
            logging.info(f'Logging verification attempt for user: {user_id}')
            query = "INSERT INTO verification_logs (user_id, success, timestamp) VALUES (%s, %s, NOW())"
            self.cursor.execute(query, (user_id, success))
            self.connection.commit()
            logging.info(f'Successfully logged: {user_id}, Success: {success}')
        except Exception as e:
            logging.error(f'Error logging verification attempt: {e}')

    def close(self):
        self.cursor.close()
        self.connection.close()