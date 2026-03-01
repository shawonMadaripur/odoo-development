project_directory/
    |
    |--module_a/
    |   |--controllers/
    |   |   |--__init__.py
    |   |   |--controller.py
    |   |
    |   |--data/
    |   |   |--data.xml
    |   |
    |   |--models/
    |   |   |--__init__.py
    |   |   |--model.py
    |   |
    |   |--security/
    |   |   |--ir.model.access.csv
    |   |
    |   |--views/
    |   |   |
    |   |   |--templates.xml
    |   |   |--views.xml
    |   |
    |   |--__init__.py
    |   |--__manifest__.py



# simple fields :
    - Boolean (True, False)
    - char & Text (string)
    - selection (list of string)
    - Float & Integer (Number)
    - Date & Datetime (dates)
    - Binary (To store file)
    - Html (formated Text)



#: Fields Attributes
    - String (field name displayed in the views)
    - invisible (True or False, dispalys the field or not in the views)
    - Readonly (True or False, if true then field can't be edited by user)
    - Required (True or False, if true then record can't be saved in database with an empty/null value
    - Default (set value on the field automatically during record creation)


#: demo/demo.xml
    - addining demo data

#: creating new group.
<odoo>
    <record id="estate_manager" model="res.groups">
        <fields name="name">Estate Manager</fields>
    </record>
</odoo>
--------------------> I can create new group for security.


#: Access Rights
    - id (external identifier for the access rule)
    - name (name of the access rule)
    - model_id:id (ID of the model that the access rule applies to.)
    - group_id:id (ID of the group that the access rule applies to)
    - perm_read (read permission for the access rule)
    - perm_write (write permission for access rule)
    - perm_create (create permission for the access rule)
    - perm_unlink (unlink permission for the access rule)


#: Action
    - open different type of window
    - open specific data/set of data
    # Triggered by
        - clicking on menuitem
        - clicking on button in views
        - contextual action on object


#: Action
    - id (external identifier)
    - model (fixed value of ir.actions.act_window)
    - name (name of action)
    - res_model (model which the action applies to)
    - view_mode (views that will be available{tree,form})


#: Fields Attributes
    - string
    - readonly
    - required
    - default 
    - domain


#: fields attribute in models
    - active = fields.Boolean(default=True) -----------> (default value set)
    - state = fields.Selection(
        [
            ("new", "New"),
            ("received", "offer Received"),
            ("accepted", "offer Accepted"),
            ("sold", "sold"),
            ("canceled", "canceled"),
        ],
        copy=False
    )  ----------------> selection field and can't paste duplicate value.

    - def default_date(self):
        return fields.Date.today()
    
    date = fields.Date(default=default_date) ---------> default date value set



#: Different types of view (model="ir.ui.view")
    - list
    - form
    - search
    - kanban
    - pivot
    - map
