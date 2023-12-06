from selenium import webdriver
import time
import unittest

class PruebaRegistroUsuario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Asegúrate de tener el driver adecuado instalado y en el PATH
        self.driver.get("http://127.0.0.1:5500/index.html")  # Reemplaza con la URL de tu aplicación
        self.driver.maximize_window()

    def test_registro_usuario_exitoso(self):
        # Simula el proceso de registro exitoso
        self.driver.find_element_by_link_text("Registrarse").click()

        # Completa el formulario de registro con información válida
        self.driver.find_element_by_name("nombre").send_keys("Nombre de Prueba")
        self.driver.find_element_by_name("email").send_keys("prueba@email.com")
        self.driver.find_element_by_name("contrasena").send_keys("contrasena123")
        self.driver.find_element_by_name("btn-registro").click()

        # Verifica que el usuario sea redirigido a la página de inicio de sesión
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5500/index.html")

    def test_registro_usuario_con_informacion_invalida(self):
        # Simula el proceso de registro con información inválida
        self.driver.find_element_by_link_text("Registrarse").click()

        # Completa el formulario de registro con información inválida
        self.driver.find_element_by_name("nombre").send_keys("Nombre de Prueba")
        self.driver.find_element_by_name("email").send_keys("email_invalido")
        self.driver.find_element_by_name("contrasena").send_keys("contrasena123")
        self.driver.find_element_by_name("btn-registro").click()

        # Verifica que se muestre un mensaje de error
        mensaje_error = self.driver.find_element_by_id("mensaje-error").text
        self.assertIn("Email inválido", mensaje_error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
