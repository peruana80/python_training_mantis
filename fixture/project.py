from model.project import Project


class ProjectHelper:
    def __init__(self,app):
        self.app = app


    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("input.button-small").click()


    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_id('project-name').send_keys(project.name)
        #wd.find_element_by_css_selector('#project_status').send_keys(project)
        #wd.find_element_by_css_selector('#project-view-state').send_keys(project)
        wd.find_element_by_id('project-description').send_keys(project.description)


    def select_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        project_row = wd.find_element_by_xpath("//h2[text()='Projects']/following-sibling::table//tbody//tr[%s]" % index)
        project_row.find_element_by_xpath("td[1]//a").click()


    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//fieldset//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@type='submit'][@value = 'Add Project']").click()
        self.open_project_page()
        self.project_cache=None

#    def delete_project_by_index(self, index):
#        wd = self.app.wd
#        self.select_project_by_index(index)
#        wd.find_element_by_xpath("//input[@class='button'][@value ='Usuń projekt']").click()
#        #confirm removing
#        wd.find_element_by_xpath("//input[@class='button'][@value ='Usuń projekt']").click()
#        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_xpath("//h2[text()='Projects']/following-sibling::table//tbody//tr"))

    project_cache=None
    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//h2[text()='Projects']/following-sibling::table//tbody//tr"):
                cell = element.find_element_by_xpath("td//a")
                name = cell.text
                cells = element.find_elements_by_xpath("td")
                status = cells[2].text
                viewstate = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, status=status, viewstate=viewstate,description=description))
        return list(self.project_cache)