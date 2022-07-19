from django import forms
from django_jsonforms.forms import JSONSchemaField




class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class CustomForm(forms.Form):
    first_name_schema = {
        "type": "object",
        "required": ["First Name"],
        "properties": {
            "First Name": {
                "type": "string",
                "maxLength": 30
            }
        }
    }

    last_name_schema = {
        "type": "object",
        "required": ["Last Name"],
        "properties": {
            "Last Name": {
                "type": "string",
                "maxLength": 30,
            }
        }
    }
    Person_schema = {
            "title": "Person",
            "type": "object",
            "id": "person",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "First and Last name",
                    "minLength": 4
                },
                "age": {
                    "type": "integer",
                    "default": 21,
                    "minimum": 18,
                    "maximum": 99
                },
                "gender": {
                    "type": "string",
                    "enum": [
                        "male",
                        "female"
                    ]
                }
            }
        }

    options = {"no_additional_properties": True}
    first_name = JSONSchemaField(schema = Person_schema, options = options)
    last_name = JSONSchemaField(schema = last_name_schema, options = options)