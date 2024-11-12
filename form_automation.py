import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration du WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-infobars")

service = Service('C:/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL du formulaire de contact
form_url = "https://akamimehdi.netlify.app/Contact"
driver.get(form_url)

# Fonction pour gérer la fenêtre de consentement des cookies
def handle_cookies():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )
        driver.execute_script("""
            let buttons = document.querySelectorAll('button');
            buttons.forEach(button => {
                if (button.innerText.includes('Tout refuser') || button.innerText.includes('Reject all')) {
                    button.click();
                }
            });
        """)
        print("Fenêtre de consentement des cookies gérée avec succès.")
    except Exception as e:
        print("Erreur lors de la gestion des cookies :", e)

# Fonction pour remplir et soumettre le formulaire
def fill_form_and_submit(name, email, message):
    try:
        # Remplir les champs du formulaire
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Votre Nom']"))
        )
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Votre E-mail']")
        message_field = driver.find_element(By.XPATH, "//textarea[@placeholder='Votre Message']")
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer')]")

        name_field.send_keys(name)
        email_field.send_keys(email)
        message_field.send_keys(message)

        print("Formulaire rempli avec succès.")

        # Cliquer sur le bouton "Envoyer"
        submit_button.click()
        print("Formulaire soumis avec succès.")

        # Enregistrer les données dans la base de données
        save_to_database(name, email, message)

    except Exception as e:
        print("Erreur lors de la soumission du formulaire :", e)

# Fonction pour enregistrer les données dans SQLite
def save_to_database(name, email, message):
    try:
        conn = sqlite3.connect('data/form_data.db')
        cursor = conn.cursor()

        # Insertion des données dans la table
        cursor.execute('''
        INSERT INTO form_submissions (name, email, message)
        VALUES (?, ?, ?)
        ''', (name, email, message))

        conn.commit()
        print("Données enregistrées dans la base de données avec succès.")
    except Exception as e:
        print("Erreur lors de l'enregistrement des données :", e)
    finally:
        conn.close()

# Gérer la fenêtre de consentement
handle_cookies()

# Remplir et soumettre le formulaire
fill_form_and_submit("AKAMIMEHDI", "akamimehdi.dev^gmail.com", "Ceci est un message de test.'Hola que tal' ")

# Attendre quelques secondes avant de fermer le navigateur
time.sleep(5)
driver.quit()
