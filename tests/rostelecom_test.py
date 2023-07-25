from settings import *
import pytest


# T-1 Открывается cтраница c формой "Авторизация", вкладка "Телефон".
def test_phone_auth(browser, auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# T-2 Открывается cтраница c формой "Авторизация", вкладка "Почта".
def test_mail_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)


# T-3 Открывается cтраница c формой "Авторизация", вкладка "Логин".
def test_login_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    assert auth.find_element(auth.LOCATOR_BTN_LOGIN)


# T-4 Открывается cтраница c формой "Авторизация", вкладка "Лицевой счет".
def test_account_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    assert auth.find_element(auth.LOCATOR_BTN_LS)


# T-5 Вызов формы "Восстановление пароля".
def test_password_recovery_form(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# T-6 Вызов формы "Регистрация".
def test_registration_form(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION

# T-7 (авторизация по незарегистрированным телефону и паролю)
def test_auth_fake_phone(selenium):
    form = AuthForm(selenium)

    # вводим телефон и пароль
    form.username.send_keys('+79175862568')
    form.password.send_keys('fkvbkdjghbfj')
    sleep(25) #  вводим вручную
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'
