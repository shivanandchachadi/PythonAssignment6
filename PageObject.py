from selenium.webdriver.common.by import By

from Assignment_six.BaseTest import add_log


class PageObject:
    log= add_log()
    log.info("Locators from Pageobject")
    radio_button_two = (By.XPATH, "//input[@value='radio2']")
    suggest_box=(By.ID,"autocomplete")
    suggested_name=(By.XPATH,"//li[@class='ui-menu-item']/div")
    suggest_drop_box_value = (By.XPATH,)
    select_dropdown=(By.ID,"dropdown-class-example")
    select_value=(By.XPATH,"//*[@id='dropdown-class-example']/option[@value='option2']")
    checkbox2=(By.ID,"checkBoxOption2")
    checkbox3=(By.ID,"checkBoxOption3")
    alert_name=(By.ID,"name")
    alert_button=(By.ID,"alertbtn")
    alert_confm_button=(By.ID,"confirmbtn")
    window_handle=(By.ID,"openwindow")
    table_value=(By.XPATH,"(//table[@id='product']/tbody/tr)/child::td[2]")
    visible_text=(By.ID,"displayed-text")
    hide_button=(By.ID,"hide-textbox")
    show_button=(By.ID,"show-textbox")
    tab_button=(By.ID,"opentab")
    mouse_hover=(By.CLASS_NAME,"mouse-hover")
    items_in_mousehover=(By.XPATH,"//div[@class='mouse-hover']/div/a")
    iframes=(By.XPATH,"//iframe")
    links_present=(By.TAG_NAME,"a")


    def __init__(self,driver):
        self.driver=driver
    def links_present_m(self):
        return self.driver.find_elements(*PageObject.links_present)
    def iframes_m(self):
        return self.driver.find_elements(*PageObject.iframes)
    def items_in_mousehover_m(self):
        return self.driver.find_elements(*PageObject.items_in_mousehover)
    def mouse_hover_m(self):
        return self.driver.find_element(*PageObject.mouse_hover)
    def tab_button_m(self):
        return self.driver.find_element(*PageObject.tab_button)
    def show_button_m(self):
        return self.driver.find_element(*PageObject.show_button)
    def hide_button_m(self):
        return self.driver.find_element(*PageObject.hide_button)
    def visible_text_m(self):
        return self.driver.find_element(*PageObject.visible_text)
    def table_values(self):
        return self.driver.find_elements(*PageObject.table_value)
    def alert_confm_button_m(self):
        return self.driver.find_element(*PageObject.alert_confm_button)

    def window_handles(self):
        return self.driver.find_element(*PageObject.window_handle)

    def alert_name_m(self):
        return self.driver.find_element(*PageObject.alert_name)

    def alert_button_m(self):
        return self.driver.find_element(*PageObject.alert_button)


    def radio_button_2(self):
        return self.driver.find_element(*PageObject.radio_button_two)

    def suggestion_box(self):
        return self.driver.find_element(*PageObject.suggest_box)

    def suggested_names(self):
        return self.driver.find_elements(*PageObject.suggested_name)


    def select_dropdownbox(self):
        return self.driver.find_element(*PageObject.select_dropdown)


    def selectdropdown_values(self):
        return self.driver.find_element(*PageObject.select_value)


    def checkbox_2(self):
        return self.driver.find_element(*PageObject.checkbox2)


    def checkbox_3(self):
        return self.driver.find_element(*PageObject.checkbox3)
