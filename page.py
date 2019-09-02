from selenium.webdriver.common.by import By


class Page(object):

    start_tutorial_button = (By.ID, 'com.adobe.lrmobile:id/startTutorialButton')

    continue_button = (By.ID, "com.adobe.lrmobile:id/continueButton")

    tutorial_next = (By.ID, "com.adobe.lrmobile:id/tutorial_next")

    tutorial_step_text = (By.ID, "com.adobe.lrmobile:id/tutorial_step_text")
