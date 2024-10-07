# FormTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Form Template | 
**description** | **str** | The Description of the Form Template | 

## Example

```python
from procore_sdk.models.form_template import FormTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of FormTemplate from a JSON string
form_template_instance = FormTemplate.from_json(json)
# print the JSON string representation of the object
print(FormTemplate.to_json())

# convert the object into a dict
form_template_dict = form_template_instance.to_dict()
# create an instance of FormTemplate from a dict
form_template_from_dict = FormTemplate.from_dict(form_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


