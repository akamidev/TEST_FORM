from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration du WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Chemin vers ChromeDriver
service = Service('C:/chromedriver-win64/chromedriver.exe')  # Remplace par le chemin correct
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL du formulaire de contact
url = "https://akamimehdi.netlify.app/Contact"
driver.get(url)

# Fonction pour remplir et soumettre le formulaire
def fill_contact_form():
    try:
        # Remplir le champ "Nom"
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Votre Nom']"))
        )
        name_field.send_keys("AKAMIMEHDI")

        # Remplir le champ "E-mail"
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Votre E-mail']")
        email_field.send_keys("akamimehdi.dev@example.com")

        # Remplir le champ "Message"
        message_field = driver.find_element(By.XPATH, "//textarea[@placeholder='Votre Message']")
        message_field.send_keys("Ceci est un message de test envoyé via Selenium.")

        # Cliquer sur le bouton "Envoyer"
        submit_button = driver.find_element(By.XPATH, "//button[text()='Envoyer']")
        submit_button.click()

        print("Formulaire soumis avec succès !")
    except Exception as e:
        print("Erreur lors de la soumission du formulaire :", e)

# Exécuter la fonction
fill_contact_form()

# Attendre quelques secondes avant de fermer le navigateur
time.sleep(5)
driver.quit()
