from urllib import request

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Assignment_six.BaseTest import BaseTest, add_log
from Assignment_six.PageObject import PageObject

@pytest.mark.usefixtures("data_provide")
class Test_main(BaseTest):
    def test_radiobutton(self,data_provide):
        logs=add_log()
        logs.info("test started")
        self.driver.implicitly_wait(5)
        logs.info("Testing for Radio button")
        radio_button=PageObject.radio_button_2(self)
        radio_button.click()
        try:
            assert radio_button.is_enabled()
            logs.info("Radio button is clicked")
        except:
            print("Error: button is not clicked")
            logs.error("Radio button is not clicked")

        logs.info("Testing suggestion box")
        suggest_box=PageObject.suggestion_box(self)
        suggest_box.send_keys(data_provide[0])
        suggested_names=PageObject.suggested_names(self)
        print(suggested_names)
        for names in suggested_names:
            print(names.text)
            if names.text == "Indonesia":
                names.click()
        suggest_drop_box_value = self.driver.execute_script('return document.getElementById("autocomplete").value')
        print("The value in the drop box value is", suggest_drop_box_value)
        logs.debug("The name in the suggestion drop box is ",suggest_drop_box_value)

        try:
            assert suggest_drop_box_value=='Indonesia'
            logs.info("Indonesia is selected")
        except:
            print("entered name is not correct")
            logs.error("Error with suggestion box")


        select_o=Select(PageObject.select_dropdownbox(self))
        select_option=select_o.select_by_value("option2")
        select_val=PageObject.selectdropdown_values(self).text
        print(select_val)
        try:
            assert select_val=="Option2"
            logs.info("option2 is selected")
        except:
            print("selected option is worng")
            logs.error("Error with dropdown")

        #test for checkbox
        checkbox2=PageObject.checkbox_2(self)
        checkbox2.click()

        checkbox3=PageObject.checkbox_3(self)
        checkbox3.click()
        try:
            assert checkbox2.is_selected()
            logs.info("Checkbox2 is selected")
        except:
            print("check box 2 is not selected")
        try:
            assert checkbox3.is_selected()
            logs.info("Checkbox 3 is selected")
        except:
            print("check box 3 is not selected")
            logs.error("Error in Checkbox 3")

        #Alert for accept button
        logs.info("Test for alert button")
        alert_name=PageObject.alert_name_m(self)
        alert_name.send_keys(data_provide[1])
        PageObject.alert_button_m(self).click()
        #alert_button.click()
        alert_switch=self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        try:
            assert data_provide[1] in alert_switch
            logs.info("Name in alert button is asserted")
        except:
            print("the name in alert is not expected one")
            logs.error("Error: Name in alert button is not fetched")

        #test for alert confirm button
        alert_name = PageObject.alert_name_m(self)
        alert_name.send_keys(data_provide[1])
        PageObject.alert_confm_button_m(self).click()
        alert_text=self.driver.switch_to.alert.text
        self.driver.switch_to.alert.dismiss()
        try:
            assert data_provide[1] in alert_text
            logs.info("Name in alert box after clicking cancel button is asserted")
        except:
            print("Alert box did not show  up")
            logs.info("Error: Alert button after clicking cancel button")

        #Window handles
        logs.info("Test for window handles")
        PageObject.window_handles(self).click()
        win_num=self.driver.window_handles
        self.driver.switch_to.window(win_num[1])
        child_title = self.driver.title
        print("child window title ", child_title)
        logs.debug("The name of child window is ",child_title)
        self.driver.close()
        self.driver.switch_to.window(win_num[0])
        parent_title = self.driver.title
        print("Parent window title", parent_title)
        logs.debug("Parent window title", parent_title)
        #Test for Table
        logs.info("Fetching Selenium name from the list")
        table_list=PageObject.table_values(self)
        selenium_count = []
        for value in table_list:
            coloumn_value = value.text
            if "Selenium" in coloumn_value:
                selenium_count.append(coloumn_value)
        print("the name of the course containing selenium ", selenium_count)
        logs.debug("the name of the course containing selenium ", selenium_count)
        print("number of course containing selenium are ", selenium_count.__len__())
        logs.debug("number of course containing selenium are ", selenium_count.__len__())

        # test for visible text
        PageObject.visible_text_m(self).send_keys(data_provide[1])
        PageObject.hide_button_m(self).click()
        try:
            assert not PageObject.visible_text_m(self).is_displayed()
            logs.info("visible text is displayed after hide button")
        except:
            print("Error: hide button is not working")
            logs.error("Error: Hide button is not working")

        PageObject.show_button_m(self).click()
        try:
            assert PageObject.visible_text_m(self).is_displayed()
            logs.info("visible text is displayed after show button")
        except:
            print("show button is not working")
            logs.error("Error: show button is not working")
        elemnet_visible_text_value = self.driver.execute_script("return document.getElementById('displayed-text').value")
        print("the entered name is ", elemnet_visible_text_value)
        logs.debug("the entered name is ", elemnet_visible_text_value)

        #Test for Tab button
        PageObject.tab_button_m(self).click()
        windows_name = self.driver.window_handles
        self.driver.switch_to.window(windows_name[1])
        child_title = self.driver.title
        print(" the name other tab", child_title)
        logs.debug(" the name other tab", child_title)
        self.driver.close()
        self.driver.switch_to.window(windows_name[0])

        #Test for mouse hover

        action = ActionChains(self.driver)
        action.move_to_element(PageObject.mouse_hover_m(self)).perform()
        for value in PageObject.items_in_mousehover_m(self):
            print("the values in mouse  hover", value.text)

        logs.debug("the values in mouse  hover", value.text)
        #Test for iframes
        logs.info("Test for iframes")
        frames_count=PageObject.iframes_m(self).__len__()
        print("number of frames are ", frames_count)
        logs.debug("number of frames are ", frames_count)
        self.driver.switch_to.frame("iframe-name")

        #getting all links
        url_list = []
        url_list = PageObject.links_present_m(self)
        url_count=url_list.__len__()
        print("number of links present", url_count)
        logs.debug("number of links present", url_count)
        for lst in url_list:
            if "None" in lst.get_property("href"):
                continue
            else:
                print(lst.get_property("href"))

        self.driver.switch_to.parent_frame()
        logs.info("End of test")
        self.driver.quit()


