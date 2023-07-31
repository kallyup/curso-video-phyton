import time
from selenium import webdriver

navegador = webdriver.Chrome()

#Passo 1
navegador.get("https://practice.automationtesting.in/shop")
print("abriu a página")
time.sleep(3)

#Passo 2
navegador.find_element('xpath','//*[@id="wpmenucartli"]/a').click()
print("clicou no carrinho")
time.sleep(3)

#Passo 3
navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")#descer a página
navegador.find_element('xpath','//*[@id="content"]/ul/li[6]/a[1]/h3').click()
print("Clicou no Mastering JavaScript")
time.sleep(3)

#Passo 4
navegador.find_element('xpath','//*[@id="product-165"]/div[2]/form/button').click()
print("Adicionou ao carrinho")
time.sleep(3)

#Passo 5
navegador.find_element('xpath','//*[@id="content"]/div[1]/a').click()
print("Clicou no View Basket")
time.sleep(3)

#Passo 6
navegador.find_element('xpath','//*[@id="page-34"]/div/div[1]/div/div/div/a').click()
print("Clicou no Proceed to checkout")
time.sleep(3)

#Passo 7 até 10
navegador.find_element('xpath','//*[@id="billing_first_name"]').send_keys("TestFirstName")
navegador.find_element('xpath','//*[@id="billing_last_name"]').send_keys("TestLastName")
navegador.find_element('xpath','//*[@id="billing_email"]').send_keys("test@email.com")
navegador.find_element('xpath','//*[@id="billing_phone"]').send_keys("81999999999")
print("Preencheu os campos de First Name, Last Name, email e Phone")
time.sleep(3)

#Passo 11
navegador.find_element('xpath','//*[@id="s2id_billing_country"]/a/span[2]/b').click()
navegador.find_element('xpath','//*[@id="s2id_autogen1_search"]').send_keys("brazil")
navegador.find_element('xpath','//*[@id="select2-result-label-1067"]/span').click()
print("Selecionou Brazil")
time.sleep(3)

#Passo 12 e 13
navegador.find_element('xpath','//*[@id="billing_address_1"]').send_keys("MyStreet")
navegador.find_element('xpath','//*[@id="billing_city"]').send_keys("Recife")
print("Preencheu os campos de Address e City")
time.sleep(3)

#Passo 14
navegador.find_element('xpath','//*[@id="s2id_billing_state"]/a/span[2]/b').click()
navegador.find_element('xpath','//*[@id="s2id_autogen2_search"]').send_keys("pernambuco")
navegador.find_element('xpath','//*[@id="select2-result-label-1235"]').click()
print("Selecionou Pernambuco")
time.sleep(3)

#Passo 15
navegador.find_element('xpath','//*[@id="billing_postcode"]').send_keys("50740-560")
print("Preencheu o CEP")
time.sleep(3)

#Passo 16
navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)") #descer a página
if (navegador.find_element('xpath','//*[@id="order_review"]/table/tfoot/tr[3]/td/strong/span/text()').text == "367.50"):
    print("O valor estar correto = 367.50")
time.sleep(3)

#Passo 17
navegador.find_element('xpath','//*[@id="payment_method_cod"]').click()
print("Marcou o Cash on Delivery")
time.sleep(3)

#Passo 18
navegador.find_element('xpath','//*[@id="place_order"]').click()
print("Clicou no botão Place Order")