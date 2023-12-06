import allure
from selenium import webdriver
import unittest

class PruebaRegistroUsuario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("URL_DE_TU_APLICACION")
        self.driver.maximize_window()

    @allure.story('Registro de Usuario Exitoso')
    def test_registro_usuario_exitoso(self):
        with allure.step("Clic en Registrarse"):
            self.driver.find_element_by_link_text("Registrarse").click()
        
        with allure.step("Completar formulario de registro"):
            self.driver.find_element_by_name("nombre").send_keys("Nombre de Prueba")
            self.driver.find_element_by_name("email").send_keys("prueba@email.com")
            self.driver.find_element_by_name("contrasena").send_keys("contrasena123")
            self.driver.find_element_by_name("btn-registro").click()

        with allure.step("Verificar redirección a la página de inicio de sesión"):
            self.assertEqual(self.driver.current_url, "URL_ESPERADA_DE_LA_PAGINA_DE_INICIO_DE_SESION")

    @allure.story('Registro de Usuario con Información Inválida')
    def test_registro_usuario_con_informacion_invalida(self):
        with allure.step("Clic en Registrarse"):
            self.driver.find_element_by_link_text("Registrarse").click()

        with allure.step("Completar formulario de registro con información inválida"):
            self.driver.find_element_by_name("nombre").send_keys("Nombre de Prueba")
            self.driver.find_element_by_name("email").send_keys("email_invalido")
            self.driver.find_element_by_name("contrasena").send_keys("contrasena123")
            self.driver.find_element_by_name("btn-registro").click()

        with allure.step("Verificar mensaje de error"):
            mensaje_error = self.driver.find_element_by_id("mensaje-error").text
            self.assertIn("Email inválido", mensaje_error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
