
from selenium import webdriver

navegador = webdriver.Chrome()
#Passo 1
navegador.get("https://practice.automationtesting.in/")
print("abriu")

#Passo 2
navegador.find_element('xpath','//*[@id="menu-item-50"]/a').click()
print("clicou")

#Passo 3
navegador.find_element('xpath','//*[@id="reg_email"]').send_keys("process_test2023@email.com")
print("digitou email")

#Passo 4
navegador.find_element('xpath','//*[@id="reg_password"]').send_keys("2023process2023")
print("digitou senha")

#Passo 5
navegador.find_element('xpath','/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]').click()
print("registrou")

#Passo 6
if (navegador.find_element('xpath','/html/body/div[1]/div[2]/div/div/div/div/div[1]/ul').is_displayed()):
    print("Não registou, mostrou a mensagem de error")