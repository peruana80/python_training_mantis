def test_add_project(app, json_project):
    project = json_project
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)